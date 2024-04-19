n1 = float(input('Dígite a primeita nota: '))
n2 = float(input('Dígite a segunda nota: '))

m = (n1 + n2) / 2
print('Sua média é: {:.2f}'.format(m))
if m <= 4.9:
    print('\33[0:31mREPROVADO\33[m')
elif m >= 5:
    if m <= 6.9:
        print('\33[0:33mRECUPERAÇÃO\33[m')
    else:
        print('\33[0:32mAPROVADO\33[m')