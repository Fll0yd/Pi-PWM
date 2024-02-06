import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED_PIN = 8
GPIO.setup(LED_PIN, GPIO.OUT)

PWM_FREQ = 50 
PWM_RANGE = 100 
pwm = GPIO.PWM(LED_PIN, PWM_FREQ)
LED_PWM.start(0)

try:
    while True:
        
        for duty_cycle in range(0, PWM_RANGE + 1):
         pwm.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)

        for duty_cycle in range(PWM_RANGE, -1, -1):
         pwm.ChangeDutyCycle(duty_cycle)
         time.sleep(0.01)   
           
except KeyboardInterrupt:
    pass

LED_PWM.stop()
GPIO.cleanup()