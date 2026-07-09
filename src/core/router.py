from fastapi import APIRouter

from src.account.router import router as account_router
from src.authentication.routers.auth import router as auth_router
from src.chat.server import  router as chat_router

router = APIRouter(
    prefix="/api",
)

router.include_router(account_router)
router.include_router(auth_router)
router.include_router(chat_router)