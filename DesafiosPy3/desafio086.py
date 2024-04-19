numeros = [[], [], [], [], [], [], [], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        numeros[l].insert(c, int(input(f'Dígite um valor para {[l, c]}: ')))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {numeros[l][c]:^5} ]', end='')
    print()
