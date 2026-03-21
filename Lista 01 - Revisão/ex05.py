"""Escreva um programa em python utilizando os comandos (entrada e saida de dados, estruturas
condicional e de repetição), que imprima na tela um MENU contendo as seguintes opções:
1=Incluir usuário
2=Excluir usuario
3=Consultar usuário
4=Alterar usuário
5=Listar todos os usuários que estão cadastrados
9=Sair.
Funcionalidades necessárias:
a) o programa só deve ser finalizado quando o usuário digitar a opção 9=Sair;
b) caso o usuário digitar as demais opções, deverá ser impresso o número e nome da opção e
em seguida finalizar o programa
c) caso o usuário digite alguma opção não prevista, deverá ser impresso uma mensagem de
opção inválida e o programa não poderá ser finalizado.
"""
# Loop principal do programa
while True:
    # Exibe o menu de opções
    print("\nMENU:")
    print("1 = Incluir usuário")
    print("2 = Excluir usuário")
    print("3 = Consultar usuário")
    print("4 = Alterar usuário")
    print("5 = Listar todos os usuários que estão cadastrados")
    print("9 = Sair")

    # Solicita ao usuário a opção desejada
    opcao = input("Digite a opção desejada: ")

    # Verifica a opção escolhida
    if opcao == '1':
        print("Opção 1: Incluir usuário")
        break
    elif opcao == '2':
        print("Opção 2: Excluir usuário")
        break
    elif opcao == '3':
        print("Opção 3: Consultar usuário")
        break
    elif opcao == '4':
        print("Opção 4: Alterar usuário")
        break
    elif opcao == '5':
        print("Opção 5: Listar todos os usuários que estão cadastrados")
        break
    elif opcao == '9':
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")