from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.account.models.user import Base
from src.core.config import settings

sync_engine = create_engine(settings.db.db_sync_url,echo=True)
async_engine = create_async_engine(settings.db.db_async_url, echo=True)


sync_session_marker = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
async_session_marker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


def get_sync_session():
    with Session(sync_engine) as session:
        return session

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_marker() as session:
        yield session




# Base.metadata.create_all(sync_engine)