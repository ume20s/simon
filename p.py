import time

q = [2,1,2,4,3,3,1,4,2,2,4,3,1,2,4,1,3,1,1,2,4,4,1,2,4,3,4,1,3,2,3,4,1,2,4]

for stage in range(1, len(q)+1):
    print("stage", stage)
    
    # Present a question
    for i in range(0, stage):
        print(q[i], end='')
        time.sleep(0.5)
    print('')
    
    # Answer and judgment
    for i in range(0, stage):
        ans = int(input())
        if ans == q[i]:
            print("Hit")
        else:
            print("Miss")
            break
    else:
        continue
    break

# Ending process
print("end")
