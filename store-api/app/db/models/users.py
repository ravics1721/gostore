from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    hasStore = Column(Boolean, index=True)
    isSeller = Column(Boolean, index=True)
    items = relationship("Item", back_populates="owner")
    stores = relationship("Store", back_populates="store")
