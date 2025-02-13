from motor.motor_asyncio import AsyncIOMotorCollection
from models.user_models import User

from typing import Optional


class UserCRUD:
    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    async def get_user_by_username(self, username: str) -> Optional[User]:
        user_data = await self._collection.find_one({"username": username})
        return User(**user_data) if user_data else None

    async def get_user_by_email(self, email: str) -> Optional[User]:
        user_data = await self._collection.find_one({"email": email})
        return User(**user_data) if user_data else None

    async def create_user(self, user: User) -> str:
        user_data = user.dict(by_alias=True)
        result = await self._collection.insert_one(user_data)
        return str(result.inserted_id)
