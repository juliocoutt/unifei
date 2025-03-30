'''
Faça um programa em Python que leia o número de eleitores de um
município, o número de votos em branco, nulos e válidos. Calcular e
escrever o percentual que cada um representa em relação ao total de
eleitores, isto é, o percentual de votos brancos, percentual de votos nulos e o
percentual de votos válidos.
'''
# Entradas
num_eleitores = int(input("Digite o número de eleitores: "))
votos_brancos = int(input("Digite o número de votos em branco: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))
# Processamento
percentual_brancos = (votos_brancos / num_eleitores) * 100
percentual_nulos = (votos_nulos / num_eleitores) * 100
percentual_validos = (votos_validos / num_eleitores) * 100
# Saída
print("O percentual de votos brancos é: ", percentual_brancos, "%")
print("O percentual de votos nulos é: ", percentual_nulos, "%")
print("O percentual de votos válidos é: ", percentual_validos, "%")


