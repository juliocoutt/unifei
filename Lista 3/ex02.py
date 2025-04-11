'''Faça um programa em Python que calcule a média de 4 (quatro) números. Caso
oresultado da média seja maior ou igual ao valor 60, imprima a mensagem
"AlunoAprovado". Caso contrário, imprima "Aluno Reprovado". '''

# Entrada
# O usuarios vai inserir os numeros solicitados 

n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
n3 = float (input("Digite o terceiro número: "))
n4 = float (input("Digite o quarto número: "))

#Processamento
# É feito o calculo da media de acordo com os dados dos usuarios inseridos
media = float (n1+n2+n3+n4)/4

#Saída
# Retorno para o usuario de acordo com a condiçãoes estabelicidas. 
if media >= 60:
    print ("Aluno Aprovado")
else:
    print("Aluno Reprovado.")