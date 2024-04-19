pessoas = {}
pessoas['Nome'] = [input('Nome: ')]
pessoas['Media'] = [float(input('Media: '))]
for c in pessoas.keys():
    print(f'{c.strip()} ', end='')
palavras = pessoas['Nome']
palavras = palavras.strip('""')
print(palavras)