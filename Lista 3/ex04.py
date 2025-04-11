'''
Faça um programa em Python que recebe o NOME e o PREÇO de um produto. Casoo
PREÇO informado seja maior do que 100,00 calcule um desconto de 25% e imprima
oNOME e PREÇO-COM-DESCONTO e a frase "Desconto de 25%.". Caso
contrário,calcule um desconto de 15% e imprima o NOME, PREÇO-COM-DESCONTO
e a frase"Desconto de 15%." 
'''

#Entrada

nome = str(input("NOME DO PRODUTO: "))
preco = float (input("Preço do produto em R$: "))

#Processamento

precoDesconto = float (0) #deixando a variavel de desconto zerada

if preco > 100: #comparando se o preço do item é mais que R$ 100 e realizando o calculo do percentual
    precoDesconto = preco - (preco*0.25) # calculo do preço com desconto
    print(f"Nome do Produto {nome}") # apresentando o nome do produto
    print("Desconto de 25 %.")
    print (f"R$ {precoDesconto}") # mostrando preço para p usuario 

# caso o preço seja seja menor ou igual a R$ 100 ele entra nessa segunda sentença. 
elif preco <= 100:
    precoDesconto = preco - (preco*0.15)
    print(f"Nome do Produto {nome}")
    print("Desconto de 15 %.")
    print (f"R$ {precoDesconto}")