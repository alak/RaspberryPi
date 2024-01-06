# import gpiod
# import time
# ENA_PIN = 4
# IN1_PIN = 17
# IN2_PIN = 27
# chip = gpiod.Chip('gpiochip4')
# ena_line = chip.get_line(ENA_PIN)
# ena_line.request(consumer="ENA_MOTOR", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

# in1_line = chip.get_line(IN1_PIN)
# in1_line.request(consumer="IN1_MOTOR", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

# in2_line = chip.get_line(IN2_PIN)
# in2_line.request(consumer="IN2_MOTOR", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
# try:
#    while True:
#        print("start")
#        ena_line.set_value(1)
#        in1_line.set_value(1)
#        in2_line.set_value(0)
#        print("sleep")
#        time.sleep(20)
#        print("endsleep")
#        ena_line.set_value(0)
#        in1_line.set_value(0)
#        print("stop")
#        time.sleep(1)
       
# finally:
#    print("release")
#    led_line.release()

# import gpiod
# import time
# LED_PIN = 21
# chip = gpiod.Chip('gpiochip4')
# led_line = chip.get_line(LED_PIN)
# led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
# try:
#    while True:
#        led_line.set_value(1)
#        time.sleep(1)
#        led_line.set_value(0)
#        time.sleep(1)
# finally:
#    led_line.release()

from gpiozero import LED
from time import sleep

led = LED(21)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)