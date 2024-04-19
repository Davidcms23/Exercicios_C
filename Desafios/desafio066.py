n = s = 0
while True:
    n = int(input('Dígite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos número dígitado é: {s}')