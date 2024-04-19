ano = int(input('Dígite que\33[0:31m ano\33[m você nasceu: '))

from datetime import date
data = date.today().year
idade = data - ano
if idade == 18 or idade == 17:
    print('Esta na Hora de se alistar,')
elif idade >= 19:
    print('Ja passou da hora de se alistar,')
    print('Você esta {} ano(s) atrasado'.format(idade-18))
else:
    print('Ainda não chegou a hora,')
    idade = idade - 18
    print('Ainda faltam {} ano(s)'.format(abs(idade)))