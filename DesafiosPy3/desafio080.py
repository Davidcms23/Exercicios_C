lista = []
for n in range(0, 5):
    numero = int(input('Dígite um número: '))
    if n == 0 or numero >= lista[-1]:
        lista.append(numero)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while True:
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(lista)