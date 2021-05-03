import Rpi.GIPO as GPIO
import time
pwm_obj=GPIO.PWM(18,400)
pwm_obj.start(100)
pwm_obj.ChangeDutyCycle(50)
while True:
    GPIO.output(18,True)
    time.sleep(0.5)
    GPIO.output(18,False)
    time.sleep(0.5)