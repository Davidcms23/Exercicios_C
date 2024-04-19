while True:
    numero = int(input('Dígite um número entre 0 e 20: '))
    numero_extenso = 'Zero', 'Um', 'Dois', 'Trê', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Once', 'Doze', 'Treze', 'Quatorze', 'Treze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezeoito', 'Dezenove', 'Vinte'
    continua = ' '
    while numero >= 21 or numero <= -1:
        numero = int(input('Tente novamente, Dígite um número entre 0 e 20: '))
    print(f'Você dígitou o número \33[0:32m{numero_extenso[numero+1]}\33[m')
    while continua not in 'SN':
        continua = input('Você quer continuar [S/N}? ').strip().upper()
    if continua == 'N':
        break