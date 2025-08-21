'''Escreva um programa de MENU contendo as opções:
1=Incluir usuário,
2=Excluir usuário
3=Consultar usuário
4=Alterar usuário
5=Listar todos os usuários que estão cadastrado
9=Sair.
É necessário que o programa tenha as seguintes funcionalidades:
1) O programa só deve ser finalizado quando o usuário digitar a opção 9=Sair
2) Utilizar todos recursos de programação (estruturas condicional e de repetição)
aprendidos até momento, em especial a manipulação de Listas, para armazenar os
dados.
3) Deve-se habilitar para as opções do MENU para que sejam preenchidos no
mínimo os seguintes campos:
NOME COMPLETO
CPF
TELEFONE
E-MAIL
DATA DE NASCIMENTO
4) Todos os campos devem ser validados conforme o tipo de dado (string, inteiro
e etc.) que são esperados. Ou seja, caso seja informado pelo usuário do sistema
um valor inadequado, o programa de vocês deve criticar informando uma mensagem para o usuário e barrar este tipo de informação inadequada.'''

usuarios = []
def incluir_usuario(): # Função para incluir um novo usuário
    nome = input("Digite o nome completo: ")
    cpf = input("Digite o CPF (apenas números): ")
    telefone = input("Digite o telefone (apenas números): ")
    email = input("Digite o e-mail: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")

    usuario = {# Dicionário para armazenar os dados do usuário
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email,
        "data_nascimento": data_nascimento
    }
    
    usuarios.append(usuario) # Adiciona o usuário à lista de usuários
    # Validação de inclusão
    print("Usuário incluído com sucesso!")


def excluir_usuario(): # Função para excluir um usuário
    cpf = input("Digite o CPF do usuário a ser excluído: ") # Solicita o CPF do usuário a ser excluído
    if not cpf.isdigit() or len(cpf) != 11: # Valida se o CPF é numérico e tem 11 dígitos
        print("CPF inválido. Deve conter apenas números e ter 11 dígitos.")
        return
    for usuario in usuarios:    # Percorre a lista de usuários
        if usuario["cpf"] == cpf:
            usuarios.remove(usuario)
            print("Usuário excluído com sucesso!")
            return
    print("Usuário não encontrado.")   

# Função para consultar um usuário pelo CPF
def consultar_usuario():
    cpf = input("Digite o CPF do usuário a ser consultado: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Telefone: {usuario['telefone']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            return
    print("Usuário não encontrado.")

# Função para alterar os dados de um usuário
def alterar_usuario():
    cpf = input("Digite o CPF do usuário a ser alterado: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            nome = input("Digite o novo nome completo: ")
            telefone = input("Digite o novo telefone (apenas números): ")
            email = input("Digite o novo e-mail: ")
            data_nascimento = input("Digite a nova data de nascimento (DD/MM/AAAA): ")

            usuario["nome"] = nome
            usuario["telefone"] = telefone
            usuario["email"] = email
            usuario["data_nascimento"] = data_nascimento
            
            print("Usuário alterado com sucesso!")
            return
    print("Usuário não encontrado.")

# Função para listar todos os usuários cadastrados
def listar_usuarios(): 
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Telefone: {usuario['telefone']}, E-mail: {usuario['email']}, Data de Nascimento: {usuario['data_nascimento']}")

# Função para exibir o menu e gerenciar as opções
def menu():
    while True:
        print("\nMENU:")
        print("1 - Incluir usuário")
        print("2 - Excluir usuário")
        print("3 - Consultar usuário")
        print("4 - Alterar usuário")
        print("5 - Listar todos os usuários cadastrados")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_usuario()
        elif opcao == '2':
            excluir_usuario()
        elif opcao == '3':
            consultar_usuario()
        elif opcao == '4':
            alterar_usuario()
        elif opcao == '5':
            listar_usuarios()
        elif opcao == '9':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()

