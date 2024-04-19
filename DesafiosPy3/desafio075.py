n1 = int(input('Dígite um número: '))
n2 = int(input('Dígite outro número: '))
n3 = int(input('Dígite mais um número: '))
n4 = int(input('Dígite o último número: '))
numeros = n1, n2, n3, n4
n = '0'
quantidade_par = 0
for n in range(0, 4):
    num = n1, n2, n3, n4
    p = num[n]%2
    if p == 0:
        quantidade_par += 1
print(f'Você dígitou os números {numeros}')
print(f'O valor 9 aarece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 foi dígitado na {numeros.index(3)+1}° posição')
else:
    print('Você não dígitou o número 3')
print(f'Os números pares são: {quantidade_par}')