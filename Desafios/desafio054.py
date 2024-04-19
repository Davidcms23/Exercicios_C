from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = data - ano
    if idade >= 18:
        maior += 1
    elif idade <= 17:
        menor += 1
print('Existem {} pessoas maiores de idade e {} menores de idade!!'.format(maior, menor))


