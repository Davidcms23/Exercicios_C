import random
n = 0
t = 0
while True:
    r = int(input('Escolha um número de 1 a 10:'))
    n = random.randint(1, 10)
    print('O número escolhido foi: \33[0:32m{}\33[m'.format(n))
    if r == n:
        print('\33[0:32mAcertou\33[m \nPrecisou de \33[0:34m{}\33[m tentativas'.format(t))
        break
    else:
        print('\33[0:31mTente novamente\33[m')
        t += 1