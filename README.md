# This is a practice project I did at (Algoryc).

- This project entails helmet detection in images.
- For this purpose, the model has been trained on a custom dataset and YoloV8.

The dataset has not been included in the repo as it is very large. 

The dataset can be easily downloaded from.

```
"https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/data"
```
Sample code
``` 
images_path = sorted([i for i in Path(root_images_path).glob("*.png")])
```
