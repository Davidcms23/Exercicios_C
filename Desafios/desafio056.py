"""No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
"""A MÉDIA"""
media = 0

"""VELHO"""
idade_velho = []
velho = '' #Nome do velho
vidade = 0 #Idade do velho

"""JOVEM"""
jovem = 0

for c in range(1, 5):
    nome = input('Dígite o seu nome: ')
    idade = int(input('Dígite a sua idade: '))
    genero = input('[M] para masculino ou [F] para feminino: ').upper()
    media += idade
    idade_velho += [idade]
    if idade > vidade:
        vidade = idade
        velho = nome
    if genero == 'F':
        if idade <= 19:
            jovem += 1
print('-'*50)
print('A média de idade do grupo é de: \33[0:32m{}\33[m anos'.format(media // 4))
print('O nome do homem mais velho é: \33[0:32m{}\33[m ({} anos)'.format(velho.capitalize(), max(idade_velho)))
print('Existem \33[0:32m{}\33[m Mulheres menores de 20 anos'.format(jovem))
print('-'*50)