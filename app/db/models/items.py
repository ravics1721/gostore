from sqlalchemy import Column, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from ..database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    pictures = Column(ARRAY(String))
    owner_id = Column(String, ForeignKey('users.id'))
    category_id = Column(String, ForeignKey('category.id'))
    owner = relationship("Category", back_populates='items')
    category = relationship("Category", back_populates='items')
    reviews = relationship("Review", back_populates='reviews')
