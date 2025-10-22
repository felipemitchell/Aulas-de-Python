'''#questão 1 - calculando a média da prova
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

soma = nota1 + nota2 + nota3 
media = soma / 3

print(f'A média é: {media}')'''

#questão 2 par ou impar

'''num = int(input('Insira um número: '))
if num %2 == 0 :
    print(f'{num} é um número par.')
else: 
    print(f'{num} é um número ímpar. ')'''

#questão 2 +

'''lista = []
while len(lista) < 10 :
    num = int(input('Insira um número: '))
    lista.append(num)
for l in lista : 
    if l %2 == 0 :
        print(f'{l} é um número par')
    else :
        print(f'{l} é um número ímpar. ')'''

# questão 3 - loja de descontos 

'''valorProduto = float(input('Qual o valor do produto? \n R$ '))
if valorProduto > 100 and valorProduto <199 :
    valorFinal = valorProduto - (valorProduto*10)/100
    print(f'Você ganhou 10% de desconto \n Valor total: R$ {valorFinal}')
elif valorProduto > 200 and valorProduto < 299 :
    valorFinal = valorProduto - (valorProduto*20)/100
    print(f'Você ganhou 20% de desconto. \n Valor total: R$ {valorFinal}')
elif valorProduto > 300: 
    valorFinal = valorProduto - (valorProduto*30)/100
    print(f'Você ganhou 30% de desconto. \n Valor total: R$ {valorFinal}')
else:
    print('Você não obteve desconto.')'''

# questão 4 - conversor de tempo

'''minutos = int(input('Insira o tempo em minutos: '))
valorEmHoras = minutos // 60 
min = minutos % 60
print(f'{minutos} minutos é igual a {valorEmHoras} horas e {min} minutos16')'''

