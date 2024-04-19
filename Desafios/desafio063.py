r = int(input('Quantos termos você quer mostrar? '))
n1 = 1
n2 = 1
n = 1
print('0 -> ', end='')
par = r % 2
r = r // 2
while r - 1 >= n:
    n += 1
    print('{} -> '.format(n1), end='')
    print('{} -> '.format(n2), end='')
    n1 = n1 + n2
    n2 = n1 + n2
print('{} -> '.format(n1), end='')
if par == 1:
    print('{} ->'.format(n2), end='')
print('\33[0:34mFIM {}\33[m'.format(par))