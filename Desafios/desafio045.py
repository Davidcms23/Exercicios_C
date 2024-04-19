print('Escolha uma das opções abaixo: \nPEDRA\nPAPEL\nTESOURA')
p = 0
pc = 0
print('\33[0:32mSeus pontos: {}\33[m\n\33[0:31mPontos do NPC: {}\33[m'.format(p, pc))
while True:
    r = input('Qual a sua Escolha? ')
    import random
    from time import sleep
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    a = ('PEDRA', 'PAPEL', 'TESOURA')
    a = random.choice(a)
    r = r.upper()
    print('Eu escolhi {}'.format(a))

    #Pedra
    if r == 'PEDRA':
        if a == 'TESOURA':
            p = p + 1
            print('\33[0:34mVocê Ganhou!!\33[m')
        else:
            print('\33[0:33mVocê errou, tente novamente!\33[m')
            pc = pc + 1
        print('-=' * 11)
        print('\33[0:32mSeus pontos: {}\33[m\n\33[0:31mPontos do NPC: {}\33[m'.format(p, pc))
        print('-=' * 11)
    #Tesoura
    elif r == 'TESOURA':
        if a == 'PAPEL':
            p = p + 1
            print('\33[0:34mVocê Ganhou!!\33[m')
        else:
            print('\33[0:33mVocê errou, tente novamente!\33[m')
            pc = pc + 1
        print('-=' * 11)
        print('\33[0:32mSeus pontos: {}\33[m\n\33[0:31mPontos do NPC: {}\33[m'.format(p, pc))
        print('-=' * 11)

    #Papel
    elif r == 'PAPEL':
        if a == 'PEDRA':
            p = p + 1
            print('\33[0:34mVocê Ganhou!!\33[m')
        else:
            print('\33[0:33mVocê errou, tente novamente!\33[m')
            pc = pc + 1
        print('-=' * 11)
        print('\33[0:32mSeus pontos: {}\33[m\n\33[0:31mPontos do NPC: {}\33[m'.format(p, pc))
        print('-=' * 11)

    #Sair
    elif r == '0':
        print('saindo...')
        break
    else:
        print('\33[0:33mEscolha uma das Opções!\33[m')
        pc = pc + 1
        print('-=' * 11)
        print('\33[0:32mSeus pontos: {}\33[m\n\33[0:31mPontos do NPC: {}\33[m'.format(p, pc))
        print('-=' * 11)