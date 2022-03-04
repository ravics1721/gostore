from sqlalchemy import Column, String
from ..database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(String, index=True)
    title = Column(String, index=True)
