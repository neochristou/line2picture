import sys

import cv2
import numpy as np

original = cv2.imread(sys.argv[1])

gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gray_smooth = cv2.bilateralFilter(gray, 7, 60, 60)
outline = cv2.Canny(gray_smooth, 60, 120)
gray_outline = cv2.add(gray, outline)
outline_3_channel = np.stack((outline,) * 3, axis=-1)
cv2.imwrite("output.png", outline_3_channel)
