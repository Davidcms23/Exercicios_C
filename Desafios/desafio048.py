for c in range(1, 501):
    a = c % 3
    if a == 0:
        r = c // 3
        print('\33[0:32m{} % 3 = {}\33[m'.format(c, r))