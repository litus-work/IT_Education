def sum_roman(a,b):
    str = a+b
    countI = 0
    countV = 0
    countX = 0
    X = 0
    V = 0
    I = 0

    for letter in str:
         if(letter == 'I'):
            countI += 1
    #print(countI,'I letters found')

    while countI > 4:
        countI = countI-5
        countV =countV+1

    for letter in str:
        if (letter == 'V'):
            countV += 1
    #print(countV, 'V letters found')
    while countV > 1:
        countV = countV-2
        countX =countX + 1

    for letter in str:
        if (letter == 'X'):
            countX += 1
    # print(countX, 'X letters found')
    while countX > 4:
        countX = countX - 5
        countL =countL+1


    print('Rom_Dig_is:'+('X' * countX) + ('V' * countV) + ('I' * countI))


sum_roman('VVVVVIIIII','VI')




