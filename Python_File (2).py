import subprocess
import time

procount = {}
for i in range(1,17):
    res = 0.0
    tim = 0.0

    for j in range(0,10):
        args = ['main.exe', str(i)]
        subprocess.call(args)
        with open('output.txt', 'r') as f:
            arr =f.readline()[:-1].split(';')
            res += float(arr[0])
            tim += float(arr[1])
        time.sleep(1)

    res /= 10
    tim /= 10

    procount[i] = [res, tim]
    
    print(procount[i])

print("Time:")
for i in procount:
    print(str(i) + ";" + str(procount[i][1]))

print("Error:")
for i in [1,2,4,10]:
    print(str(i) + ";" + str(procount[i][0]))
