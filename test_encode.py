import os
import cv2
import android
from AidLux import Aashmem
import numpy as np
import time

ash=Aashmem("/tmp/"+str(0))
ash1=Aashmem("/tmp/"+str(1))
t1=time.time()
print("t1",t1)

while True:
    ##pull
    index=ash.get_bytes(4, 0)
    decode_trip = int.from_bytes(index, byteorder='little')
    print("decode_trip",decode_trip)
    t2=time.time()
    print("t2-t1",(t2-t1))
    # if t2-t1>60:
    #     break
    if decode_trip!=1:
        if decode_trip==2:
            print("break")
            break
        else:
            continue
    byte=ash.get_bytes(1280*720*3, 4)
    ##push
    o=1
    encode_trap=o.to_bytes(4, byteorder='little', signed=True)   
    ash1.set_bytes(encode_trap,4,0)
    ash1.set_bytes(byte,len(byte),4)
    img = np.frombuffer(byte, dtype=np.uint8).reshape(720, 1280, 3)
    bgr_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("bgr_image",bgr_image)
    cv2.waitKey(1)
    
print("break")
k=2
encode_trap=k.to_bytes(4, byteorder='little', signed=True)   
ash1.set_bytes(encode_trap,4,0)
cv2.destroyAllWindows()