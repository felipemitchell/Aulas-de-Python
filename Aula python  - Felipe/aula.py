'''senha = input('Insira sua senha: ')
if senha == 'python123':
    print('acesso liberado')
else:
    print('Senha incorreta')'''

'''num = int(input("Insira um número: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")'''
'''idade = int(input("Digite sua idade: "))
if idade <= 12 :
    print("Criança")
elif idade <= 17 :
    print("Adolescente")
elif idade >= 60:
    print("Idoso")
else :
    print("Adulto")'''

'''i = 0
while i < 5:
    print(i)
    i+=1'''
'''x=1
while x <=3:
    print(x)
    x+=1'''
'''for letra in 'Python':
    print(letra)'''
'''n = 5
while n > 0 :
    print(n)
    n -= 1'''
'''for i in range(1,11,2):
    print(i)'''
#calculadora
'''numero = int(input("Insira um número: "))
for i in range(1,11):
    print(f'{numero} * {i} = {numero * i }')'''
#Tabuada 
'''numero = int(input("Insira um número: "))
for i in range(1, 11):
    calculo = numero * i
    print(f'{numero} x {i} = {calculo}')'''

# Média Escolar
'''nome = input("Insira seu nome: ")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

def soma (a,b):
    return a + b 

def media(nome, nota1, nota2):
    total = soma(nota1,nota2)
    m = total / 2
    situacao = "Aprovado" if m >= 7 else "Reprovado"
    print(f'{nome}: média {m:.2f} - {situacao}')
media(nome, nota1, nota2)'''