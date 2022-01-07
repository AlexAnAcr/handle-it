import win32clipboard


averaged = []

with open('result.txt','r') as f:
    for rg in [2, 1000, 10000, 100000, 1000000, 10000000, 100000000, 200000000, 300000000, 400000000]:
        while True:
            row = f.readline().strip()
            
            if (len(row.split(';')) == 3 and row.split(';')[0] == '8' and row.split(';')[1] == str(rg)): #Settings
                break;

        raw = []
        while row != '':
            raw.append(int(row.split(';')[2]))
            row = f.readline().strip()

        filtered = 0
        if (rg != 2):
            for i in raw:
                filtered += i
            averaged.append(filtered / len(raw))
        else:
            for i in range(10, 20):
                filtered += raw[i]
            averaged.append(filtered / 10)
            
            filtered = 0
            for i in range(100, 110):
                filtered += raw[i]
            averaged.append(filtered / 10)
            


str0 = ""

for i in averaged:
    str0 += str(i) + '\n'


win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(str0[:-1])
win32clipboard.CloseClipboard()
