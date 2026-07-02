from datetime import datetime

from pydantic import BaseModel

from src.account.constants import UserSexEnum,UserStatusEnum


class UserCreateSchema(BaseModel):
    fullname: str
    email: str
    sex: UserSexEnum
    status: UserStatusEnum = UserStatusEnum.ACTIVE


class UserResponseSchema(BaseModel):
    id:int
    fullname: str
    email: str
    sex: UserSexEnum
    name: str | None = None
    age: int | None = None
    created_at: datetime
    updated_at: datetime
    status: UserStatusEnum