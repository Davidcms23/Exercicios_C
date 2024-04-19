from random import randint
from time import sleep
mega = []
r = int(input('Quantos jogos você quer eu eu sorteie? '))
print('-'*30)
for l in range(0, r):
    mega.append([])
    for n in range(0, 6):
        numero = randint(1, 61)
        while numero in mega[l]:
            numero = randint(1, 61)
        else:
            mega[l].append(numero)
    sleep(1)
    print(f'Jogo numero {l+1}: {mega[l]}')



