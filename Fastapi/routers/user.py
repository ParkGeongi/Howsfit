from fastapi import APIRouter, Depends, WebSocket
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse, RedirectResponse

#from app.crud.user import UserCrud
from app.schemas.user import UserDTO
from app.utils.database import get_db

router = APIRouter()
'''@router.post("/register",status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=dict(
        msg=UserCrud(db).add_user(request_user=dto)))

@router.post("/login", status_code=200)
async def login_user(dto:UserDTO ,db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).login_user(request_user =dto)))


@router.post("/logout", status_code=200)
async def logout_user(dto:UserDTO ,db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(msg=UserCrud(db).logout_user(request_user =dto)))

@router.get("/load")
async def load_user(dto: UserDTO, db: Session = Depends(get_db)):
    if UserCrud(db).match_token(request_user=dto):
        return JSONResponse(status_code=200,
                            content=jsonable_encoder(
                                UserCrud(db).find_user_by_token(request_user=dto)))
    else:
        RedirectResponse(url='/no-match-token', status_code=302)'''
