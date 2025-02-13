from fastapi import APIRouter, Depends
from models.user_models import User
from dependencies import get_current_user


router = APIRouter(prefix="/users")


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return {"username": current_user.username, "email": current_user.email}
