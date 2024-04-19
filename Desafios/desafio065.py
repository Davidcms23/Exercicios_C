cont = 0
maior = 0
menor = 999
soma = 0
s = 'S'
while s == 'S':
    r = int(input('Dígite um número: '))
    s = input('Quer continuar [S/N]: ').upper()
    cont += 1
    soma += r
    if r > maior:
        maior = r
    elif r < menor:
        menor = r
    elif s == 'N':
        break
    else:
        break
print('\33[0:32mVocê dígitou {} números, a média é de {}.\nO maior número é {} e O menor número é {}\33[m.'.format(cont, soma // cont, maior, menor))