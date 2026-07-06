from fastapi import APIRouter

from .role import router as role_router
from .user import router as user_router

router = APIRouter(
    prefix="/account",
    tags=["Account"]
)
router.include_router(user_router)
router.include_router(role_router)