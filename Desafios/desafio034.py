s = float(input('Dígite o Salário: ').strip())
maior = s * 15 / 100
menor = s * 10 / 100
if s <= 1250:
    print('Seu salário agora é {}'.format(int(s + maior)))
else:
    print('Seu salároi agora é {}'.format(s + menor))