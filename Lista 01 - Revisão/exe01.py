'''Faça um programa em Python que receba o valor de uma conta e um percentual de desconto.
Calcule o novo valor da conta ao ser aplicado o percentual de desconto e escreva o resultado
obtido.'''

# Recebe o valor da conta e o percentual de desconto
valor_conta = float(input("Digite o valor da conta: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
# Calcula o valor do desconto
valor_desconto = valor_conta * (percentual_desconto / 100)
# Calcula o novo valor da conta após aplicar o desconto
novo_valor_conta = valor_conta - valor_desconto
# Exibe o resultado
print(f"O novo valor da conta após aplicar o desconto é: R$ {novo_valor_conta:.2f}")