#tensorboard --logdir=./tensorboard
import os
import random

# 이미지 파일이 저장된 디렉토리 경로
img_dir = "./data/train/cloth"
# 생성할 텍스트 파일 경로
txt_file = "./data/train_paris_random.txt"
# 생성할 텍스트 파일 라인 수
num_lines = 3000

# 반복하여 텍스트 파일에 이미지 파일 이름 2개씩 저장
with open(txt_file, "w") as f:
    for i in range(num_lines):
        # 이미지 파일 이름 2개를 랜덤으로 선택
        img_names = random.sample(os.listdir(img_dir), 2)
        # 선택된 이미지 파일 이름을 텍스트 파일에 저장
        f.write("{} {}\n".format(img_names[0], img_names[1]))