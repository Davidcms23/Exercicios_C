valor = float(input('Dígite o valor a ser pago: '))
print('[1]Á vista(Dinheiro/Cheque)\n[2]Á vista(Cartão)\n[3]Em até 2x no cartão\n[4]3x ou mais no cartão')
c = int(input('\33[0:31mEscolha uma das opiçoes acima: 1, 2, 3 ou 4\33[m\nQual a condição de pagamento? '))
if c == 1:
    valor = valor - (valor / 100 * 10)
    print('\33[0:32mDesconto de 10%\33[m\nValor a ser pago: {:.2f}'.format(valor))
elif c == 2:
    valor = valor - (valor / 100 * 5)
    print('\33[0:32mDesconto de 15%\33[m\nValor a ser pago: {:.2f}'.format(valor))
elif c == 3:
    print('Valor a ser pago: {:.2f}'.format(valor))
else:
    valor = valor + (valor / 100 * 20)
    print('\33[0:31m20% de Juros\33[m\nValor total a ser pago: {}'.format(valor))