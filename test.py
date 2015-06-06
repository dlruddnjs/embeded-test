import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import cv
import pygame
print "Motion Sensor"


pygame.init()
screen=pygame.display.set_mode((1500,1500))
background=pygame.image.load("1.png")
background.convert_alpha()
screen.blit(background, (0, 0))
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.OUT)
cap=cv2.VideoCapture()
obj=cap.open('111.3gp')

while True:
	pygame.display.update()
	GPIO.output(23, 0)
	i=GPIO.input(18)
	if i==True:
		if obj==True:
			while(True):
				f,frame=cap.read()
				if f == False:
					break
				
				cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
				cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
				cv2.imshow("test", frame)
				ch=cv2.waitKey(10)

				if ch==27:
					break

			cap.release()
			cv2.destroyALLWindows()
	GPIO.output(23, 1)
	time.sleep(1)
	
print "GPIO.cleanup()"
GPIO.cleanup()






