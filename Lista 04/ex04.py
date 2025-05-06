""" Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse
número, somente a multiplicação."""

numero = int(input("Digite um número de 1 a 10")) # USUARIO ENTRA COM O NUMERO  E CONVERTO PARA INTEIRO

if numero >= 1 and numero<=10 : # CONDICIONAL PARA GARANTIR QUE O NÚMERO ESTÁ DENTRO DO INTERVALO NECESSARIO
    cont = 1 # INICIANDO O CONTATO PARA QUE O MESMO ASSUMA O VALOR DENTRO DO LOOP, ONDE ELE SERÁ USADO COM MULTIPLICADOR
    while cont <= 10: #GARANTO QUE QUANDO CHEGAR A 10 O LOOP SERÁ ENCERRADO.

        # APRESENTANDO AO USUARIO O RESULTADO
        # STR PARA CONVERTER EM STRING E E APRESENTAR O USUARIO COCATENADO
    
        print(str(numero) + " x " + str(cont) + " = " + str(numero * cont)) 
        cont+=1 # ACRESCENTANDO + 1 A CADA LOOP EXEXUTADO 
else:
    print("Numero invalido !") # CASO O USUARIO DIGITE UM NUMERO FORA DO INTERVALO.