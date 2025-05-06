"""Escreva um programa para encontrar a soma S = 3 + 6 + 9 +…. + 333."""

soma = 0 #zerando a variavel

for i in range (3,334,3): # coloquei o limite em 334 para garantir que o 333 entre na conta.
    soma += i 
print ("Soma: ", soma)