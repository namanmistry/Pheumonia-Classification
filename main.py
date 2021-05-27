import numpy as np
import os
import cv2

data = []

for file in os.listdir("./data/train/NORMAL"):
    try:
        img = cv2.imread(f"./data/train/NORMAL/{file}")
        img = cv2.resize(img,(100,100))
        img_array = np.array(img).flatten()
        data.append([img_array,0])
        break
    except Exception as e:
        pass

print(data[0])
