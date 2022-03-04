from typing import List, Optional
from pydantic import BaseModel
import uuid


class Store(BaseModel()):
    id: str = uuid.uuid4()
    title: str
    about: Optional(str)
