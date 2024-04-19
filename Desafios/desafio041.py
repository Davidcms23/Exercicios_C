ano = int(input('Qual ano você nasceu? '))
from datetime import date
idade = date.today().year - ano
if idade <= 20:
    if idade <= 19:
        if idade <= 14:
            if idade <= 9:
                print('Você tem {} anos, se classifica na categoria \33[0:034mMIRIM\33[m'.format(idade))
        else:
            print('Você tem {} anos, se classifica na categoria \33[0:34mINFANTIL\33[m'.format(idade))
    else:
        print('Você tem {} anos, se classifica na categoria \33[0:34mSÊNIOR\33[m'.format(idade))
else:
    print('Você tem {} anos, se classifica na categoria \33[0:34mMASTER\33[m'.format(idade))