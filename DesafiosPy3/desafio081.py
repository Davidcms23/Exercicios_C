numeros = []
while True:
    n = int(input('Dígite um valor: '))
    numeros.append(n)
    continua = str(input('Quer continuar [S/N]: ')).upper()
    while continua not in 'SN':
        print('\33[0:32mEntrada invalida\33[m, Dígite S ou N')
        continua = str(input('Quer continuar [S/N]: ')).upper()
    if continua == 'N':
        break
print('='*30)
numeros.sort(reverse=True)
print(f'\33[0:35m{numeros}\33[m')
print('='*30)
print(f'Na lista contem \33[0:32m{len(numeros)}\33[m numeros')
print('='*30)
if 5 in numeros:
    print('\33[0:32mA lista tem o numero 5\33[m')
else:
    print('\33[0:32A não lista tem o número 5\33[m')
print('=' * 30)