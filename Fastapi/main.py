import base64
import os

from PIL import Image
from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse
from typing import Optional, Dict, Any

from agnostics.get_img_agnostic import getting_img_agnostic
from agnostics.get_parse_agnostic import get_parse_agnostic
from cloth_mask import get_cloth_mask
from densepose.get_densepose import get_densepose
from humanparse.get_human_parse import get_human_parse
from openpose.get_openpose import get_openpose
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://127.0.0.1:3000"]
app = FastAPI()

# uvicorn main:app --reload
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/cloth")
async def cloth(image: UploadFile = File(...)):
    UPLOAD_FOLDER = "data/test/cloth"
    print(image.filename) #이미지 이름
    file_location = os.path.join(UPLOAD_FOLDER, image.filename)

    # 받은 이미지를 user_image 폴더에 저장
    with open(file_location, "wb") as buffer:
        buffer.write(await image.read())

    print(file_location) #파일 전체 경로 data/test/cloth\t1.jpg

    get_cloth_mask(image.filename)

    with open(f"data/test/cloth-mask/{image.filename}", "rb") as img_file:
        print(image.filename) # 출력결과: 'result_gan_vid/face_6.jpg' 이렇게 나오면 안되고 face_6.jpg 만 나와야함
        image_bytes = img_file.read()

    a = base64.b64encode(image_bytes).decode()
    # 바이트 스트림을 base64 인코딩하여 반환
    return {"data": a}


@app.post("/densepose")
async def densepose(image: UploadFile = File(...)):
    UPLOAD_FOLDER = "data/test/image"
    print(image.filename)  # 이미지 이름
    file_location = os.path.join(UPLOAD_FOLDER, image.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(await image.read())

    print(f'######## model_fname for densepose: {image.filename}')
    os.chdir("./densepose")
    get_densepose(image.filename)
    os.chdir("../")

    with open(f"data/test/image-densepose/{image.filename}", "rb") as img_file:
        print(image.filename)  # 출력결과: 'result_gan_vid/face_6.jpg' 이렇게 나오면 안되고 face_6.jpg 만 나와야함
        image_bytes = img_file.read()

    a = base64.b64encode(image_bytes).decode()
    return {"data": a}


@app.post("/cloth-mask", status_code=200)
async def cloth_mask(request_body: Optional[Dict[str, Any]] = None):
    cloth_fname = request_body.get('cloth_fname')
    get_cloth_mask(cloth_fname)
    return JSONResponse(status_code=200,
                        content={"msg": "cloth mask done"})


@app.post("/openpose", status_code=200)
async def openpose(request_body: Optional[Dict[str, Any]] = None):
    model_fname = request_body.get('model_fname')
    os.chdir("./openpose")
    get_openpose(model_fname)
    os.chdir("../")
    return JSONResponse(status_code=200,
                        content={"msg": "openpose done"})


@app.post("/densepose", status_code=200)
async def densepose(request_body: Optional[Dict[str, Any]] = None):
    model_fname = request_body.get('model_fname')
    print(f'######## model_fname for densepose: {model_fname}')
    os.chdir("./densepose")
    get_densepose(model_fname)
    os.chdir("../")
    return JSONResponse(status_code=200,
                        content={"msg": "densepose done"})


@app.post("/human-parse", status_code=200)
async def human_parse(request_body: Optional[Dict[str, Any]] = None):
    model_fname = request_body.get('model_fname')
    print(f'######## model_fname for human-parse: {model_fname}')
    os.chdir("./humanparse")
    get_human_parse(model_fname)
    os.chdir("../")
    return JSONResponse(status_code=200,
                        content={"msg": "human-parse done"})


@app.post("/agnostics", status_code=200)
async def agnostics(request_body: Optional[Dict[str, Any]] = None):
    model_fname = request_body.get('model_fname')
    print(f'######## model_fname for agnostics: {model_fname}')
    os.chdir("./agnostics")
    getting_img_agnostic(model_fname)
    get_parse_agnostic(model_fname)
    os.chdir("../")
    return JSONResponse(status_code=200,
                        content={"msg": "agnostics done"})


@app.get("/viton", status_code=200)
async def viton_image():
    viton_fname = "00018_00.jpg"
    viton_path = f"./output/{viton_fname}"
    with open(viton_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    return JSONResponse(status_code=200, content={"image": encoded_string, "fname": viton_fname})


