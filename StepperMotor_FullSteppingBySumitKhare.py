import gpiod
import time

chip = gpiod.Chip('gpiochip4')

ControlPin=[7,11,13,15]
les_pins=[]

for pin in ControlPin:
    l = chip.get_line(pin)
    les_pins.append(l)
    l.request(consumer="MOTOR", type=gpiod.LINE_REQ_DIR_OUT)
    
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
                les_pins[pin].set_value(seq[fullStep][pin])
                time.sleep(0.001)
        
 
for pin in les_pins:
    pin.release()

