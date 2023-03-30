import os

import cv2
import numpy as np
from PIL import Image
#배경제거..
'''ori_img = cv2.imread("./test/image/my_resize.jpg") # original img
mask_img = cv2.imread('./test/image/my_resize_gray.png', cv2.IMREAD_GRAYSCALE) # parse_img.png
mask_img = cv2.resize(mask_img, (768, 1024))
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask_img = cv2.erode(mask_img, k)
img_seg = cv2.bitwise_and(ori_img, ori_img, mask=mask_img)
back_ground = ori_img - img_seg
img_seg = np.where(img_seg == 0, 215, img_seg)'''
#cv2.imwrite("./1.png", img_seg)
#img = cv2.resize(img_seg, (768, 1024))
#cv2.imwrite('./test/image/test_2.jpg', img_seg)


#1. cloth mask
print('1. cloth mask')
os.chdir("../services/preprocess/packages")
os.system("python cloth_mask.py")

#2. dense pose
print('2. dense pose')
'''terminnal_command = "python ./DensePose/apply_net.py show ./DensePose/configs/densepose_rcnn_R_50_FPN_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl " \
                    r"C:\project\backend\app\custom\image dp_segm -v --opts MODEL.DEVICE cpu"
os.system(terminnal_command)'''
###3. openpose'''
print('3. openpose')

os.chdir("./openpose")
print(os.getcwd())
#terminnal_command = r'C:\project\backend\app\services\preprocess\packages\openpose/artifacts/bin/OpenPoseDemo.exe --image_dir ../../../../custom/image --write_json ../../../../custom/openpose_json --write_images ../../../../custom/openpose_img'
terminnal_command = r'C:\project\backend\app\services\preprocess\packages\openpose/artifacts/bin/OpenPoseDemo.exe --image_dir C:\project\backend\app\services/data/test/image --write_json C:\project\backend\app\services//data/test/openpose_json --write_images C:\project\backend\app\services//data/test/openpose_img'
os.system(terminnal_command)

###4. image parse
'''print('4. image parse')
os.chdir("../Graphonomy-master")
img = cv2.resize(cv2.imread("../../../data/test/image/my_resize.jpg"), (300, 400))
cv2.imwrite("../../../data/test/image/my_resize.jpg", img)
terminnal_command = "python ./inference.py --loadmodel ./inference.pth --img_path ../../../data/test/image/my_resize.jpg --output_path ../../../data/test/image-parse-v3 --output_name my_resize"
os.system(terminnal_command)

img = cv2.resize(cv2.imread("../../../data/test/image-parse-v3/my_resize_gray.png"), (768, 1024))
cv2.imwrite("../../../data/test/image-parse-v3/my_resize.png", img)

img = cv2.cvtColor(cv2.imread("../../../data/test/image-parse-v3/my_resize.png"), cv2.COLOR_BGR2GRAY)
cv2.imwrite("../../../data/test/image-parse-v3/my_resize.png", img)
'''
'''
os.chdir('../../../try_on')
print(os.getcwd())
terminnal_command = "python my_test_generator.py --test_name cpu_test2 --tocg_checkpoint ./eval_models/weights/v0.1/tocg_final.pth --gpu_ids 0 --gen_checkpoint ./eval_models/weights/v0.1/gen_model_final.pth --datasetting unpaired --data_list test_pairs.txt --dataroot ../data --output_dir ./output"
os.system(terminnal_command)'''
