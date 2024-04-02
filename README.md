# Detecing-Hate-Expression
Now one of important social isuses in korea is hate expression about a specific sites.

Then this project was generated custom model for dtecting hand gestures of hate expression using YOLO-v8.

YOLO is a state-of-the-art, real-time object detection algorithm. 

We used the Google Colab Network to generate models at high speed, because Google Colab Network can use GPU

Using this custom model can detect hate expression and shows result of drawing a bounding box.

* Data labeling tool : [labelimg-master](https://github.com/liyunfei0411/labelimg-master)

## Programming procedure

We created a dataset to train the model using yolo.

The images were collected by image crawling, and to discriminate them with the val train test, the images were saved in yolo format in txt format by specifying the bounding box for each class using makesense.

The dataset consists of train data, valid data, test data.

Valid data consists of 10% of the total data randomly, while the train data consists of the remaining 90%.

The test data consists of 10% of the train data at random.

Train it with yolo and infer the learned result.

Find the "hateful hand expression" by inference and output it to OpenCV.

Translated with DeepL.com (free version)

## Demo
![test](https://github.com/gks7345/Detecting-Hate-Expression/assets/140896655/6b025a6e-fc8f-4a58-b394-d32362d5a04b)
