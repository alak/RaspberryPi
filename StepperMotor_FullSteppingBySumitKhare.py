import gpiod
import time
LED_PIN = 17
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="MOTOR", type=gpiod.LINE_REQ_DIR_OUT)
try:
   while True:
       print("start")
       led_line.set_value(1)
       print("sleep")
       time.sleep(20)
       print("endsleep")
       led_line.set_value(0)
       print("stop")
       time.sleep(1)
       
finally:
   print("release")
   led_line.release()