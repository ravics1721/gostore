from uuid import UUID, uuid4
from sqlalchemy import Column, String
from fastapi_restful.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(GUID, primary_key=True, index=True,
                server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
