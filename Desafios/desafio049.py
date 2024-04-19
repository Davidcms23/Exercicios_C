from time import sleep
n = int(input('Escolha um Numero: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c * n))
    sleep(0.3)