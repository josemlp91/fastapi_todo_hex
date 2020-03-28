from typing import List
from fastapi import Response
from fastapi.routing import APIRouter

from todolist.domains.todo.entities.todo_item import (
    CreateTodoItemDto,
    TodoItem,
    UpdateTodoItemDto,
)
from todolist.domains.todo.services import todo_item_service
from todolist.infraestructure.database.repositories.todo.fake import FakeRepo

fake_repo = FakeRepo()


# Router
router = APIRouter()


# Handlers
@router.post(
    "",
    response_model=TodoItem,
    status_code=201,
    responses={201: {"description": "Item created"}},
)
async def create_one(dto: CreateTodoItemDto):
    return await todo_item_service.create_one(fake_repo.create, dto)


@router.delete(
    "/{item_id}",
    status_code=204,
    responses={
        204: {"description": "Item deleted"},
        404: {"description": "Item not found"},
    },
)
async def delete_one(item_id: int):
    result = await todo_item_service.delete_one(fake_repo.delete, item_id)
    if not result:
        return Response(status_code=404)
    return Response(status_code=204)


@router.get(
    "",
    response_model=List[TodoItem],
    status_code=200,
    responses={200: {"description": "Items found"}},
)
async def get_all():
    return list(await todo_item_service.get_all(fake_repo.get_all))


@router.get(
    "/{item_id}",
    response_model=TodoItem,
    status_code=200,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def get_one(item_id: int):
    item = await todo_item_service.get_one(fake_repo.get_one, item_id)
    if not item:
        return Response(status_code=404)
    return item


@router.put(
    "/{item_id}",
    response_model=TodoItem,
    status_code=200,
    responses={
        200: {"description": "Item replaced"},
        404: {"description": "Item not found"},
    },
)
async def replace_one(dto: CreateTodoItemDto, item_id: int):
    item = await todo_item_service.update_one(fake_repo.replace, dto, item_id)
    return item if item else Response(status_code=404)


@router.patch(
    "/{item_id}",
    response_model=TodoItem,
    status_code=200,
    responses={
        200: {"description": "Item updated"},
        404: {"description": "Item not found"},
    },
)
async def update_one(dto: UpdateTodoItemDto, item_id: int):
    item = await todo_item_service.update_one(fake_repo.update, dto, item_id)
    return item if item else Response(status_code=404)
