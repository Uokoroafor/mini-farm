from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from crud.todo_crud import ListCRUD
from crud.user_crud import UserCRUD
from jose import jwt, JWTError
from config import settings


def get_todo_crud(request: Request) -> ListCRUD:
    return request.app.state.todo_CRUD


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    request: Request,
    token: str = Depends(oauth2_scheme),
):
    # Get the UserCRUD instance from the app's state
    user_crud: UserCRUD = request.app.state.user_CRUD
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await user_crud.get_user_by_username(username)
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid")
