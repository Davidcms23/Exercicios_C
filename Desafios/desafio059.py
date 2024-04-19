from time import sleep
while True:
    n1 = int(input('Dígite o 1° número: '))
    n2 = int(input('Dígite o 2° número: '))
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair do Programa')
    op = int(input('Escolha uma das opções: '))
    #Somar
    if op == 1:
        print('\33[0:33m{} + {} = {}\33[m'.format(n1, n2, n1+n2))
    #Multiplicar
    elif op == 2:
        print('\33[0:32m{} * {} = {}\33[m'.format(n1, n2, n1*n2))
    #Maior
    elif op == 3:
        if n1 > n2:
            print('\33[0:31m{} > {}\33[m'.format(n1, n2))
        elif n2 > n1:
            print('\33[0:34m{} > {}\33[m'.format(n2, n1))
        else:
            print('\33[0:31m{}\33[m = \33[0:34m{}\33[m'.format(n1, n2))
    #Novos Numeros
    elif op == 4:
        print('Voltando...')
        sleep(3)
        continue
    elif op == 5:
        break