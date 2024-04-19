valor = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário atual: '))
anos = int(input('Em quantos anos você pretende pagar: '))

pres = valor / (anos * 12)
n = (salario * 30) / 100

if n < pres:
    print('Você não pode financiar essa casa!!')
else:
    print('Você pagara {:.2f} por mês'.format(pres))
    print('{:.2f}'.format(pres))