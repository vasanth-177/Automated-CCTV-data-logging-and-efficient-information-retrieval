import dlib
import cv2
import os
#step1: read the image

goal_dir = os.path.join(os.getcwd(),"output/")
image = cv2.imread("/home/yukan/MyWorkSpace/Project-Final/Image/img1.jpeg")

#step2: converts to gray image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#step3: get HOG face detector and faces
hogFaceDetector = dlib.get_frontal_face_detector()
faces = hogFaceDetector(gray, 1)

#step4: loop through each face and draw a rect around it
f=1

for (i, rect) in enumerate(faces):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    #draw a rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    crop_img = image[y:y+h, x:x+w]
    filename =goal_dir+'img'+str(f)+'.jpg'
    f+=1
    try:
        print(goal_dir,filename)
        cv2.imwrite(filename, crop_img)
    except:
        pass
    
#step5: display the resulted image

# while 1:
#     cv2.imshow("Image", image)
#     cv2.waitKey(1)