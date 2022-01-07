import math
bitness = 16
points_count = 1024


max_val = 2**(bitness - 1) - 1

def int_to_bytes(num):
    return num.to_bytes(length=(8+(num+(num<0)).bit_length()) // 8, byteorder='big', signed=True)

with open('out.txt','w') as f:
    for i in range(0, points_count):
        value = int(math.sin(i*2*math.pi/points_count)*max_val)
        i += 1
        value = int_to_bytes(value)
        strHex =  'x"' + value.hex().ljust(4, '0') + '"'
        f.write(strHex + ', ')
        if i % 8 == 0:
            f.write('\n')
        
            
