from sqlalchemy.ext.asyncio import AsyncSession

from src.account.models import User
from src.account.repositories.user import UserRepository
from src.account.schemas.users import UserCreateSchema, UserUpdateSchema


class UserAlreadyExist(Exception):
    pass

class UserNotFound(Exception):
    pass

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = UserRepository(session=session)

    async def check_exist(self,email: str = None, user_id: int = None) -> bool:
        if email:
            return bool(await self.repository.check_exist_email(email=email))
        if user_id:
            return bool(await self.repository.check_exist_user_id(user_id=user_id))
        return False


    async def create(self, user_schema: UserCreateSchema) -> User:
        if await self.check_exist(email=user_schema.email):
            raise UserAlreadyExist
        return await self.repository.create(user_schema=user_schema)


    async def get_one(self, user_id: int)  -> User:
        if await self.check_exist(user_id=user_id):
            return await self.repository.get_one(user_id=user_id)
        raise UserNotFound

    async def get_all(self)  -> list[User]:
        return list(await self.repository.get_all())

    async def update(self, user_id: int, user_schema: UserUpdateSchema) -> User:
        user = await self.get_one(user_id=user_id)
        return await self.repository.update(user=user, user_schema=user_schema)

    async def remove(self, user_id: int) -> None:
        user = await self.get_one(user_id=user_id)
        await self.repository.remove(user=user)