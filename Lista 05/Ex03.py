"""Faça um programa que leia um nome e imprima somente as 4 primeiras letras do nome.
Em seguida, imprima as 4 últimas letras do nome. """


#ENTRADA 
nome= input("Qual o seu nome? \n").lstrip().rstrip() # Renovendo os espaços em branco no final ou inicio do nome. 

#PROCESSAMENTO e SAÍDA

print("As quatro primeiras letras do seu nome são: ",nome[:4])#selecionando as quatro primeira posições 

print("As quatro ultimas letras do seu nome são: ",nome[-4:]) #selecionando as quatro ultimas posições 

