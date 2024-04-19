lista = []
pessoa = []
maior = []
menor = []
while True:
    pessoa = [input('Nome: '), float(input('Peso: '))]
    lista.append(pessoa)
    r = input('Quer continuar? [S/N]: ').upper()
    while r not in 'SN':
        r = input('Dígite algo valido, quer continuar? [S/N]: ').upper()
    if r == 'N':
        break
for c in lista:
    if c[1] == max(lista)[1]:
        maior.append(c[0])
    elif c[1] == min(lista)[1]:
        menor.append(c[0])
print('-='*30)
print(f'O maior peso é {max(lista)[1]}kg. Peso de {maior}\nO menor peso é {min(lista)[1]}kg. Peso de {menor}')
print(f'Foram cadastradas {len(lista)} pessoas')

