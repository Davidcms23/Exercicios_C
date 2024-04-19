lista = []
continua = ''
numero = ''
while True:
    numero = int(input('Dígite um número: '))
    while numero in lista:
        numero = int(input('\33[0:31mNúmero repetido\33[m, tente outro número: '))
    if numero not in lista:
        lista.append(numero)
    continua = input('Quer continuar [S/N]? ').upper()
    while continua not in 'SN':
        continua = input('Dígite uma resposta valida.\nQuer continuar [S/N]? ').upper()
    if continua == 'N':
        print(f'{sorted(lista)}')
        break
