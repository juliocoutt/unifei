'''Faça um programa em Python que receba o valor de uma conta e um
percentual de desconto. Calcule o novo valor da conta ao ser aplicado o percentual de
desconto e escreva o resultado obtido.'''

valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

novo_valor = valor_conta - (valor_conta * percentual_desconto / 100)
print("O novo valor da conta é: R$", novo_valor)

