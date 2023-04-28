#coding: utf-8
import RPi.GPIO as GPIO
import time

#macro
servo=24
#setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT,initial=GPIO.LOW)
#pwm signal
p = GPIO.PWM(servo, 50) #50Hz
#start of pwm
p.start(0) #duty ratio 0%

p.ChangeDutyCycle(7.5) #0degree
time.sleep(1)
for i in range(3):
    p.ChangeDuty(2.5) #-90dgree
    time.sleep(1)
    p.ChangeDutyCycle(7.5) #0degree
    time.sleep(1)
    p.ChangeDutyCycle(12) #90degree
    time.sleep(1)
    p.ChangeDutyCycle(7.5) #0degree
    time.sleep(1)

#cleanup
p.stop()
GPIO.cleanup()