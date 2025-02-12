from contextlib import asynccontextmanager
from config import settings
from fastapi import FastAPI
from database import database

from crud.todo_crud import ListCRUD
from crud.user_crud import UserCRUD


@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.connect()

    # Test database availability
    await database.test_db_connection()

    todo_lists=database.db.get_collection(settings.COLLECTION_NAME)
    users=database.db.get_collection(settings.USER_COLLECTION_NAME)
    
    app.state.db=database
    app.state.todo_CRUD=ListCRUD(todo_lists)
    app.state.user_CRUD=UserCRUD(users)

    yield

    database.disconnect()