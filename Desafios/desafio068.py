from random import randint
print('=-'*20, '\nVamos jogar Par ou Impar\n', '=-'*20)
pontos = 0
while True:
    n = int(input('Dígite um valor: '))
    pi = input('Par ou impar [P/I]?').upper()
    NPC = randint(0, 10)
    soma = (n + NPC) % 2
    if pi == 'P':
        pi = 0
    elif pi == 'I':
        pi = 1
    if soma == 0:
        print('\33[0:34mPAR\33[m')
    else:
        print('\33[0:34mImpar\33[m')
    print(f'Pontos: \33[0:32m{pontos}\33[m')
    if pi == soma:
        print('\33[0:32mVocê Ganhou!!!\33[m')
        pontos += 1
    else:
        print('\33[0:31mPerdeu\33[m')
        break