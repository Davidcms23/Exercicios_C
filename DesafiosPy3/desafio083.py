e = input('Dígite uma expressão: ')
if e.count('(') == e.count(')'):
    cont = 0
    for n in e:
        if cont == -1:
            print('A expressão esta errada!!')
            cont += 10
        if n == '(':
            cont+=1
        elif n == ')':
            cont-=1
    if cont == 0:
        print('A expressão esta certo!!')
else:
    print('A expressão esta errada!!')