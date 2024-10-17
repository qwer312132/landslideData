import cv2
import numpy as np
import os
import sys
import shutil
file = os.listdir("gt")
for i in file:
    img = cv2.imread("gt/"+i)
    if len(np.unique(img))>=2:
        shutil.copy("gt/"+i, "gtNoZero/"+i)
        shutil.copy("img/"+(i.replace(".png", ".tif")), "imgNoZero/"+(i.replace(".png", ".tif")))