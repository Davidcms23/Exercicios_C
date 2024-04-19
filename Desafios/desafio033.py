n1 = int(input('Dígite o primeiro valor: '))
n2 = int(input('Dígite o segundo valor: '))
n3 = int(input('Dígite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print('O maior é {}'.format(n1))
    if n2 < n3:
        print('O menor é {}'.format(n2))
    else:
        print('O menor é {}'.format(n3))
if n2 > n1 and n2 > n3:
    print('O maior é {}'.format(n2))
    if n1 < n3:
        print('O menor é {}'.format(n1))
    else:
        print('O menor é {}'.format(n3))
if n3 > n1 and n3 > n2:
    print('O maior é {}'.format(n3))
    if n1 < n2:
        print('O menor é {}'.format(n1))
    else:
        print('O menor é {}'.format(n2))
