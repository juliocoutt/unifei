''' 

Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números negativos.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números pares.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção___

'''

#ENTRADA
print (" \n ******* Menu de Opções ******* \n\n 1- Soma de 2 números negativos \n 2- Diferença entre 2 números (maior pelo menor).\n 3- Produto entre 2 números pares. \n 4- Divisão entre 2 números (o denominador não pode ser zero). \n \n ")
opcao = int(input("Opção : "))

resultado= float(0)
#PROCESSAMENTO  E SAÍDA 
if opcao >= 1 and opcao <= 4:   

    n1= float(input("Digite o primeito numero"))
    n2= float(input("Digite o segundo numero")) 

    if opcao == 1:  

        if (n1 < 0 and n2 < 0):
            resultado = n1 + n2
            print(f"O resultado da operação é = {resultado}")
        else:
            print("Um dos numeros foi digitado incorretamente")

    elif opcao == 2:

        if (n1>n2):
            resultado= n1 - n2
            print(f"O resultado da operação é = {resultado}")
        else:
            resultado= n2- n1
            print(f"O resultado da operação é = {resultado}")

    elif opcao == 3: 

        resultado= n1 * n2
        print(f"O resultado da operação é = {resultado}")

    elif opcao == 4: 
        if ( n2 > 0):
            resultado = n1 / n2
            print(f"O resultado da operação é = {resultado}")
        else:
            print("Denominador não pode ser igual ou menor que zero")

else:
    print("Opção Invalida \n")