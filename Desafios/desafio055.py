g = 0
m = 0
grupo = []
for c in range(1, 6):
    peso = float(input('Dígite o peso da {}° pessoa: '.format(c)))
    grupo += [peso]
print('O maior peso é: {}kg\nO menor peso é: {}kg'.format(max(grupo), min(grupo)))
