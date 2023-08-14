import os
import shutil
import tqdm

# 입력 폴더를 지정합니다.
input_folder = r'C:\Users\Smart\Desktop\datas\emergency_vehicle\police'

# 출력 폴더를 지정합니다.
output_folder = r'C:\Users\Smart\Desktop\datas\emergency_vehicle\police'


# 입력 폴더를 순회합니다.
for root, directories, files in tqdm.tqdm(os.walk(input_folder)):
    # 하위 폴더에 있는 jpg 파일과 json 파일을 찾습니다.
    for file in files:
        if file.endswith('.jpg'):
            # jpg 파일을 아웃풋 폴더의 이미지 폴더로 이동합니다.
            shutil.move(os.path.join(root, file), os.path.join(output_folder, 'img'))
        elif file.endswith('.json'):
            # json 파일을 아웃풋 폴더의 라벨링 폴더로 이동합니다.
            shutil.move(os.path.join(root, file), os.path.join(output_folder, 'labeling_data'))
