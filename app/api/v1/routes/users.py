from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get('/')
def users():
    return {"users": "it is users routes"}
