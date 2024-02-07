import numpy as np
import os
import shutil
from pathlib import Path
#
root_annotations_path = Path("/Users/saadahmadmalik/Documents/Coding/WORK/archive (1)/annotations")
root_images_path = Path("/Users/saadahmadmalik/Documents/Coding/WORK/archive (1)/images")

annotations_path = sorted([i for i in Path(root_annotations_path).glob("*.xml")])
images_path = sorted([i for i in Path(root_images_path).glob("*.png")])

n_imgs = len(images_path)

classes = np.array(['helmet', 'head', 'person'])

with open(annotations_path[500], 'r') as f:
    print(f.read())

os.makedirs('../data/train/images', exist_ok=True)
os.makedirs('../data/train/annotations', exist_ok=True)

os.makedirs('../data/validation/images', exist_ok=True)
os.makedirs('../data/validation/annotations', exist_ok=True)

os.makedirs('../data/test/images', exist_ok=True)
os.makedirs('../data/test/annotations', exist_ok=True)

# This is the num of test images which is the first we mention
n_split = n_imgs // 10

for i, (annot_path, img_path) in enumerate(zip(annotations_path, images_path)):
    if i > n_imgs:
        break
    if i < n_split:
        shutil.copy(img_path, 'data/test/images/' + img_path.parts[-1])
        shutil.copy(annot_path, 'data/test/annotations/' + annot_path.parts[-1])
    elif n_split <= i < n_split * 3:
        shutil.copy(img_path, 'data/validation/images/' + img_path.parts[-1])
        shutil.copy(annot_path, 'data/validation/annotations/' + annot_path.parts[-1])
    else:
        shutil.copy(img_path, 'data/train/images/' + img_path.parts[-1])
        shutil.copy(annot_path, 'data/train/annotations/' + annot_path.parts[-1])

print(len(list(Path('../data/train/annotations/').glob('*.xml'))))
print(len(list(Path('../data/validation/annotations/').glob('*.xml'))))
print(len(list(Path('../data/test/annotations/').glob('*.xml'))))


def convert_annot(size, box):
    x1 = int(box[0])
    y1 = int(box[1])
    x2 = int(box[2])
    y2 = int(box[3])

    dw = np.float32(1. / int(size[0]))
    dh = np.float32(1. / int(size[1]))

    w = x2 - x1
    h = y2 - y1
    x = x1 + (w / 2)
    y = y1 + (h / 2)

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return [x, y, w, h]


def save_txt_file(img_jpg_file_name, size, img_box):
    save_file_name = '/Dataset/labels/' + img_jpg_file_name + '.txt'

    # file_path = open(save_file_name, "a+")
    with open(save_file_name, 'a+') as file_path:
        for box in img_box:
            cls_num = classes.index(box[0])

            new_box = convert_annot(size, box[1:])

            file_path.write(f"{cls_num} {new_box[0]} {new_box[1]} {new_box[2]} {new_box[3]}\n")

        file_path.flush()
        file_path.close()


def get_xml_data(file_path, img_xml_file):
    img_path = file_path + '/' + img_xml_file + '.xml'
    # print(img_path)

    dom = parse(img_path)
    root = dom.documentElement
    img_name = root.getElementsByTagName("filename")[0].childNodes[0].data
    img_size = root.getElementsByTagName("size")[0]
    objects = root.getElementsByTagName("object")
    img_w = img_size.getElementsByTagName("width")[0].childNodes[0].data
    img_h = img_size.getElementsByTagName("height")[0].childNodes[0].data
    img_c = img_size.getElementsByTagName("depth")[0].childNodes[0].data

    img_box = []
    for box in objects:
        cls_name = box.getElementsByTagName("name")[0].childNodes[0].data
        x1 = int(box.getElementsByTagName("xmin")[0].childNodes[0].data)
        y1 = int(box.getElementsByTagName("ymin")[0].childNodes[0].data)
        x2 = int(box.getElementsByTagName("xmax")[0].childNodes[0].data)
        y2 = int(box.getElementsByTagName("ymax")[0].childNodes[0].data)

        img_jpg_file_name = img_xml_file + '.jpg'
        img_box.append([cls_name, x1, y1, x2, y2])

    # test_dataset_box_feature(img_jpg_file_name, img_box)
    save_txt_file(img_xml_file, [img_w, img_h], img_box)


files = os.listdir('/hard-hat-detection/annotations')
for file in files:
    file_xml = file.split(".")
    get_xml_data('/hard-hat-detection/annotations', file_xml[0])
