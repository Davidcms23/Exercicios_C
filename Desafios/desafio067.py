cont = 0
while True:
    n = int(input('Quer ve a tabuada de que número? '))
    print('=-' * 20)
    if n <= -1:
        break
    for c in range(0, 10):
        cont += 1
        print(f'{n} x {cont} = {n*cont}')
    print('=-' * 20)
