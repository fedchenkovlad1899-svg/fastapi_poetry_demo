from http import HTTPMethod

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

from src.account.dependencies import get_user_service
from src.account.schemas.users import (UserCreateSchema, UserResponseSchema,
                                       UserUpdateSchema)
from src.account.services.user import (UserAlreadyExist, UserNotFound,
                                       UserService)
from src.core.database import get_async_session, get_sync_session

router = APIRouter(
    prefix="/users",
    tags=["Account"]
)


@router.post(
    path="/",
    response_model = UserResponseSchema,
    status_code=201
)
async def create_user(
    user_schema: UserCreateSchema,
    user_service: UserService = Depends(get_user_service)
):
    try:
        return await user_service.create(user_schema=user_schema)
    except UserAlreadyExist:
        raise HTTPException(status_code=403, detail=f"User already exists")

@router.get(
    path="/{user_id}",
    response_model = UserResponseSchema,
    status_code=200
)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = await user_service.get_one(user_id=user_id)
        return user
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")


@router.get(
    path="/",
    response_model = list[UserResponseSchema],
    status_code=200
)
async def get_users(
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_all()

@router.put(
    path="/{user_id}",
    response_model = UserResponseSchema,
    status_code=200
)
async def update_user(
    user_id: int,
    user_schema: UserUpdateSchema,
    user_service: UserService = Depends(get_user_service)
):
    try:
        return await  user_service.update(user_id=user_id,user_schema=user_schema)
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")

@router.delete(
    path="/{user_id}",
    status_code=204
)
async def remove_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    try:
        return await user_service.remove(user_id=user_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail=f"User not found")


