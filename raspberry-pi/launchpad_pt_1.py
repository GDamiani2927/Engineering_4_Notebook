import time
import board #type: ignore
import digitalio #type: ignore

for i in range(10,0,-1): #decrement from 10 to 1 by one 
    print(i)
    time.sleep(1) #every second
print("LIFTOFF!") #print liftoff after countdown