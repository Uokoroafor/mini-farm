from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo import ReturnDocument
from models.todo_models import ListSummary, ToDoList

from typing import Union, Optional
from uuid import uuid4


class ListCRUD:
    def __init__(self, list_collection: AsyncIOMotorCollection):
        self._list_collection = list_collection

    async def show_all_lists(self, session=None):
        async for doc in self._list_collection.find(
            {},
            projection={
                "name": 1,
                "item_count": {"$size": "$items"},
            },
            sort={"name": 1},
            session=session,
        ):
            yield ListSummary.from_doc(doc)

    async def create_todo_list(self, name: str, session=None) -> str:
        response = await self._list_collection.insert_one(
            {"name": name, "items": []}, session=session
        )
        return str(response.inserted_id)

    async def delete_todo_list(self, id_: Union[str, ObjectId], session=None) -> bool:
        response = await self._list_collection.delete_one(
            {"_id": ObjectId(id_)}, session=session
        )
        return response.deleted_count == 1

    async def get_todo_list(self, id_: Union[str, ObjectId], session=None) -> bool:
        doc = await self._list_collection.find_one(
            {"_id": ObjectId(id_)}, session=session
        )
        return ToDoList.from_doc(doc)

    async def create_item(
        self, id_: Union[str, ObjectId], label: str, session=None
    ) -> Optional[ToDoList]:
        result = await self._list_collection.find_one_and_update(
            {"_id": ObjectId(id_)},
            {
                "$push": {
                    "items": {
                        "id": uuid4().hex,
                        "label": label,
                        "checked": False,
                    }
                }
            },
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return ToDoList.from_doc(result)
        else:
            return

    async def update_checked_state(
        self,
        doc_id: Union[str, ObjectId],
        item_id: str,
        checked_state: bool,
        session=None,
    ) -> Optional[ToDoList]:
        result = await self._list_collection.find_one_and_update(
            {"_id": ObjectId(doc_id), "items.id": item_id},
            {"$set": {"items.$.checked": checked_state}},
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return ToDoList.from_doc(result)
        else:
            return

    async def delete_item(
        self, doc_id: Union[str, ObjectId], item_id: str, session=None
    ) -> Optional[ToDoList]:
        result = await self._list_collection.find_one_and_update(
            {"_id": ObjectId(doc_id)},
            {
                "$pull": {
                    "items": {
                        "id": item_id,
                    }
                }
            },
            session=session,
            return_document=ReturnDocument.AFTER,
        )
        if result:
            return ToDoList.from_doc(result)
        else:
            return
