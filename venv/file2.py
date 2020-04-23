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
         elif (letter == 'V'):
             countV += 1
         elif (letter == 'X'):
             countX += 1
    I=countI%5
    V=(countV+countI//5)%2
    X=(countX+(countV+countI//5)//2)%5
    L=(countX+(countV+countI//5)//2)//5

    print('Rom_Dig_is:'+('L'*L)+('X' * X) + ('V' * V) + ('I' * I))

sum_roman('IIIII IIIII IIIII IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIXIIIIII','')
#
#
#
#
