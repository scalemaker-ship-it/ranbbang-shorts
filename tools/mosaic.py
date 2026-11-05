#!/usr/bin/env python3
"""실사 캡처 얼굴 모자이크 (2026-10-27 사용자 지시: 캡처 사진의 얼굴은 모자이크).
  python3 tools/mosaic.py <in> <out> [--box x,y,w,h ...] [--cell 14] [--min 0.5]
YuNet(opencv_zoo) 으로 얼굴을 찾아 픽셀화하고, --box 로 수동 영역을 더한다. 찾은 얼굴 수를 출력한다.
모델 = tools/models/face_detection_yunet_2023mar.onnx (없으면 opencv_zoo 에서 받는다).
"""
import os, sys, urllib.request
import cv2, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, "models", "face_detection_yunet_2023mar.onnx")
URL = "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"

def pixelate(im, x, y, w, h, cell):
    H, W = im.shape[:2]
    px = int(w * 0.25); py = int(h * 0.3)   # 얼굴 주변 여유
    x0, y0 = max(0, x - px), max(0, y - py); x1, y1 = min(W, x + w + px), min(H, y + h + py)
    roi = im[y0:y1, x0:x1]
    if roi.size == 0: return
    small = cv2.resize(roi, (max(1, (x1 - x0) // cell), max(1, (y1 - y0) // cell)), interpolation=cv2.INTER_LINEAR)
    im[y0:y1, x0:x1] = cv2.resize(small, (x1 - x0, y1 - y0), interpolation=cv2.INTER_NEAREST)

def detect(im, score=0.5):
    if not os.path.exists(MODEL):
        os.makedirs(os.path.dirname(MODEL), exist_ok=True); urllib.request.urlretrieve(URL, MODEL)
    H, W = im.shape[:2]
    faces = []
    for scale in (1.0, 2.0):   # 작은 얼굴은 확대해서 한 번 더
        img = im if scale == 1.0 else cv2.resize(im, None, fx=scale, fy=scale)
        det = cv2.FaceDetectorYN.create(MODEL, "", (img.shape[1], img.shape[0]), score, 0.3, 5000)
        _, f = det.detect(img)
        for r in (f if f is not None else []):
            x, y, w, h = [int(v / scale) for v in r[:4]]
            if not any(abs(x - a) < w / 2 and abs(y - b) < h / 2 for a, b, _, _ in faces):
                faces.append((x, y, w, h))
    return faces

def run(src, dst, boxes=(), cell=14, score=0.5):
    im = cv2.imread(src)
    assert im is not None, src
    faces = detect(im, score)
    for x, y, w, h in faces: pixelate(im, x, y, w, h, cell)
    for x, y, w, h in boxes: pixelate(im, x, y, w, h, cell)
    cv2.imwrite(dst, im, [cv2.IMWRITE_JPEG_QUALITY, 93])
    return faces

if __name__ == "__main__":
    a = sys.argv[1:]; boxes = []; cell = 14; score = 0.5
    while "--box" in a:
        i = a.index("--box"); boxes.append(tuple(int(v) for v in a[i + 1].split(","))); del a[i:i + 2]
    if "--cell" in a: i = a.index("--cell"); cell = int(a[i + 1]); del a[i:i + 2]
    if "--min" in a: i = a.index("--min"); score = float(a[i + 1]); del a[i:i + 2]
    f = run(a[0], a[1], boxes, cell, score)
    print(f"faces {len(f)} {f} + boxes {len(boxes)} -> {a[1]}")
