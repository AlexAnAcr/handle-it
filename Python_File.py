import subprocess
import time

procount = []
prew = ''
for i in range(2,9):

    for k in [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 200000000, 300000000, 400000000]:
        tim = 0.0
        count = 0
        for j in range(0,10):
            args = ['mpiexec', '-n', str(i), 'main.exe', str(k + j)]
            subprocess.call(args)
            with open('output.txt', 'r') as f:
                cs = f.readline().strip()
                if (prew != cs):
                    prew = cs
                    count += 1
                    tim += float(cs)
            time.sleep(1)

        if (count > 0):
            tim /= count
            procount.append([i, k, tim])
        else:
            procount.append([i, k, -1])
        print(procount[-1])

print(procount)

print("Time:")
for i in procount:
    print(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]))
