from fastapi import APIRouter

router = APIRouter()


@router.get("/stores", tags=["stores"])
async def stores():
    return [{
        "store1": "Amazon",
        "message": 'All store comming soon'
    }]
