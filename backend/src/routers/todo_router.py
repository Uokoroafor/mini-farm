from fastapi import status, APIRouter, Depends
from typing import List

from crud.todo_crud import ListCRUD, ListSummary, ToDoList
from schemas.todo_schemas import (
    NewList,
    NewListResponse,
    ToDoItemUpdate,
    NewItem,
)
from dependencies import get_todo_crud

router = APIRouter(prefix="/api")


@router.get("/lists", response_model=List[ListSummary])
async def get_all_lists(
    todo_crud: ListCRUD = Depends(get_todo_crud),
) -> List[ListSummary]:
    return [i async for i in todo_crud.show_all_lists()]


@router.post(
    "/lists",
    status_code=status.HTTP_201_CREATED,
    response_model=NewListResponse,
)
async def create_todo_list(
    new_list: NewList, todo_crud: ListCRUD = Depends(get_todo_crud)
) -> NewListResponse:
    return NewListResponse(
        id=await todo_crud.create_todo_list(new_list.name), name=new_list.name
    )


@router.get("/lists/{list_id}", response_model=ToDoList)
async def get_list(
    list_id: str, todo_crud: ListCRUD = Depends(get_todo_crud)
) -> ToDoList:
    return await todo_crud.get_todo_list(list_id)


@router.delete("/lists/{list_id}", response_model=bool)
async def delete_list(
    list_id: str, todo_crud: ListCRUD = Depends(get_todo_crud)
) -> bool:
    return await todo_crud.delete_todo_list(list_id)


@router.post(
    "/lists/{list_id}/items",
    status_code=status.HTTP_201_CREATED,
    response_model=ToDoList,
)
async def create_item(
    list_id: str,
    new_item: NewItem,
    todo_crud: ListCRUD = Depends(get_todo_crud),
) -> ToDoList:
    return await todo_crud.create_item(list_id, new_item.label)


@router.delete(
    "/lists/{list_id}/items/{item_id}",
)
async def delete_item(
    list_id: str, item_id: str, todo_crud: ListCRUD = Depends(get_todo_crud)
) -> ToDoList:
    return await todo_crud.delete_item(list_id, item_id)


@router.patch("/lists/{list_id}/checked_state")
async def set_checked_state(
    list_id: str,
    update: ToDoItemUpdate,
    todo_crud: ListCRUD = Depends(get_todo_crud),
) -> ToDoList:
    return await todo_crud.update_checked_state(
        list_id, update.item_id, update.checked_state
    )
