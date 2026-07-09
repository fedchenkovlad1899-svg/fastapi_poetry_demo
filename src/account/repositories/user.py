from typing import Any, Sequence

from sqlalchemy import Row, RowMapping, ScalarResult, select
from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.models import User
from src.account.schemas.users import UserCreateSchema, UserUpdateSchema


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,user_schema: UserCreateSchema) -> User:
        user = User(
            fullname=user_schema.fullname,
            email=user_schema.email,
            sex=user_schema.sex.value,
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.flush()

        return user

    async def get_one(self, user_id: int) -> User:
        stm = select(User).where(User.id==user_id)
        result = await self.session.execute(stm)
        return result.scalars().one()


    async def check_exist_email(self, email: str) -> Sequence[User]:
        stm = select(User).where(User.email == email)
        result = await self.session.execute(stm)
        return result.scalars().fetchall()


    async def check_exist_user_id(self,user_id: int) -> Sequence[User]:
        stm = select(User).where(User.id == user_id)
        result = await self.session.execute(stm)
        return result.scalars().fetchall()




    async def get_all(self) -> ScalarResult[User]:
        stm = select(User)
        result = await self.session.execute(stm)
        return result.scalars()


    async def update(
         self,
         user: User,
         user_schema: UserUpdateSchema,
    ) -> User:
        for name, value in user_schema.model_dump().items():
            setattr(user, name, value)
        await self.session.commit()
        await self.session.flush()
        return user


    async def remove(self, user: User):
        await self.session.delete(user)
        await self.session.commit()






