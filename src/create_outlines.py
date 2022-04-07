import glob

import cv2
import numpy as np

for filename in glob.glob("../data/*jpg"):

    print(filename)
    original = cv2.imread(filename)
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    gray_smooth = cv2.bilateralFilter(gray, 7, 60, 60)
    outline = cv2.Canny(gray_smooth, 60, 120)
    gray_outline = cv2.add(gray, outline)
    outline_3_channel = np.stack((outline,) * 3, axis=-1)
    out_filename = filename.replace(".jpg", "_outline.jpg")
    cv2.imwrite(out_filename, outline_3_channel)
