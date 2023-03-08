def classificacao(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 35:
        return 'Obesidade grau 1'
    elif imc >= 35 and imc < 40:
        return 'Obesidade grau 2'
    elif imc >= 40:
        return 'Obesidade grau 3'

print('Calculadora IMC')
peso = float(input('\nDigite seu peso: '))
altura = float(input('\nDigite sua altura (em metros): '))
imc = peso/(altura*altura)
print('Seu IMC é ' + str(round(imc, 2)))
print('Seu resultado é: ' + classificacao(imc))
