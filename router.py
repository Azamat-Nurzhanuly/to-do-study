from typing import Annotated, List
from models.to_do_items import ToDoItemAdd, ToDoItem
from repository import ItemRepository
from fastapi import Depends
from fastapi import APIRouter


router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.get("")
def get_items() -> list[ToDoItem]:
    items = ItemRepository.find_all()
    return items

@router.post("")
def add_items(item: Annotated[ToDoItemAdd, Depends()]):
    item_id = ItemRepository.add_one(item)
    return {"ok": True, "item_id": item_id}
