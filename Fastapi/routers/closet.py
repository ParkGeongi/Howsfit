from fastapi import APIRouter, Depends
from app.schemas.closet import ClosetDTO

from app.utils.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()
@router.post("/register",status_code=201)
async def register_user(dto: ClosetDTO, db: Session = Depends(get_db)):
    return {"message": f"Hello "}