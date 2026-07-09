
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from src.account.constants import UserSexEnum, UserStatusEnum


class BaseUserSchema(BaseModel):
    fullname: str
    name: str | None = None

class UserCreateSchema(BaseUserSchema):
    email: EmailStr
    sex: UserSexEnum
    status: UserStatusEnum
    age: int | None = Field(ge=0)


class UserUpdateSchema(BaseUserSchema):
    pass


class UserResponseSchema(BaseUserSchema):
    id:int
    email: EmailStr
    sex: UserSexEnum
    age: int | None = None
    created_at: datetime
    updated_at: datetime
    status: UserStatusEnum



