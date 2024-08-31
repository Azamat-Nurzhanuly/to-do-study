import random

from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from database import ItemOrm, engine
from models.to_do_items import ToDoItemAdd, ToDoItem


class ItemRepository:
    @classmethod
    def add_one(cls, data: ToDoItemAdd) -> int:
        Session = sessionmaker(bind=engine)
        session = Session()
        item_dict = data.model_dump()
        item_dict['id'] = random.randint(1, 1000)

        item = ItemOrm(**item_dict)
        session.add(item)
        session.flush()
        session.commit()
        return item.id

    @classmethod
    def find_all(cls) -> list[ToDoItem]:
        connection = engine.connect()
        my_query = text('SELECT * FROM public."ToDoItems"')
        item_models = connection.execute(my_query).fetchall()
        item_schemas = [ToDoItem(name=item_model.name, description=item_model.description, id=item_model.id) for item_model in item_models]
        return item_schemas
