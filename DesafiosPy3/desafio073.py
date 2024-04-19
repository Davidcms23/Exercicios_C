times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Internacional', 'Fluminense',
         'Atlético-GO', 'Cuiabá', 'Ceará', 'São Paulo', 'América-MG', 'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print(len(times))
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 colocados são: {times[16:21]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}° posição')