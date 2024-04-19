print('Pares entre 1 e 50')
from time import sleep
for c in range(1, 51):
    a = c % 2
    if a == 1:
        print('\33[0:32m{}(IMPAR)\33[m'.format(c), end=' ')
        sleep(0.5)
    if a == 0:
        print('\33[0:34m{}(PAR)\33[m'.format(c), end=' ')
        sleep(0.5)

