# This is a Object Detection Project I did at (Algoryc) for my practice.

- This project entails helmet detection in images.
- For this purpose, the model has been trained on a custom dataset and YoloV8.

## Dataset

The dataset has not been included in the repo as it is very large. 

The dataset can be easily downloaded from.

```
"https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/data"
```
## Preprocessing
As this dataset is in the Pascal VOC format it cannot be used directly with YoloV8 so the format must be converted (into the YoloV8 one).
The primary difference between the two is the bounded box, so the bounded box of Pascal VOC must be converted, 
```
(xmin, xmax, ymin, ymax) => after conversion (x, y, h, w)
```
Roboflow is a resource that can be used to convert the format.

After this, the dataset can be split into 3 parts (Train 70%, Validation 20%, Test 10%)

## Training
The training of the model can be done rather swiftly the code is provided in the Notebooks/helmet-detection-training.ipynb.

## Inference
The inference can be taken from the same file Notebooks/helmet-detection-training.ipynb.

## To test the model
To test the model on the test dataset add this line at the end of the notebook.
```
!yolo task=detect mode=val split=test model=/content/runs/detect/train/weights/best.pt data=/content/drive/MyDrive/helmet_dataset_2/helmet-dataset.v1i.yolov8/data.yaml
```

## Tracking
Object live tracking can also be done for that see the code inside the Tracking folder.

### Path Tracking
The path of the target object can also be tracked for this purpose YoloV8 has inbuilt functionality. See Tracking/tracking-overtime.py

### Tracking algorithms
There are 2 primary algorithms, I have implemented both,
- Bytetrack (9-11 FPS)
- BoTSort (12-13 FPS)

### FPS Performance
The FPS performance depends on many factors, the algorithm and hardware are of prime importance. I ran both algorithms on my M2 Silicon Macbook Pro (Performance will vary according to system).
#### BotSort
<img width="428" alt="Screenshot 2024-02-12 at 4 08 26 PM" src="https://github.com/saada865/helmet-detection-yoloV8/assets/80025562/b341b41a-cd76-4033-8e80-165639da1893">

#### Bytetrack
<img width="430" alt="Screenshot 2024-02-12 at 4 10 24 PM" src="https://github.com/saada865/helmet-detection-yoloV8/assets/80025562/f1adc4be-0064-4cd5-953b-f313aebda0f9">


