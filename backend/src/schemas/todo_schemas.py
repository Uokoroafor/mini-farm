from pydantic import BaseModel


class NewList(BaseModel):
    name: str


class NewListResponse(BaseModel):
    id: str
    name: str


class NewItem(BaseModel):
    label: str


class NewItemResponse(BaseModel):
    id: str
    label: str


class ToDoItemUpdate(BaseModel):
    item_id: str
    checked_state: bool
