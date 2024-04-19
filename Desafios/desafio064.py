a = 0
while True:
    n = int(input('Dígite um número[999 pra PARAR]: '))
    if n != 999:
        a += n
    elif n == 999:
        print('=-='*10)
        break
print('A soma dos número dígitados é:\33[0:32m {}\33[m'.format(a))