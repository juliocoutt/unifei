''' 
Escreva um programa de MENU contendo as opções de (1=Inclusão,
2=Exclusão, 3=Consulta, 4=Relatório e 9=Sair). O programa só deve ser
finalizado quando o usuário digitar a opção 9=Sair
'''

opcao = ' ' #DEFININDO A VARIAVEL 


while opcao != '9': # CRIANDO O LOOP PARA QUE A CONDIÇÃO DE SAIDA SEJA RESPEITADA 

    # APRESENTANDO AO USUARIO A DEFINIÇÃO DO MENU 
    print ("Menu de Opções \n")
    print ("1 - Inclusão")
    print ("2 - Exclusão")
    print ("3 - Consulta")
    print ("4 - Relatório")
    print ("9 - Sair\n")
    opcao =  input("Escolha uma opção: \n")  # RECEBENDO DO USUARIO A OPÇÃO DESEJADA 

    # PROCESSAMENTO
    # NESTA ETAPA SERÁ FEITA A CONDICIONAL DENTRE AS OPÇÕES DO MENU E RETORNANDO AO CLIENR
    if opcao == '1':
        print ("Opção 1 : Você deseja fazer uma inclusão!\n")
    elif opcao == '2':
        print ("Opção 2 : Você deseja fazer uma Exclusão!\n")
    elif opcao == '3':
        print ("Opção 3 : Você deseja fazer uma Consulta!\n")
    elif opcao == '4':
        print ("Opção 4 : Você deseja fazer uma Relatorio!\n")

    elif opcao == '9': # APENAS QUANDO O USUARIO DIGITAR OPÇÃO 9 O PROGRAMA SERÁ ENCERRADO
        print ("Saindo do programa!\n")
    else:
        print ("Opcão invalida ! \n") # SEMPRE QUE A AOPÇÃO FOR DIFERENTE DAS OFERECIDAS NO MENU ESSA OPÇÃO SERÁ APRESENTADA. 
    
    
