import time
from random import randint

def star():
    print(' '*39, '/ \\')
    print(' '*36, '---   ---')
    print(' '*37, '/     \\')

o = ' o'
i = 0
while True:
    print('')
    star()
    for j in range(1, 11):
        a = o*j
        if i%2 == 0:
            b = list(a)
            n = randint(1, len(a) - 1)
            b[n] = '*'
            a = ''.join(b)
        print(' '*(40 - j), a)
        if j!=10: print()
    print('Happy New Year!')
    i+= 1
    time.sleep(0.5)
