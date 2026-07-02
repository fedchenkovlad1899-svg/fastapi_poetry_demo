from typing import Annotated
from src.account.constants import UserSexEnum,UserStatusEnum
from sqlalchemy.orm import Mapped,mapped_column


from src.core.orm import (
    primary_integer,
    string_64_nullable,
    string_64_not_nullable,
    simple_integer_nullable,
    string_64_unique,
    Base,
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[primary_integer]
    name: Mapped[string_64_nullable]
    fullname: Mapped[string_64_not_nullable]
    age: Mapped[simple_integer_nullable]
    sex: Mapped[Annotated[str, UserSexEnum]]
    email: Mapped[string_64_unique]
    password: Mapped[string_64_nullable]
    status: Mapped[Annotated[str, UserStatusEnum]] = mapped_column(default=UserStatusEnum.ACTIVE)




