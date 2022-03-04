from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from .routers import stores, items, users


app = FastAPI()

origins = [
    "http://localhost:*"
]


app.include_router(stores.router)
app.include_router(items.router)
app.include_router(users.router)

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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
