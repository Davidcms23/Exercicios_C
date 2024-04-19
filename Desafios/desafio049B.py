from time import sleep
m = 1
while True:
    for c in range(1, 11):
        print('{} x {} = {}'.format(c, m, c * m))
        sleep(0.3)
    m = m + 1
    s = c * m
    if s == 110:
        print('\33[0:32mFIM\33[m')
        break
