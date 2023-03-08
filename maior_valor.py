valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')
if int(valor1) > int(valor2):
    print(f'{valor1} é maior que {valor2}')
elif int(valor2) > int(valor1):
    print(f'{valor2} é maior que {valor1}')
else: 
    print(f'{valor1} é igual a {valor2}')