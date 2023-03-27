import json
from os import path as osp
import os

import numpy as np
from PIL import Image, ImageDraw

import argparse

from tqdm import tqdm


def get_im_parse_agnostic(im_parse, pose_data, w=768, h=1024):
    label_array = np.array(im_parse)
    parse_upper = ((label_array == 5).astype(np.float32) +
                   (label_array == 6).astype(np.float32) +
                   (label_array == 7).astype(np.float32))
    parse_neck = (label_array == 10).astype(np.float32)

    r = 10
    agnostic = im_parse.copy()

    # mask arms
    for parse_id, pose_ids in [(14, [2, 5, 6, 7]), (15, [5, 2, 3, 4])]:
        mask_arm = Image.new('L', (w, h), 'black')
        mask_arm_draw = ImageDraw.Draw(mask_arm)
        i_prev = pose_ids[0]
        for i in pose_ids[1:]:
            if (pose_data[i_prev, 0] == 0.0 and pose_data[i_prev, 1] == 0.0) or (
                    pose_data[i, 0] == 0.0 and pose_data[i, 1] == 0.0):
                continue
            mask_arm_draw.line([tuple(pose_data[j]) for j in [i_prev, i]], 'white', width=r * 10)
            pointx, pointy = pose_data[i]
            radius = r * 4 if i == pose_ids[-1] else r * 15
            mask_arm_draw.ellipse((pointx - radius, pointy - radius, pointx + radius, pointy + radius), 'white',
                                  'white')
            i_prev = i
        parse_arm = (np.array(mask_arm) / 255) * (label_array == parse_id).astype(np.float32)
        agnostic.paste(0, None, Image.fromarray(np.uint8(parse_arm * 255), 'L'))

    # mask torso & neck
    agnostic.paste(0, None, Image.fromarray(np.uint8(parse_upper * 255), 'L'))
    agnostic.paste(0, None, Image.fromarray(np.uint8(parse_neck * 255), 'L'))

    return agnostic


def get_parse_agnostic(model_fname):
    data_path = "../data"
    output_path = "../data/image-parse-agnostic-v3.2"
    print(model_fname)
    model_dir = model_fname.split('.')[0]
    print(model_dir)

    os.makedirs(output_path, exist_ok=True)

    for im_name in tqdm(os.listdir(osp.join(data_path, 'image', model_dir))):
        print(im_name)

        # load pose image
        pose_name = im_name.replace('.jpg', '_keypoints.json')

        try:
            with open(osp.join(data_path, 'openpose_json', pose_name), 'r') as f:
                pose_label = json.load(f)
                pose_data = pose_label['people'][0]['pose_keypoints_2d']
                pose_data = np.array(pose_data)
                pose_data = pose_data.reshape((-1, 3))[:, :2]
        except IndexError:
            print(pose_name)
            continue

        # load parsing image
        parse_name = im_name.replace('.jpg', '.png')
        im_parse = Image.open(osp.join(data_path, 'image-parse-v3', parse_name))

        agnostic = get_im_parse_agnostic(im_parse, pose_data)

        agnostic.save(osp.join(output_path, parse_name))


if __name__ == "__main__":
    model_fname = "image_picker_146BB643-3A02-405D-A6F3-3E15290E8367-2528-00000004CC3BCA19.jpg"
    get_parse_agnostic(model_fname)
