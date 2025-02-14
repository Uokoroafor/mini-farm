from crud.user_crud import UserCRUD
from auth.security import verify_password


# Authenticate user
async def authenticate_user(username: str, password: str, user_crud: UserCRUD):
    user = await user_crud.get_user_by_username(username=username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
