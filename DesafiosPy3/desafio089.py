continua = ''
alunos = []
n = 0
while True:
    alunos.append([str(input('Nome: '))])
    for c in range(0, 2):
        r = float(input(f'Nota {c+1}: '))
        alunos[n].insert(c+1, r)
    n += 1
    continua = str(input('Você quer continuar? S/N: ')).upper()
    while continua not in 'SN':
        continua = str(input('Você quer continuar? S/N: ')).upper()
    if continua == 'N':
        break
print('='*30)
print(f'{"No.":<} {"NOME":<5} {"MÉDIA":>15}')
print('-'*30)
for c in range(0, len(alunos)):
    media = (alunos[c][1]+alunos[c][2]) / 2
    print(f'{c:<}   {alunos[c][0]:<5} {media:>15.2f}')
while True:
    r = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    print(f'Notas de {alunos[r][0]} são {alunos[r][1]} e {alunos[r][2]}!!!')
    if r == 999:
        print('Finalizando...')
        break
