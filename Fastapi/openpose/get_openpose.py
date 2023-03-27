import os
import shutil

"""
def create_dir(model_fname):
    model_path = f"../data/image/{model_fname.split('.')[0]}"
    os.makedirs(model_path, exist_ok=True)
    if os.path.isfile(model_path):
        dir_name = os.path.splitext(os.path.basename(model_path))[0]
        src_dir = os.path.dirname(model_path)
        new_dir = os.path.join(src_dir, dir_name)
        os.makedirs(new_dir, exist_ok=True)
        dst_path = os.path.join(new_dir, os.path.basename(model_path))
        shutil.copy(model_path, dst_path)
"""

def get_openpose(model_fname):
    model_dir = model_fname.split('.')[0]
    terminal_command = f"build/examples/openpose/openpose.bin " \
                       f"--image_dir ../data/image/{model_dir} " \
                       "--write_json ../data/openpose_json " \
                       "--write_images ../data/openpose_img"
    os.system(terminal_command)


if __name__ == '__main__':
    model_fname = "image_picker_4D0EBEDB-D6ED-4395-BC7E-41D540041548-10365-0000002AC1923233.jpg"
    get_openpose(model_fname)
