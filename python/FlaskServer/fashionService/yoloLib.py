import cv2
import numpy as np
import time


def initNet():
    CONFIG = 'fashionService/config/yolov4-tiny-myobj.cfg'
    WEIGHT = 'fashionService/config/yolov4-tiny-myobj_best.weights'
    NAMES = 'fashionService/config/obj.names'

    # 讀取物件名稱以及設定外框顏色
    with open(NAMES, 'r') as f:
        names = [line.strip() for line in f.readlines()]
        colors = np.random.uniform(0, 255, size=(len(names), 3))

    # 設定神經網路
    net = cv2.dnn.readNet(CONFIG, WEIGHT)

    # opencv 自行編譯話才會有cuda
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1 / 255.0)
    # YOLO 要對調顏色
    model.setInputSwapRB(True)

    return model, names, colors


def nnProcess(image, model):
    classes, confs, boxes = model.detect(image, 0.6, 0.3)
    return classes, confs, boxes


def drawBox(image, classes, confs, boxes, names, colors):
    new_image = image.copy()
    for (classid, conf, box) in zip(classes, confs, boxes):
        x, y, w, h = box
        label = '{}: {:.2f}'.format(names[int(classid)], float(conf))
        color = colors[int(classid)]
        cv2.rectangle(new_image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(new_image, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2
                    )
    return new_image
