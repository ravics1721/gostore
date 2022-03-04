from typing import List, Optional
from pydantic import BaseModel
import uuid
from .items import Item
from .stores import Store


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserCreate):
    id: str = uuid.uuid4()
    isSeller: bool = False
    hasStores: bool = False
    items: Optional(List(Item)) = []
    stores: Optional(List(Store)) = []
