t50 = t20 = t10 = t1 = 0
print('='*40)
print('{:^40}'.format('BANK PAGUE MAIS'))
print('='*40)
valor = int(input('Qual valor você quer sacar: R$'))
while True:
    if valor >= 50:
        valor -= 50
        t50 += 1
    elif valor >= 20:
        valor -= 20
        t20 += 1
    elif valor >= 10:
        valor -= 10
        t10 += 1
    elif valor >= 1:
        valor -= 1
        t1 += 1
    elif valor == 0:
        break
if t50 > 0:
    print(f'Total de \33[0:32m{t50}\33[m cédulas de R$50')
if t20 > 0:
    print(f'Total de \33[0:32m{t20}\33[m cédulas de R$20')
if t10 > 0:
    print(f'Total de \33[0:32m{t10}\33[m cédulas de R$10')
if t1 > 0:
    print(f'Total de \33[0:32m{t1}\33[m cédulas de R$1')
