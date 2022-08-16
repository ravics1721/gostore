from uuid import UUID, uuid4
from fastapi import FastAPI, Depends
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from passlib.hash import pbkdf2_sha256
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models
import db
import schemas

models.Base.metadata.create_all(db.engine)

app = FastAPI()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=10
)
origins = [
    "http://localhost:*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"Hello": "World"}


def get_db():
    sql_db = db.SessionLocal()
    try:
        yield sql_db
    finally:
        sql_db.close()


@app.post("/user")
def add_user(body: schemas.UserModel, db: Session = Depends(get_db)):
    hash_pasword = pwd_context.encrypt(body.password)
    id: UUID = uuid4()
    new_user = models.User(id=id, name=body.name,
                           email=body.email, password=hash_pasword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
