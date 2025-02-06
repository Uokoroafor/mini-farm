from fastapi import Request
from crud.todo_crud import ListCRUD


def get_todo_crud(request: Request) -> ListCRUD:
    return request.app.state.todo_CRUD
