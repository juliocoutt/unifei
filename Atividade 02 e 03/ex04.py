'''
Faça um programa em Python que receba o valor de uma conta e um
percentual de desconto. Calcule o novo valor da conta ao ser aplicado, o
percentual de desconto e escreva o resultado obtido.
'''
#Entradas
valor_conta = float(input("Digite o valor da conta: "))
percentual_desconto = float(input("Digite o percentual de desconto: ")) 
#Processamento
#Calculo do desconto
#Calculo do valor final
desconto = valor_conta * percentual_desconto / 100
valor_final = valor_conta - desconto
#Saída
print("O valor da conta com desconto é: R$ ",(valor_final))
print("O desconto aplicado foi de: R$ ",(desconto)) 