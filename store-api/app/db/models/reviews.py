from sqlalchemy import Boolean, Column, String, ForeignKey, ARRAY, Integer
from sqlalchemy.orm import relationship
from ..database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(String, index=True)
    rating = Column(Integer, index=True)
    description = Column(String, index=True)
    user_id = Column(String, ForeignKey('user.id'))
    product_id = Column(String, ForeignKey('item.id'))
    user = relationship("User", back_populates="user")
