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

app = FastAPI()
# uvicorn main:app --reload


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/upload", status_code=200)
async def upload_image(model: UploadFile = File(...), cloth: UploadFile = File(...)):
    model_path = f"./data/image/{model.filename.split('.')[0]}"
    os.makedirs(model_path, exist_ok=True)
    model_fname = f"{model_path}/{model.filename}"
    with open(model_fname, "wb") as buffer:
        buffer.write(await model.read())
    model_image = Image.open(model_fname)
    # model_image.show()

    cloth_fname = f"./data/cloth/{cloth.filename}"
    with open(cloth_fname, "wb") as buffer:
        buffer.write(await cloth.read())
    cloth_image = Image.open(cloth_fname)
    # cloth_image.show()
    """
    cloth_data = await cloth.read()
    cloth_image = Image.open(BytesIO(cloth_data))
    cloth_image.show()
    """
    return JSONResponse(status_code=200,
                        content={"msg": "send to fastapi done"})


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


