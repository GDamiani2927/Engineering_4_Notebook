import time
import board #type: ignore
import digitalio #type: ignore

redLed = digitalio.DigitalInOut(board.GP17)
redLed.direction = digitalio.Direction.OUTPUT
greenLed = digitalio.DigitalInOut(board.GP16)
greenLed.direction = digitalio.Direction.OUTPUT

for i in range(10,0,-1): #decrement from 10 to 1 by one 
    print(i)
    redLed.value=True #turn on red LED
    time.sleep(0.2) #wait 0.2 seconds
    redLed.value=False #turn off red LED
    time.sleep(0.8) #wait 0.8 seconds (0.2+0.8=1)
print("LIFTOFF!") #print liftoff after countdown
while True:
    greenLed.value=True #keep green LED on indefinitely
