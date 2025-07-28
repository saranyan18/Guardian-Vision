import cv2

def fancy_box(img, box, score, label="Object", color=(0, 255, 255), thickness=3):
    x1, y1, x2, y2 = box
    r, l = 12, 18

    corners = [
        ((x1 + r, y1 + r), 180, (x1 + r + l, y1), (x1, y1 + r + l)),
        ((x2 - r, y1 + r), 270, (x2 - r - l, y1), (x2, y1 + r + l)),
        ((x1 + r, y2 - r), 90, (x1 + r + l, y2), (x1, y2 - r - l)),
        ((x2 - r, y2 - r), 0, (x2 - r - l, y2), (x2, y2 - r - l)),
    ]

    for (ellipse_center, angle, line1_end, line2_end) in corners:
        cv2.ellipse(img, ellipse_center, (r, r), angle, 0, 90, color, thickness)
        cv2.line(img, ellipse_center, line1_end, color, thickness)
        cv2.line(img, ellipse_center, line2_end, color, thickness)

    text = f"{label}: {score:.2f}"
    font = cv2.FONT_HERSHEY_DUPLEX
    (tw, th), _ = cv2.getTextSize(text, font, 0.5, 1)
    #cv2.rectangle(img, (x1, y1 - th - 10), (x1 + tw + 8, y1), color, -1)
    #cv2.putText(img, text, (x1 + 4, y1 - 4), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    #cv2.putText(img, text, (x1 + 4, y1 - 4), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
