a = input('Dígite algo: ')
print('[1] Converter para \33[0:31mBINARIO \33[m\n[2] Converter para \33[0:32mOCTAL \33[m\n[3] Converter para \33[0:33mHEXADECIMAL\33[m')
r = input('Escolha uma das opções: ')
if r == '1':
    print('\33[0:31mBINARIO\33[m: {}'.format(format(int(a), 'b')))
elif r == '2':
    print('\33[0:32mOCTAL\33[m: {}'.format(format(int(a), 'o')))
elif r == '3':
    print('\33[0:33mHEXADECIMAL\33[m: {}'.format(format(int(a), 'x')))