from fastapi import APIRouter
from fastapi import Depends, FastAPI
router = APIRouter(tags=["AUTHENTICATION"])

from typing import Annotated


from fastapi.security import OAuth2PasswordBearer



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}