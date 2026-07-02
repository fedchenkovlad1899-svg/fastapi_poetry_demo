from enum import StrEnum

class UserSexEnum(StrEnum):
    MALE = 'male'
    FEMALE = 'female'


class UserStatusEnum(StrEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'