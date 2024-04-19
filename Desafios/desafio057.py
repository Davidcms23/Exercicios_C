while True:
    n = input('Escolha uma das opções\nM/F: ').upper()
    if n == 'M' or n == 'F':
        print('Obrigado!!')
        if n == 'M':
            print('Parece que você é homem. ')
        else:
            print('Parece que você quer ser mulher')
        break
    else:
        print('Faça oque eu estou pedindo.')