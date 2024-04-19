a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if c + b > a and a + b > c and a + c > b:
    pode = print('pode formar um triângulo')
else:
    print('Não pode formar um triângulo')