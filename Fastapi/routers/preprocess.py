import os
import subprocess
import sys

import cv2
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.services.preprocess.packages.cloth_mask import get_cloth_mask
from app.utils.database import get_db
from resize import resize_img

router = APIRouter()
@router.get("/cloth-mask")
async def cloth_mask(db: Session = Depends(get_db)):
    # 성공
    # 1. cloth mask
    print('1. cloth mask')
    cloth_img= 'app/services/data/test/cloth/t1.jpg'
    save_path= 'app/services/data/test/cloth-mask/t1.jpg'
    get_cloth_mask(cloth_img,save_path)
    return {"msg": "success"}

@router.get("/densepose")
async def dense_pose(db: Session = Depends(get_db)):
    # 성공
    print('2. dense-pose')
    terminnal_command = "python app/services/preprocess/packages/DensePose/apply_net.py show app/services/preprocess/packages/DensePose/configs/densepose_rcnn_R_50_FPN_s1x.yaml app/utils/weights/model_final_162be9.pkl " \
                        r"app/services/data/test/image dp_segm -v --opts MODEL.DEVICE cpu"
    os.system(terminnal_command)
    return {"msg": "success"}

@router.get("/parse")
async def parse(db: Session = Depends(get_db)):
    print('3. Human-parse')
    resize_img('app/services/data/test/image/t1.jpg','app/services/data/test/image-parse-v3/t1.jpg',300,400,False)
    path = 'app/services/preprocess/packages/Graphonomy-master'
    terminnal_command = f'python {path}/inference.py --loadmodel {path}/inference.pth --img_path app/services/data/test/image/t1.jpg --output_path app/services/data/test/image-parse-v3 --output_name 00296'
    os.system(terminnal_command)
    resize_img('app/services/data/test/image-parse-v3/test_1_.png', 'app/services/data/test/image-parse-v3/test_1_.png', 768, 1028,True)
    return {"msg": "success"}

@router.get("/agnostic")
async def agnostic(db: Session = Depends(get_db)):
    terminnal_command = 'python app/services/preprocess/agnostic.py'
    os.system(terminnal_command)
    return {"msg": "success"}

@router.get("/parse-agnostic")
async def parse_agnostic(db: Session = Depends(get_db)):


    terminnal_command = 'python app/services/preprocess/image-parse-agnostic.py'
    os.system(terminnal_command)


    return {"msg": "success"}

@router.get("/try-on")
async def try_on(db: Session = Depends(get_db)):
    terminnal_command = "python app/services/try_on/my_test_generator.py --test_name viton_in_light_sail --tocg_checkpoint app/services/try_on/eval_models/weights/v0.1/tocg_final.pth --gpu_ids 0 --gen_checkpoint app/services/try_on/eval_models/weights/v0.1/gen_model_final.pth --datasetting unpaired --data_list test_pairs.txt --dataroot app/services/data"
    os.system(terminnal_command)
    print('1. tryon')
    return {"msg": "success"}


@router.get("/img/{img_name}")
async def read_file(img_name: str):
    # cloth-mask path : app/services/data/test/cloth-mask/test_2.jpg
    file_path1 = f'app/services/data/test/cloth-mask/{img_name}'
    file_path = f'app/output/{img_name}'

    return FileResponse(file_path1)

