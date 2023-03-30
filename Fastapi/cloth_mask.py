import os
import time

import numpy as np
from PIL import Image, ImageOps
from carvekit.web.schemas.config import MLConfig
from carvekit.web.utils.init_utils import init_interface


def get_cloth_mask(cloth_fname):
    start = time.time()
    cloth_path = f"./data/test/cloth/{cloth_fname}"

    SHOW_FULLSIZE = False
    PREPROCESSING_METHOD = "none"
    SEGMENTATION_NETWORK = "tracer_b7"
    POSTPROCESSING_METHOD = "fba"
    SEGMENTATION_MASK_SIZE = 640
    TRIMAP_DILATION = 30
    TRIMAP_EROSION = 5
    DEVICE = 'cpu'

    config = MLConfig(segmentation_network=SEGMENTATION_NETWORK,
                      preprocessing_method=PREPROCESSING_METHOD,
                      postprocessing_method=POSTPROCESSING_METHOD,
                      seg_mask_size=SEGMENTATION_MASK_SIZE,
                      trimap_dilation=TRIMAP_DILATION,
                      trimap_erosion=TRIMAP_EROSION,
                      device=DEVICE)

    interface = init_interface(config)

    imgs = []
    imgs.append(cloth_path)
    img = np.array(interface(imgs)[0])[..., :3]
    idx = (img[..., 0] == 130) & (img[..., 1] == 130) & (img[..., 2] == 130)
    img = np.ones(idx.shape) * 255
    img[idx] = 0
    image = Image.fromarray(np.uint8(img), 'L')
    image.save(f'./data/test/cloth-mask/{cloth_fname}')
    print(f"cloth mask 소요시간 : {round((time.time() - start), 2)}")
    print('finish')

