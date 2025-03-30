'''
Faça um programa em Python que receba o valor de um salário e um
percentual de reajuste. Calcule o valor do novo salário reajustado.
'''

# Entradas
salario = float(input("Digite o valor do salário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

# Processamento
novo_salario = salario + (salario * percentual_reajuste / 100)
# Saída
print("O novo salário reajustado é: R$ ", novo_salario)
print("O percentual de reajuste aplicado foi de: ", percentual_reajuste, "%")
print("O valor do salário original era: R$ ", salario)
print("O valor do reajuste aplicado foi de: R$ ", (novo_salario - salario))
# Fim do programa