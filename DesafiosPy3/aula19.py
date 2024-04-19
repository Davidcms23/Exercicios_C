lista = [] #Lista
pessoa = {} #Dicionario
while True:
    pessoa['Nome'] = [input('Nome: ')]
    pessoa['Idade'] = [int(input('Idade: '))]
    lista.append(pessoa.copy())
    continua = input('Continua? S/N: ').upper()
    if continua == 'N':
        break
print('-'*30)
for p in lista:
    for k, v in pessoa.items():
        print(f'{k}: {v} ')
    print('-' * 30)