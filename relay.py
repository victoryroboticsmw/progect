import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redled = 23
fountain = 25
GPIO.setup(redled,GPIO.OUT,initail=GPIO.LOW
GPIO.output(redled,GPIO.HIGH)
time.sleep(5)
GPIO.output(redled,GPIO.LOW)
GPIO.sleep(5)
