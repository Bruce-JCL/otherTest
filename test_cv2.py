import os
import cv2
import android
from AidLux import Aashmem
import numpy as np

ash=Aashmem("/tmp/"+str(0))

while True:
    byte=ash.get_bytes(1280*720*3, 4)
    img = np.frombuffer(byte, dtype=np.uint8).reshape(720, 1280, 3)
    bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("bgr_image",bgr_image)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()
            
