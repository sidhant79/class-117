import os
import cv2

path = "C:\WhiteHat jr/Classwork/class 117/c117-videoCapture-1-4-main/c117-videoCapture-1-4-main/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images.append(file_name)
        
print("Total frame count :",len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
print("Width and height of the frame : ",size)

out=cv2.VideoWriter('Sun.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")








