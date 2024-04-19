n1 = int(input('Dígite o primeiro termo: '))
n2 = int(input('Dígite a razão: '))
decimo = n1 + 10 * n2
for c in range(n1, decimo, n2):
    print('{} ->'.format(c), end=' ')
print('Acabou')
