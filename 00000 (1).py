
with open('sinus.txt', 'r') as f:
    with open('sinus2.txt', 'w') as fw:
        row = f.readline().strip()[:-2]
        while True:
            if (row == ''):
                break;
            fw.write(row + '\n')
            row = f.readline().strip()[:-2]
        
