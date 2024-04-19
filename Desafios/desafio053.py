nome = str(input('Dígite um nome: ')).strip()
n1 = len(nome)
r = ''
for c in range(n1-1, -1, -1):
    n1 = n1 - 1
    print('{}'.format(nome[n1]), end='')
    r = r + nome[n1]
l = r.split()
l = ''.join(l)
i = nome.split()
i = ''.join(i)
print('\nSeu nome é: {}'.format(l))
if i.upper() == l.upper():
    print('\33[0:32mPalíndromo\33[m')
else:
    print('\33[0:31mNormal\33[m')
print(l)