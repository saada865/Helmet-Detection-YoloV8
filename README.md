# This is a practice project I did at (Algoryc).

- This project entails helmet detection in images.
- For this purpose, the model has been trained on a custom dataset and YoloV8.

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

Sample code
``` 
images_path = sorted([i for i in Path(root_images_path).glob("*.png")])
```
