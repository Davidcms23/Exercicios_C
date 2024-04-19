matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].insert(c, int(input(f'Dígite um valor para {[l, c]}: ')))
pares = 0
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c]%2 == 0:
            pares += matriz[l][c]
        if l == 2:
            soma += matriz[l][c]
    print()
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira linha é: {soma}')
print(f'O maior valor da segundo linha é: {max(matriz[1])}')