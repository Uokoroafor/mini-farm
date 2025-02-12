from pydantic import BaseModel
from typing import List


class ListSummary(BaseModel):
    id: str
    name: str
    item_count: int

    @classmethod
    def from_doc(cls, doc) -> "ListSummary":
        return cls(
            id=str(doc["_id"]),
            name=doc["name"],
            item_count=doc["item_count"],
        )


class ListItem(BaseModel):
    id: str
    label: str
    checked: bool

    @classmethod
    def from_doc(cls, item) -> "ListItem":
        return cls(
            id=item["id"],
            label=item["label"],
            checked=item["checked"],
        )


class ToDoList(BaseModel):
    id: str
    name: str
    items: List[ListItem]

    @classmethod
    def from_doc(cls, doc) -> "ToDoList":
        return cls(
            id=str(doc["_id"]),
            name=doc["name"],
            items=[ListItem.from_doc(item) for item in doc["items"]],
        )
