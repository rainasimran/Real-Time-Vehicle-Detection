import cv2

vehiclexml=cv2.CascadeClassifier('vehicle2.xml') #xml file imported/read




def detection(frame):  #function defined to detect cars through frames

    vehicle=vehiclexml.detectMultiScale(frame,1.15,4)

    for (x,y,w,h) in vehicle:

        cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)


        cv2.putText(frame,'Vehicle Detected',(x+w,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=2)

    return frame




def capturescreen():  #function created for live time detection using frames.

    realtimevideo=cv2.VideoCapture(0)     #camera module
    #realtimevideo=cv2.VideoCapture('traffic.mp4')       #video module
    # realtimevideo=cv2.VideoCapture('Cars On The Road.mp4')
    # realtimevideo=cv2.VideoCapture('Pexels Videos 2103099.mp4')
    #realtimevideo=cv2.VideoCapture('vecteezy_busy-traffic-on-the-highway_6434705_181.mp4')

    while realtimevideo.isOpened():

        ret,frame=realtimevideo.read()

        controlkey=cv2.waitKey(1)

        if ret:

            vehicleframe=detection(frame)

            cv2.imshow('vehicle detection',vehicleframe)

        else:

            break

        if controlkey==ord('q'):

            break


    realtimevideo.release()

    cv2.destroyAllWindows()




capturescreen()