'''Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em
maiúscula e sem espaços em branco. '''

#ENTRADA 


frase= input("Digite uma frase por gentileza: ")

#PROCESSAMENTO 
# Faço uso das 3 funções para fazer a substituição dos espaços e conversão para maiosuculo 
frase = frase.strip().upper().replace(" ","")

#SAIDA 

print("A frase convertida é: \n",frase)