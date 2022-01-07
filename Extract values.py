import win32clipboard

raw = []

with open('result.txt','r') as f:
    while True:
        row = f.readline().strip()
        
        if (len(row.split(';')) == 3 and row.split(';')[0] == '2' and row.split(';')[1] == '1000'): #Settings
            break;
    
    while row != '':
        raw.append(int(row.split(';')[2]))
        row = f.readline().strip()

for i in range(1, len(raw) - 1):
    if raw[i] > (raw[i-1]+raw[i+1]) / 1.8:
        raw[i] = int((raw[i-1]+raw[i+1]) / 2)

str0 = ""

for i in raw:
    str0 += str(i) + '\n'


win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(str0[:-1])
win32clipboard.CloseClipboard()
