n = int(input('Dígite um Número: '))
p = 0
d = 0
cc = n + 1
for c in range(1, cc, 1):
    d = n % c
    if d == 0:
        print('\33[0:32m{}\33[m ->'.format(c), end=' ')
        p = p + 1
    else:
        print('\33[0:31m{}\33[m ->'.format(c), end=' ')
print('ACABOU')
if p == 2:
    print('O número {} é \33[0:32mPRIMO\33[m'.format(n))
elif p >= 3:
    print('Não é \33[0:31mPrimo\33[m')
else:
    print('Não é \33[0:31mPrimo\33[m')
