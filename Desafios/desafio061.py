n1 = int(input('Qual o primeiro termo: '))
n2 = int(input('Razão da PA: '))
r = 0
while r <= 9:
    print('{} -> '.format(n1), end='')
    n1 = n1 + n2
    r += 1
print('FIM')