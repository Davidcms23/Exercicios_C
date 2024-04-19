from time import sleep
s = 0
for c in range(0, 6):
    n = int(input('Dígite um número: '))
    if n%2 == 0:
        s += n
        print('\33[0:32mNúmero selecionado\33[m: \33[0:33m{}\33[m'.format(n))
print('A soma dos números pares é: \33[0:32m{}\33[m'.format(s))