from fastapi import APIRouter


router = APIRouter()


@router.get('/users', tags=['users'])
def users():
    return {"users": "it is users routes"}
