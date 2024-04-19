numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'Dígite o {c+1}° número: '))
    if n%2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print(f'Os números pares são: {sorted(numeros[0])}\nOs números ímpares são: {sorted(numeros[1])}')