import os
import cv2


def get_human_parse(model_fname):
    img = cv2.resize(cv2.imread(f'../data/image/{model_fname.split(".")[0]}/{model_fname}'),
                     (192, 256))
    cv2.imwrite(f'../data/image/{model_fname.split(".")[0]}/resize_{model_fname}', img)
    terminnal_command = f'python inference.py ' \
                        f'--loadmodel inference.pth ' \
                        f'--img_path ../data/image/{model_fname.split(".")[0]}/resize_{model_fname} ' \
                        f'--output_path ../data/image-parse-v3 ' \
                        f'--output_name resize_{model_fname.split(".")[0]}'
    os.system(terminnal_command)
    img2 = cv2.resize(cv2.imread(f'../data/image-parse-v3/resize_{model_fname.split(".")[0]}.png'),
                      (768, 1024), interpolation=cv2.INTER_LANCZOS4)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'../data/image-parse-v3/{model_fname.split(".")[0]}.png', img2)
    os.remove(f'../data/image-parse-v3/resize_{model_fname.split(".")[0]}.png')
    os.remove(f'../data/image/{model_fname.split(".")[0]}/resize_{model_fname}')


if __name__ == '__main__':
    model_fname = "image_picker_4D0EBEDB-D6ED-4395-BC7E-41D540041548-10365-0000002AC1923233.jpg"
    get_human_parse(model_fname)
