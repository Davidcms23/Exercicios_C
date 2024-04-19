print('='*40)
print('{:^20}MERCADO SUPER BARATÃO')
print('='*40)
valor_total = 0
caro = 0
barato = 999
nome_barato = ''
sair = ' '
while True:
    nome = input('Nome do produto: ')
    valor_produto = int(input('Valor do produto: R$'))
    while sair not in 'SN':
        sair = input('Quer Sair [S/N]' ).strip().upper()[0]
    valor_total += valor_produto
    if valor_produto > 1000:
        caro += 1
    elif barato > valor_produto:
        barato = valor_produto
        nome_barato = nome
    if sair == 'S':
        break

print(f'Valor total da compra: \33[0:32m{valor_total}\33[m\nQuantos produtos custam mais de R$1000: \33[0:32m{caro}\33[m\nQual o nome do produto mais barato: \33[0:32m{nome_barato}\33[m')


