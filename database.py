from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine
import random

engine = create_engine('postgresql+psycopg2://postgres:bugayevskiypython@localhost:5432/FastApiToDoItems')


class Model(DeclarativeBase):
    pass


class ItemOrm(Model):
    __tablename__ = "ToDoItems"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


def create_tables():
    with engine.begin() as conn:
        conn.run_sync(Model.metadata.create_all)


def delete_tables():
    with engine.begin() as conn:
        conn.run_sync(Model.metadata.drop_all)
