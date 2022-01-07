with open('shift.txt', 'r') as f1:
    with open('xil_dst.txt', 'r') as f2:
        counter = 0
        row1 = f1.readline().strip()
        row2 = f2.readline().strip()
        while True:
            if row1 == '' or row2 == '':
                print('The samples are same.')
                break;
            if row1[:-2] != row2:
                print('The samples are NOT same: ' + str(counter))
                print('ADS: ' + row1[:-2])
                print('Xil: ' + row2)
                break;
            counter += 1
            row1 = f1.readline().strip()
            row2 = f2.readline().strip()
