import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


ControlPin=[7,11,13,15]

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)
    
seq=    [[1,1,0,0],  
         [0,1,1,0],
         [0,0,1,1],
         [1,0,0,1],
]


rotationNeeded=0
rotationCount=0
while(1):
    rotationNeeded==0
    print("\n")
    userInput=input("Press e-exit, How many rotation needed...")
    print("\n")
    if userInput=='e':
        break;
    
    rotationNeeded=int(userInput)
    rotationCount=50* rotationNeeded

    for i in range(rotationCount ):
        for fullStep in range(4):
            for pin in range(4):
                GPIO.output(ControlPin[pin],seq[fullStep][pin])
                time.sleep(0.001)
        
 
GPIO.cleanup()
