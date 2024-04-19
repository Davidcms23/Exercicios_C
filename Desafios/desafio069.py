print('-'*20)
print('CADASTRAR')
print('-'*20)
cont_idade = 0
cont_homem = 0
cont_moça = 0
print('=-' * 20)
while True:
    sex = ' '
    sair = ' '
    idade = int(input('Idade: '))
    while sex not in 'MF':
        sex = input('Sexo [F/M]: ').strip().upper()[0]
    while sair not in 'SN':
        sair = input('Quer Continuar [S/N]? ').strip().upper()[0]
    print('=-' * 20)
    if idade >= 18:
        cont_idade += 1
    elif sex == 'M':
        cont_homem += 1
    elif sex == 'F':
        if idade < 20:
            cont_moça += 1
    if sair == 'N':
        break
print(f'Temos {cont_idade} pessoas maiores de 18 anos,\nTemos {cont_homem} homen(s) e {cont_moça} mulher(es) menores de 20 anos')
