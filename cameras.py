# we can't use the pi to encode midflight because it's too slow
# 1 image is > 200KB as jpg, 6 hours
# 1/s is 4.3GB - 1s delay
# 2/s is 8.6GB - 0.5s delay
# 4/s is 17.2GB - 0.25s delay
import shutil
import cv2
import time

i = 0

camera1 = cv2.VideoCapture(0) #camera should be /dev/video0
camera1.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) 
camera1.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    try:
        total, used, free = shutil.disk_usage("/")
        if (free > 2000000000): #check that there is > 2GB free
            taken1, output1 = camera1.read()
            cv2.imwrite("./output/frame" + str(i) + ".jpg", output1)
            time.sleep(0.25)
            i = i + 1
        else: #Whether this triggers with depend on how long the battery lasts. 
            print("Disk is too close to the satety cutoff")
            exit()
    except Exception as e:
        print(e)