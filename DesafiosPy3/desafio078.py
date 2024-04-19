r = []
for n in range(0, 5):
    r += input(f'Dígite um úmero na posição {n}: ')
print(f'Você dígitou os valores: {r}')
print(f'O maior valor é \33[0:32m{max(r)}\33[m nas posições ', end='')
for c, v in enumerate(r):
    if max(r) == v:
        print(f'{c}... ', end='')
print(f'\nO menor valor é \33[0:32m{min(r)}\33[m nas posições ', end='')
for c, v in enumerate(r):
    if min(r) == v:
        print(f'{c}... ', end='')