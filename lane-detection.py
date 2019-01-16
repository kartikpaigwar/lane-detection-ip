import cv2
import numpy as np

def lane(frame):
    # rgb = cv2.imread(img)
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img_gray = cv2.blur(img,(10,10),img)
    #edges = cv2.Canny(img_gray,50,150,apertureSize = 3)
    #sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobelx8u = cv2.Sobel(img_gray,cv2.CV_8U,1,0,ksize=5)

    thres = cv2.inRange(sobelx8u, 254, 255)
    lines = cv2.HoughLines(thres,1,np.pi/180,200)
    if lines is not None:
        l1_rho = 0
        l2_rho = 0
        l1_theta = 0
        l2_theta = 0
        l1_count = 0
        l2_count = 0
        for value in lines:
            rho = value[0][0]
            theta = value[0][1]
            if rho > 0: # negative
                l1_rho +=rho
                l1_theta +=theta
                l1_count+=1
            else:
                l2_rho += rho
                l2_theta += theta
                l2_count += 1
        if l1_count > 0:
            rho = l1_rho / l1_count
            theta = l1_theta / l1_count
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        if l2_count > 0:
            rho = l2_rho / l2_count
            theta = l2_theta / l2_count
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return frame

if __name__== "__main__":
    vid = cv2.VideoCapture('lane-detect.mkv')

    while(vid.isOpened()):
        ret, frame = vid.read()

        if ret==True:
            processed = lane(frame)
            cv2.imshow('image',processed)
            cv2.waitKey(50)

        else:
            break

    vid.release()
    cv2.destroyAllWindows()