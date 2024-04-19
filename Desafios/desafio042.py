a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))
if a + b > c and a + c > b and a + c > a:
    print('\33[0:32mPode formar um Triângulo\33[m!!')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\33[0:31mNão pode formar um Triângulo\33[m!!')