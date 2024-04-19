peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}'.format(imc))
if imc <= 18.4:
    print('Você esta abaixo do peso!!')
elif imc >= 18.5:
    if imc >= 24.9:
        if imc >= 29.9:
            if imc >= 34.9:
                if imc >= 39.9:
                    if imc >= 40:
                        print('\33[0:370:41mObesidade Morbida(Você vai morrer!!)\33[m')
                else:
                    print('\33[0:31mObesidade Grau Dois\33[m!!')
            else:
                print('\33[0:33mObesidade Grau Um!!\33[m')
        else:
            print('\33[0:30mPeso em pré-obesidade ou acima do peso!!\33[m')
    else:
        print('\33[0:32mVocê esta com o peso normal!!\33[m')