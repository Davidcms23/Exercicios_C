lista = []
pares = []
impar = []
while True:
    numero = int(input('Dígite um número: '))
    continua = ' '
    while continua not in 'SN':
        continua = input('Você quer continuar [S/N]? ').upper()
    if continua == 'N':
        break
    lista.append(numero)
    if numero%2 == 1:
        impar.append(numero)
    elif numero%2 == 0:
        pares.append(numero)
print(f'A sua lista é >>> {lista}')
print(f'Os números pares são >>> {pares}')
print(f'Os números impares são >>> {impar}')