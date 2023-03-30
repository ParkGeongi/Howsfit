from fastapi import APIRouter
from app.schemas.cloth import ClothDTO
import os

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.models.cloth import Cloth

from app.services.cloth_color.extract_cloth_color import ExtractColor
from app.utils.database import get_db


router = APIRouter()

@router.get("/add")
async def add_cloth(db: Session = Depends(get_db)):
    db.add(Cloth(cloth_id='1',cloth_img=f"{os.getcwd()}/app/test_data/img2.jpg"))
    db.commit()

    return {"msg": "success"}
@router.get("/get_cloth")
async def get_cloth(db: Session = Depends(get_db)):
    cloth = db.query(Cloth).filter(Cloth.cloth_id=='1').first()
    return {"cloth": cloth.cloth_img}
@router.get("/delete")
async def delete_cloth(db: Session = Depends(get_db)):
    db.query(Cloth).filter(Cloth.cloth_id=='1').delete()
    db.commit()
    return {"msg": "success"}

@router.get("/color")
async def cloth(db: Session = Depends(get_db)):
    img_url = db.query(Cloth).filter(Cloth.cloth_id=='1').first().cloth_img
    print(img_url)
    #'/app/app/test_data/img2.jpg'
    result = ExtractColor().hook(img_url)
    return {"result": result}