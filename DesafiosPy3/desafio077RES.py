palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'PROGRAMAS EM PYTHON', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO', 'SCHOPENHAUER'

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end='')
