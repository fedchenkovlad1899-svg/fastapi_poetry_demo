from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.account.services.user import UserService
from src.core.database import get_async_session


async def get_user_service(session: AsyncSession = Depends(get_async_session)):
    return UserService(session)