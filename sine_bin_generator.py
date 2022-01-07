import math
bitness = 14
points_count = 768

max_val = 2**(bitness - 1) - 1

def int_to_bytes(num):
    return num.to_bytes(length=(8+(num+(num<0)).bit_length()) // 8, byteorder='big', signed=True)

with open('out.txt','w') as f:
    for i in range(0, points_count):
        value = int(math.sin(i*2*math.pi/points_count)*max_val)
        bytess = int_to_bytes(value)
        bytesarr = [bytess[i:i+1] for i in range(0, len(bytess))]
        binStr = ''.join(format(ord(byte), '08b') for byte in bytesarr)
        binStrPad = binStr.rjust(bitness, binStr[0])
        if (len(binStrPad) > bitness):
            binStrPad = binStrPad[len(binStrPad) - bitness:]
        f.write('"' + binStrPad + '", ')
        if i % 8 == 7:
            f.write('\n')
