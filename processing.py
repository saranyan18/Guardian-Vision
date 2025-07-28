import cv2
import numpy as np

input_width, input_height = 512, 512
conf_threshold = 0.3
iou_threshold = 0.5

def preprocess(frame):
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (input_width, input_height)).astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    return np.expand_dims(img, axis=0)

def postprocess(outputs, orig_shape):
    output = outputs[0]
    boxes = output[0, :4, :]
    scores = output[0, 4, :]

    mask = scores > conf_threshold
    boxes = boxes[:, mask]
    scores = scores[mask]

    if boxes.shape[1] == 0:
        return [], []

    x_c, y_c, w, h = boxes
    x1 = x_c - w / 2
    y1 = y_c - h / 2
    x2 = x_c + w / 2
    y2 = y_c + h / 2

    orig_h, orig_w = orig_shape[:2]
    scale_x = orig_w / input_width
    scale_y = orig_h / input_height

    x1 = (x1 * scale_x).astype(int)
    y1 = (y1 * scale_y).astype(int)
    x2 = (x2 * scale_x).astype(int)
    y2 = (y2 * scale_y).astype(int)

    boxes_scaled = np.stack([x1, y1, x2, y2], axis=1)
    boxes_xywh = [[x, y, x2 - x, y2 - y] for x, y, x2, y2 in boxes_scaled]

    scores_list = scores.tolist()
    indices = cv2.dnn.NMSBoxes(boxes_xywh, scores_list, conf_threshold, iou_threshold)

    if len(indices) == 0:
        return [], []

    indices = indices.flatten()
    return boxes_scaled[indices], scores[indices]
