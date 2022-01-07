
with open('xil_dst.txt', 'r') as f:
    with open('xil_dst2.txt', 'w') as fw:
        for i in range(0, 100008):
            row = f.readline().strip()
            fw.write(row + '\n')        
