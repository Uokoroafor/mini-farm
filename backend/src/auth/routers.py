from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from auth.utils import authenticate_user
from auth.security import create_access_token, hash_password
from auth.schemas import TokenResponse
from crud.user_crud import UserCRUD
from models.user_models import User


router = APIRouter(prefix="/auth")


@router.post("/login", response_model=TokenResponse)
async def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    # Retrieve the UserCRUD instance from the app's state
    user_crud: UserCRUD = request.app.state.user_CRUD

    # Authenticate user using user_crud
    user = await authenticate_user(form_data.username, form_data.password, user_crud)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    # Generate JWT token
    access_token = create_access_token(data={"sub": user.username})
    return TokenResponse(access_token=access_token, token_type="bearer")


@router.post("/register", response_model=User)
async def register_user(request: Request, user: User):
    # Retrieve the UserCRUD instance from the app's state
    user_crud: UserCRUD = request.app.state.user_CRUD

    existing_user = await user_crud.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user.hashed_password = hash_password(user.hashed_password)
    user_id = await user_crud.create_user(user)
    user.id = user_id  # Assign MongoDB's ObjectId
    return user
