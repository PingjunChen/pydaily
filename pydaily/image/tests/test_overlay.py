# -*- coding: utf-8 -*-

import os, sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pydaily.image import overlay_bbox, overlay_contour
from pydaily import DATA_DIR


def test_overlay_bbox():
    # load image
    img_path = os.path.join(DATA_DIR, "TestImgs", "pathology_test01.jpg")
    img = cv2.imread(img_path)
    img = img[...,::-1]

    bboxes = [[100, 20, 130, 140],
    [210, 110, 270, 260],
    [100, 100, 160, 180],
    ]

    rgb = (0, 255, 0)
    img = overlay_bbox(img, bboxes, rgb, stroke=5)


    plt.imshow(img)
    plt.axis('off')
    plt.show()


def test_overlay_cnt():
    # load image
    img_path = os.path.join(DATA_DIR, "TestImgs", "pathology_test01.jpg")
    img = cv2.imread(img_path)
    img = img[...,::-1]

    cnt = [[250, 280, 350, 310, 210, 180, 160, 190],
        [60, 70, 160, 200, 280, 240, 190, 120, ],
        ]
    cnt = np.asarray(cnt)

    rgb = (0, 0, 240)
    img = overlay_contour(img, cnt, rgb, cnt_width=5)

    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    test_overlay_bbox()
    # test_overlay_cnt()
