'''Faça um programa que receba uma palavra e a imprima de trás-para-frente '''

#ENTRADA

palavra = input ("Digite uma palavra: \n ")

inverso = palavra[::-1] #usando A sintaxe palavra[start:stop:step] é o fatiamento (slicing) de strings em Python.


#SAIDA
print(inverso)