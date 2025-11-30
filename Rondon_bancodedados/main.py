# main.py
# Sistema de Cadastros para Instituições e Capacitações
# Utilizando MySQL e CustomTkinter
# Autor: Júlio Cesar Couto
# Data: 30/11/2025

import customtkinter as ctk
from tkinter import messagebox

# Importar funções do app.py
from app import ( 
    cadastrar_instituicao,
    cadastrar_capacitacao,
    alterar_instituicao,
    alterar_capacitacao,
    excluir_instituicao,
    excluir_capacitacao,
    listar_instituicoes,
    listar_capacitacoes_por_instituicao,
    autenticar_instituicao
)

# Configurações iniciais
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# ==================== JANELA PRINCIPAL ====================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Capacitações - Projeto Rondon")
        self.geometry("600x550")

        title = ctk.CTkLabel(self, text="Sistema de Cadastros", font=("Arial", 22))
        title.pack(pady=20)

        botoes = [
            ("Cadastrar Instituição", self.tela_cadastrar_instituicao),
            ("Listar Instituições", self.func_listar_instituicoes),
            ("Alterar Instituição", self.tela_alterar_instituicao),
            ("Excluir Instituição", self.tela_excluir_instituicao),
            ("Cadastrar Capacitação", self.tela_cadastrar_capacitacao),
            ("Listar Capacitações", self.tela_listar_capacitacoes),
            ("Alterar Capacitação", self.tela_alterar_capacitacao),
            ("Excluir Capacitação", self.tela_excluir_capacitacao),
            ("Login / Autenticação", self.tela_login),
        ]

        for texto, comando in botoes:
            ctk.CTkButton(self, text=texto, command=comando, width=300).pack(pady=5)

    def tela_cadastrar_instituicao(self):
        JanelaCadastroInstituicao()

    def func_listar_instituicoes(self):
        dados = listar_instituicoes()

        if not dados:
            messagebox.showinfo("Instituições", "Nenhuma instituição encontrada.")
            return

        texto = ""
        for i in dados:
            texto += f"ID: {i[0]}\nNome: {i[1]}\nE-mail: {i[2]}\n\n"

        messagebox.showinfo("Instituições", texto)

    def tela_alterar_instituicao(self):
        JanelaAlterarInstituicao()

    def tela_excluir_instituicao(self):
        JanelaExcluirInstituicao()

    def tela_cadastrar_capacitacao(self):
        JanelaCadastroCapacitacao()

    def tela_listar_capacitacoes(self):
        JanelaListarCapacitacoes()

    def tela_alterar_capacitacao(self):
        JanelaAlterarCapacitacao()

    def tela_excluir_capacitacao(self):
        JanelaExcluirCapacitacao()

    def tela_login(self):
        JanelaLogin()



# ==================== TELAS SECUNDÁRIAS ====================

class JanelaCadastroInstituicao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar Instituição")
        self.geometry("400x450")

        campos = ["Nome", "Endereço", "Telefone", "E-mail", "Senha"]
        self.entries = {}

        for c in campos:
            ctk.CTkLabel(self, text=c).pack()
            entry = ctk.CTkEntry(self, width=250, show="*" if c == "Senha" else "")
            entry.pack(pady=5)
            self.entries[c] = entry

        ctk.CTkButton(self, text="Cadastrar", command=self.salvar).pack(pady=25)

    def salvar(self):
        cadastrar_instituicao(
            self.entries["Nome"].get(),
            self.entries["Endereço"].get(),
            self.entries["Telefone"].get(),
            self.entries["E-mail"].get(),
            self.entries["Senha"].get()
        )
        messagebox.showinfo("Sucesso", "Instituição cadastrada!")
        self.after(500, self.destroy)



class JanelaAlterarInstituicao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Alterar Instituição")
        self.geometry("400x500")

        campos = ["ID", "Nome", "Endereço", "Telefone", "E-mail", "Senha"]
        self.entries = {}

        for c in campos:
            ctk.CTkLabel(self, text=c).pack()
            entry = ctk.CTkEntry(self, width=250, show="*" if c == "Senha" else "")
            entry.pack(pady=5)
            self.entries[c] = entry

        ctk.CTkButton(self, text="Alterar", command=self.salvar).pack(pady=25)

    def salvar(self):
        alterar_instituicao(
            self.entries["ID"].get(),
            self.entries["Nome"].get(),
            self.entries["Endereço"].get(),
            self.entries["Telefone"].get(),
            self.entries["E-mail"].get(),
            self.entries["Senha"].get()
        )
        messagebox.showinfo("Sucesso", "Instituição alterada!")
        self.after(500, self.destroy)



class JanelaExcluirInstituicao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Excluir Instituição")
        self.geometry("300x220")

        ctk.CTkLabel(self, text="ID da Instituição").pack(pady=10)
        self.id_entry = ctk.CTkEntry(self, width=200)
        self.id_entry.pack()

        ctk.CTkButton(self, text="Excluir", command=self.excluir).pack(pady=25)

    def excluir(self):
        excluir_instituicao(self.id_entry.get())
        messagebox.showinfo("Sucesso", "Instituição excluída!")
        self.after(500, self.destroy)



class JanelaCadastroCapacitacao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastrar Capacitação")
        self.geometry("400x450")

        campos = ["ID da Instituição", "Nome", "Descrição", "Duração (horas)"]
        self.entries = {}

        for c in campos:
            ctk.CTkLabel(self, text=c).pack()
            entry = ctk.CTkEntry(self, width=250)
            entry.pack(pady=5)
            self.entries[c] = entry

        ctk.CTkButton(self, text="Cadastrar", command=self.salvar).pack(pady=25)

    def salvar(self):
        cadastrar_capacitacao(
            self.entries["ID da Instituição"].get(),
            self.entries["Nome"].get(),
            self.entries["Descrição"].get(),
            self.entries["Duração (horas)"].get()
        )
        messagebox.showinfo("Sucesso", "Capacitação cadastrada!")
        self.after(500, self.destroy)



class JanelaListarCapacitacoes(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Listar Capacitações")
        self.geometry("350x250")

        ctk.CTkLabel(self, text="ID da Instituição").pack(pady=10)
        self.id_entry = ctk.CTkEntry(self, width=200)
        self.id_entry.pack()

        ctk.CTkButton(self, text="Listar", command=self.listar).pack(pady=25)

    def listar(self):
        dados = listar_capacitacoes_por_instituicao(self.id_entry.get())

        if not dados:
            messagebox.showinfo("Capacitações", "Nenhuma capacitação encontrada.")
            return

        texto = ""
        for item in dados:
            id_cap, nome, descricao, duracao = item
            texto += f"ID: {id_cap}\nNome: {nome}\nDescrição: {descricao}\nDuração: {duracao} horas\n\n"

        messagebox.showinfo("Capacitações", texto)
        # Não fecha após listar



class JanelaAlterarCapacitacao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Alterar Capacitação")
        self.geometry("400x450")

        campos = ["ID da Capacitação", "Nome", "Descrição", "Duração (horas)"]
        self.entries = {}

        for c in campos:
            ctk.CTkLabel(self, text=c).pack()
            entry = ctk.CTkEntry(self, width=250)
            entry.pack(pady=5)
            self.entries[c] = entry

        ctk.CTkButton(self, text="Alterar", command=self.salvar).pack(pady=25)

    def salvar(self):
        alterar_capacitacao(
            self.entries["ID da Capacitação"].get(),
            self.entries["Nome"].get(),
            self.entries["Descrição"].get(),
            self.entries["Duração (horas)"].get()
        )
        messagebox.showinfo("Sucesso", "Capacitação alterada!")
        self.after(500, self.destroy)



class JanelaExcluirCapacitacao(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Excluir Capacitação")
        self.geometry("300x220")

        ctk.CTkLabel(self, text="ID da Capacitação").pack(pady=10)
        self.id_entry = ctk.CTkEntry(self, width=200)
        self.id_entry.pack()

        ctk.CTkButton(self, text="Excluir", command=self.excluir).pack(pady=25)

    def excluir(self):
        excluir_capacitacao(self.id_entry.get())
        messagebox.showinfo("Sucesso", "Capacitação excluída!")
        self.after(500, self.destroy)



class JanelaLogin(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x250")

        ctk.CTkLabel(self, text="E-mail").pack(pady=10)
        self.email_entry = ctk.CTkEntry(self, width=230)
        self.email_entry.pack()

        ctk.CTkLabel(self, text="Senha").pack(pady=10)
        self.senha_entry = ctk.CTkEntry(self, width=230, show="*")
        self.senha_entry.pack()

        ctk.CTkButton(self, text="Entrar", command=self.login).pack(pady=25)

    def login(self):
        if autenticar_instituicao(self.email_entry.get(), self.senha_entry.get()):
            messagebox.showinfo("Sucesso", "Login efetuado!")
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

        self.after(500, self.destroy)



# ==================== EXECUÇÃO PRINCIPAL ====================

if __name__ == "__main__":
    app = App()
    app.mainloop()
