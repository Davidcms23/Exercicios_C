palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'PROGRAMAS EM PYTHON', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO', 'SCHOPENHAUER'
letras = 'A', 'E', 'I', 'O', 'U'
cont = 0

for a in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[cont]} temos ', end='')
    l = 0
    for b in range(0, len(letras)):
        lp = 0
        for c in range(0, len(palavras[cont])):
            if letras[l] == palavras[cont][lp]:
                print(palavras[cont][lp], end=' ')
            lp += 1
        l += 1
    cont += 1