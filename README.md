# This is a Computer Vision Project I did at (Algoryc) for my practice.

- This project entails helmet detection in images.
- For this purpose, the model has been trained on a custom dataset and YoloV8.

## Dataset

The dataset has not been included in the repo as it is very large. 

The dataset can be easily downloaded from.

```
"https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/data"
```
## Preprocessing
As this dataset is in the Pascal VOC format it cannot be used directly with YoloV8 so the format must be converted.
The bounded box of Pascal VOC is, 
```
(xmin, xmax, ymin, ymax) => after conversion (x, y, h, w)
```
## Training
The training of the model can be done rather swiftly the code is provided in the Notebooks/helmet-detection-training.ipynb.

## Inference
The inference can be taken from the same file Notebooks/helmet-detection-training.ipynb.

## To test the model
To test the model on the test dataset add this line at the end of the notebook.
```
!yolo task=detect mode=val split=test model=/content/runs/detect/train/weights/best.pt data=/content/drive/MyDrive/helmet_dataset_2/helmet-dataset.v1i.yolov8/data.yaml
```
