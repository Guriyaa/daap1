import cv2
cascade_path = 'haarcascade_fullbody.xml'
classifier = cv2.CascadeClassifier(cascade_path)
path = r'C:\Users\Lenovo\Pictures\Camera Roll\WIN_20221225_15_28_21_Pro.mp4'  # 0 for webcam
video = cv2.VideoCapture(path)


while True:
    status, image  = video.read()
    if  not status:
        print('could not read frame')
        break
    # logic
    image = cv2.resize(image,(0,0),fx = 0.4, fy = 0.4)
    detection = classifier.detectMultiScale(image,
                                            scaleFactor=1.5,
                                            minNeighbors=3,
                                            minSize=(20,20))
    if len(detection)>0:
         print(f'Found {len(detection)} peope')
         for(x,y,w,h) in detection:
             cv2.rectangle(image,(x,y),(x+w), (0,255,0),2)
         img_egde = cv2.Canny(image, 100, 200)
    cv2.imshow('video', image)
    if cv2.waitKey(1) == ord('q'):
        break
video.release() # windows
cv2.destroyAllWindows() #close all windows
