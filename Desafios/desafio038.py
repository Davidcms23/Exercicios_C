n1 = int(input('Dígite um valor: '))
n2 = int(input('Dígite outro valor: '))

if n1 > n2:
    print('{} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('Os dois valores são iguais.')