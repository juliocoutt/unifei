import mysql.connector
from mysql.connector import Error
import hashlib

# -----------------------------------------------------
# Conexão
# -----------------------------------------------------
def conectar():
    return mysql.connector.connect(
        host='localhost',
        database='projeto_rondon',
        user='root',
        password=''
    )

# -----------------------------------------------------
# Hash de Senha
# -----------------------------------------------------
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# =====================================================
# INSTITUIÇÕES
# =====================================================


# Função para cadastrar uma nova instituição
def cadastrar_instituicao(nome, endereco, telefone, email, senha): # Cadastrar nova instituição
    try:# Tenta executar o bloco de código
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL
        # Insere os dados da nova instituição na tabela
        sql = """
        INSERT INTO instituicoes (nome, endereco, telefone, email, senha)
        VALUES (%s, %s, %s, %s, %s) 
        """
        # Executa o comando SQL com os dados fornecidos
        cursor.execute(sql, (nome, endereco, telefone, email, hash_senha(senha)))
        conexao.commit() # Confirma a transação
        print("Instituição cadastrada com sucesso!")
# Captura erros de execução
    except Error as e:
        print("Erro ao cadastrar instituição:", e) # Imprime o erro ocorrido
# Fecha o cursor e a conexão com o banco de dados

    finally: # Sempre executa este bloco
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão

# Função para alterar os dados de uma instituição existente
def alterar_instituicao(id, nome, endereco, telefone, email, senha): # Alterar dados da instituição
    try:# Tenta executar o bloco de código
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL

        sql = """
        UPDATE instituicoes
        SET nome=%s, endereco=%s, telefone=%s, email=%s, senha=%s
        WHERE id=%s
        """
        # Executa o comando SQL com os dados fornecidos
        cursor.execute(sql, (nome, endereco, telefone, email, hash_senha(senha), id))
        conexao.commit() # Confirma a transação
        print("Instituição alterada!")
# Captura erros de execução
    except Error as e:
        print("Erro ao alterar instituição:", e) # Imprime o erro ocorrido

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão

# Função para excluir uma instituição pelo ID
def excluir_instituicao(id): # Excluir instituição pelo ID
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL

        cursor.execute("DELETE FROM instituicoes WHERE id=%s", (id,))
        conexao.commit() # Confirma a transação
        print("Instituição excluída!")

    except Error as e:
        print("Erro ao excluir instituição:", e) # Imprime o erro ocorrido

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão

# Função para listar todas as instituições
def listar_instituicoes():
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL
        cursor.execute("SELECT id, nome, email FROM instituicoes")
        return cursor.fetchall()
# Captura erros de execução
    except Error as e:
        print("Erro ao listar instituições:", e)# Imprime o erro ocorrido
        return []

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão

# Função para autenticar uma instituição pelo email e senha
def autenticar_instituicao(email, senha):
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL
        sql = "SELECT id FROM instituicoes WHERE email=%s AND senha=%s"
        cursor.execute(sql, (email, hash_senha(senha)))

        return cursor.fetchone() is not None # Retorna True se encontrar a instituição
# Captura erros de execução
    except Error as e:
        print("Erro ao autenticar:", e) # Imprime o erro ocorrido
        return False

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão


# CAPACITAÇÕES


def cadastrar_capacitacao(instituicao_id, nome, descricao, duracao):
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL

        sql = """
        INSERT INTO capacitacoes (instituicao_id, nome, descricao, duracao)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (instituicao_id, nome, descricao, duracao))# Executa o comando SQL com os dados fornecidos
        conexao.commit() # Confirma a transação
        print("Capacitação cadastrada!")
# Captura erros de execução
    except Error as e:
        print("Erro ao cadastrar capacitação:", e)

    finally:
        cursor.close() # Fecha o cursor
        conexao.close()

# Função para alterar os dados de uma capacitação existente
def alterar_capacitacao(id, nome, descricao, duracao): # Alterar dados da capacitação
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL

        sql = """
        UPDATE capacitacoes
        SET nome=%s, descricao=%s, duracao=%s
        WHERE id=%s
        """
        cursor.execute(sql, (nome, descricao, duracao, id)) # Executa o comando SQL com os dados fornecidos
        conexao.commit() # Confirma a transação
        print("Capacitação alterada!")

    except Error as e:
        print("Erro ao alterar capacitação:", e) # Imprime o erro ocorrido
    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão

def excluir_capacitacao(id):
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL

        cursor.execute("DELETE FROM capacitacoes WHERE id=%s", (id,))
        conexao.commit() # Confirma a transação
        print("Capacitação excluída!")

    except Error as e:
        print("Erro ao excluir capacitação:", e) # Imprime o erro ocorrido

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão
# Função para listar todas as capacitações de uma instituição
def listar_capacitacoes_por_instituicao(instituicao_id):
    try:
        conexao = conectar() # Conecta ao banco de dados
        cursor = conexao.cursor()# Cria um cursor para executar comandos SQL
        cursor.execute("""
            SELECT id, nome, descricao, duracao
            FROM capacitacoes
            WHERE instituicao_id=%s
        """, (instituicao_id,))

        return cursor.fetchall()

    except Error as e:
        print("Erro ao listar capacitações:", e) # Imprime o erro ocorrido
        return []

    finally:
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão
