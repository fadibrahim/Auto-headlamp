import cv2
import serial
import time

cars_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
arduino = serial.Serial('COM5', baudrate = 115200, timeout=.0) #ganti COM sama COM Arduino di PCr

global x_line
global x_medium
global x_max

x_max = 640

def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 255, 0), thickness=2)
        x_medium = int((x + x + w) / 2)
        x_line = x_max - x_medium
        arduino.write(str(x_line).encode('utf-8'))
        print(x_line)
        time.sleep(0.1)
        
    if cars == ():
        # cars =  [[ 320,0,0,0]]
        x_line = 320
        arduino.write(str(x_line).encode('utf-8'))
        print(x_line)
        time.sleep(0.1)
    return frame

def Simulator():
    CarVideo = cv2.VideoCapture(0)
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:        
            cars_frame = detect_cars(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
        else:
            break
        if controlkey == ord('q'):
            break

    CarVideo.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Simulator()