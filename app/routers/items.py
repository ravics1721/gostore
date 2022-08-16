from fastapi import APIRouter

router = APIRouter()


@router.get("/items", tags=["items"])
def items():
    return {"message": "items ...."}
