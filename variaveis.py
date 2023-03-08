nome = input("Digite seu primeiro nome:") 
sobrenome = input("Digite seu sobrenome:") 
idade = input("Digite sua idade:") 
altura = input("Digite sua altura:") 
peso = input("Digite seu peso:") 

if int(idade) >= 18 : 
    maior = 'sim' 
else:
    maior = 'não'

print(f"Nome: {nome} {sobrenome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}\nMaior de idade: {maior}")