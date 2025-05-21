'''Faça um programa que leia um nome, calcule e imprima a quantidade letras que tem esse
nome. '''

#ENTRADA

nome= input("Digite seu nome por favor: \n").replace(" ","") #removendo os espaços me branco caso o usuaio digite o nome completo 

#SAÍDA E PROCESSAMENTO
print(len(nome))