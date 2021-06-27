import wiringpi as pi
import time

# GPIO pin assign
PINS =  4
PIN_S1 = 24
PIN_S2 = 23
PIN_S3 = 22
PIN_S4 = 27
PIN_L1 = 19
PIN_L2 = 13
PIN_L3 =  6
PIN_L4 =  5

# const lists
q = [2,1,2,0,0,3,1,0,2,2,0,3,1,2,0,1,3,1,1,2,0,0,1,2,0,3,0,1,3,2,3,0,1,2,0]
sw = [PIN_S1, PIN_S2, PIN_S3, PIN_S4]
led = [PIN_L1, PIN_L2, PIN_L3, PIN_L4]
tone = [784, 1047, 523, 659]

# GPIO initialization
pi.wiringPiSetupGpio()
pi.softToneCreate(PINS)
for i in sw:
    pi.pinMode(i, 0)
    pi.pullUpDnControl(i, 2)
for i in led:
    pi.pinMode(i, 1)
    pi.digitalWrite(i, 0)

# Main routine
for stage in range(1, len(q)+1):
    time.sleep(1.5)
    print("stage", stage)
    
    # Present a question
    for i in range(0, stage):
        print(q[i], end="")
        pi.digitalWrite(led[q[i]], 1)
        pi.softToneWrite(PINS, tone[q[i]])
        time.sleep(0.4)
        pi.digitalWrite(led[q[i]], 0)
        pi.softToneWrite(PINS, 0)
        time.sleep(0.1)
    print('')

    # Answer and judgment
    for i in range(0, stage):
        ans = -1
        while ans <0:
            for fet in range(4):
                if(pi.digitalRead(sw[fet]) == 0):
                    ans = fet
                    break
        if ans == q[i]:
            print("Hit")
            pi.digitalWrite(led[q[i]], 1)
            pi.softToneWrite(PINS, tone[q[i]])
            time.sleep(0.4)
            pi.digitalWrite(led[q[i]], 0)
            pi.softToneWrite(PINS, 0)
        else:
            print("Miss")
            break
    else:
        continue
    break

# Ending process
print("end")
for i in range(4):
    pi.digitalWrite(led[i], 1)
pi.softToneWrite(PINS, 100)
time.sleep(2)
for i in range(4):
    pi.digitalWrite(led[i], 0)
pi.softToneWrite(PINS, 0)
