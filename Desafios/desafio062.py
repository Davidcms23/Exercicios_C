n1 = int(input('Qual o primeiro termo: '))
n2 = int(input('Razão da PA: '))
r = 11
total = 0
while r >= 1:
    print('{} -> '.format(n1), end='')
    total += 1
    n1 = n1 + n2
    r -= 1
    if r == 1:
        print('PAUSA')
        p = int(input('Quantos termos você quer mostrar a mais? '))
        if p >= 1:
            r = p + 1
        elif p == 0:
            break
print('Progressão finalizada com \33[0:32m{}\33[m termos.'.format(total))