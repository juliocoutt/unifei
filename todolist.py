"""Sistema de Gerenciamento de Tarefas Pessoais (To-Do List Avançada):
•	Funcionalidades: 
o	Inclusão: Adicionar novas tarefas (descrição, data de vencimento, prioridade, categoria, status - pendente/concluída).
o	Exclusão: Deletar tarefas.
o	Consulta: Visualizar tarefas por data, prioridade, categoria; filtrar por status.
o	Alteração: Marcar tarefa como concluída, alterar descrição, data, prioridade.
•	Por que é bom: Simples de entender, mas permite expansões interessantes (lembretes, subtarefas, projetos). Ótimo para praticar o gerenciamento de estados.


"""

# Lista para armazenar as tarefas e um contador para o ID único
tarefas = []
proximo_id = 1

def incluir_tarefa():
    """Função para incluir uma nova tarefa."""
    global proximo_id  # Informa que usaremos a variável global

    print("\n--- Adicionar Nova Tarefa ---") # Exibe o título da seção
    # Solicita os dados da tarefa ao usuário
    descricao = input("Descrição da tarefa: ")
    data_vencimento = input("Data de vencimento (DD/MM/AAAA): ")
    prioridade = input("Prioridade (Ex: Alta, Média, Baixa): ")
    categoria = input("Categoria (Ex: Trabalho, Estudo, Pessoal): ")

    # Cria o dicionário da tarefa
    tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "data_vencimento": data_vencimento,
        "prioridade": prioridade,
        "categoria": categoria,
        "status": "Pendente"  # Nova tarefa sempre começa como pendente
    }
    
    tarefas.append(tarefa)  # Adiciona a tarefa à lista
    proximo_id += 1  # Incrementa o ID para a próxima tarefa
    
    print("\n✅ Tarefa incluída com sucesso!")


def listar_tarefas_para_selecao(): # Função auxiliar para listar tarefas com IDs antes de uma ação
    """Função auxiliar para listar tarefas com seus IDs antes de uma ação."""
    if not tarefas: # Verifica se há tarefas cadastradas
        print("\n Nenhuma tarefa cadastrada.")
        return False
    
    print("\n--- Tarefas Cadastradas ---") # Exibe as tarefas cadastradas
    for t in tarefas:
        print(f"ID: {t['id']} | Descrição: {t['descricao']} | Status: {t['status']}")
    print("--------------------------")
    return True

def excluir_tarefa():
    """Função para excluir uma tarefa pelo seu ID."""
    if not listar_tarefas_para_selecao():
        return

    try:
        id_excluir = int(input("Digite o ID da tarefa que deseja excluir: ")) # Solicita o ID da tarefa a ser excluída
        
        tarefa_encontrada = None # Variável para armazenar a tarefa encontrada
        # Percorre a lista de tarefas para encontrar a tarefa com o ID fornecido
        for tarefa in tarefas:
            if tarefa["id"] == id_excluir:
                tarefa_encontrada = tarefa
                break
        
        if tarefa_encontrada: # Verifica se a tarefa foi encontrada
            tarefas.remove(tarefa_encontrada)
            print("\n Tarefa excluída com sucesso!")
        else:
            print("\n ID não encontrado.")
            
    except ValueError: # Captura erro se o usuário não digitar um número
        print("\n ID inválido. Por favor, digite um número.")


def alterar_tarefa():
    """Função para alterar os dados de uma tarefa ou marcá-la como concluída."""
    if not listar_tarefas_para_selecao(): # Verifica se há tarefas para alterar
        return # Não há tarefas para alterar

    try: # Solicita o ID da tarefa a ser alterada
        id_alterar = int(input("Digite o ID da tarefa que deseja alterar: "))
        
        tarefa_para_alterar = None # Variável para armazenar a tarefa a ser alterada
        # Percorre a lista de tarefas para encontrar a tarefa com o ID fornecido
        for t in tarefas:
            if t['id'] == id_alterar:
                tarefa_para_alterar = t
                break
# Verifica se a tarefa foi encontrada
        # Se não encontrar, informa ao usuário
        if not tarefa_para_alterar:
            print("\n ID não encontrado.")
            return

        print("\nO que você deseja alterar?")
        print("1 - Marcar como Concluída")
        print("2 - Alterar Descrição")
        print("3 - Alterar Data de Vencimento")
        print("4 - Alterar Prioridade")
        print("5 - Alterar Categoria")
        
        opcao = input("Escolha uma opção: ") # Solicita a opção de alteração

        if opcao == '1':
            tarefa_para_alterar['status'] = 'Concluída'
            print("\n Status da tarefa alterado para 'Concluída'!")
        elif opcao == '2':
            tarefa_para_alterar['descricao'] = input("Nova descrição: ")
            print("\n Descrição alterada com sucesso!")
        elif opcao == '3':
            tarefa_para_alterar['data_vencimento'] = input("Nova data (DD/MM/AAAA): ")
            print("\n Data alterada com sucesso!")
        elif opcao == '4':
            tarefa_para_alterar['prioridade'] = input("Nova prioridade: ")
            print("\n Prioridade alterada com sucesso!")
        elif opcao == '5':
            tarefa_para_alterar['categoria'] = input("Nova categoria: ")
            print("\n Categoria alterada com sucesso!")
        else:
            print("\n Opção inválida.")

    except ValueError:
        print("\n ID inválido. Por favor, digite um número.") # Captura erro se o usuário não digitar um número

def consultar_tarefas():
    """Função para visualizar tarefas com filtros."""
    if not tarefas: # Verifica se há tarefas cadastradas
        # Se não houver tarefas, informa ao usuário
        print("\nℹ Nenhuma tarefa cadastrada para consultar.")
        return
        
    print("\n--- Consultar Tarefas ---")
    print("1 - Listar todas as tarefas")
    print("2 - Filtrar por status (Pendente/Concluída)")
    print("3 - Filtrar por prioridade")
    print("4 - Filtrar por categoria")
    # Solicita a opção de consulta
    opcao = input("Escolha uma opção: ")
    
    resultados = [] # Lista para armazenar os resultados da consulta
    # Dependendo da opção escolhida, filtra as tarefas
    
    if opcao == '1':
        resultados = tarefas
    elif opcao == '2':
        filtro_status = input("Digite o status (Pendente ou Concluída): ").capitalize()
        resultados = [t for t in tarefas if t['status'] == filtro_status]
    elif opcao == '3':
        filtro_prioridade = input("Digite a prioridade: ").capitalize()
        resultados = [t for t in tarefas if t['prioridade'].capitalize() == filtro_prioridade]
    elif opcao == '4':
        filtro_categoria = input("Digite a categoria: ").capitalize()
        resultados = [t for t in tarefas if t['categoria'].capitalize() == filtro_categoria]
    else:
        print("\n Opção inválida.")
        return

    if not resultados:
        print("\nℹ Nenhuma tarefa encontrada com este critério.")
    else:
        print("\n--- Resultados da Consulta ---")
        for t in resultados:
            print(f"ID: {t['id']}, Descrição: {t['descricao']}, Vencimento: {t['data_vencimento']}, "
                  f"Prioridade: {t['prioridade']}, Categoria: {t['categoria']}, Status: {t['status']}")
        print("-----------------------------")


def menu():
    """Função para exibir o menu e gerenciar as opções."""
    while True:
        print("\n========== MENU DE TAREFAS ==========")
        print("1 - Incluir Tarefa")
        print("2 - Alterar Tarefa")
        print("3 - Excluir Tarefa")
        print("4 - Consultar / Listar Tarefas")
        print("9 - Sair do Programa")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_tarefa()
        elif opcao == '2':
            alterar_tarefa()
        elif opcao == '3':
            excluir_tarefa()
        elif opcao == '4':
            consultar_tarefas()
        elif opcao == '9':
            print("\nSaindo do programa... Até mais! 👋")
            break
        else:
            print("\n Opção inválida. Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()


