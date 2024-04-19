a = int(input('Dígite um número: '))
n = a
while a > 1:
    print('A fatorial de {}!: '.format(a), end='')
    for c in range(a, 1, -1):
        print('{} x '.format(a), end='')
        c -= 1
        n = n * c
        a -= 1
print('1 = ', end='')
print('\33[0:32m{}\33[m '.format(n))

