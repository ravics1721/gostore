from sqlalchemy import Boolean, Column, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from ..database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, required=True)
    pictures = Column(ARRAY(String))
    about = Column(String)
    owner_id = Column(String, ForeignKey('user.id'))
    category_ids = Column(ARRAY(String))
    product_ids = Column(ARRAY(String))
    categories = relationship("Category", back_populates="categories")
    owner = relationship("User", back_populates="owner")
    products = relationship("Item", back_populates="products")
