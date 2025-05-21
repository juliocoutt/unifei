'''. Faça um programa em Python que solicite ao usuário que informe os dados de nome,
data de nascimento e CPF. Seu programa deverá validar e somente aceitar um nome
válido (não deve conter números e nem caracteres especiais e, somente a primeira letra
do nome deverá estar em maiúsculo), uma data de nascimento válida e um CPF válido
(deverá realizar o cálculo do dígito verificador). Após as validações imprimir os dados
informados com suas respectivas máscaras, por exemplo:
NOME: Eduardo Jabbur Machado
Data Nascimento: 28/08/1985
CPF: 748.099.400-12S'''

import re
from datetime import datetime

# Solicitando o nome e validando
while True:
    nome = input("Digite seu nome completo: ")

    # Verifica se não há números ou caracteres especiais
    if all(palavra.isalpha() for palavra in nome.split()):
        # Verifica se cada palavra começa com maiúscula
        if all(palavra[0].isupper() and palavra[1:].islower() for palavra in nome.split()):
            break
    print("Nome inválido! Use apenas letras e inicie cada nome com maiúscula.")

# Solicitando a data de nascimento e validando
while True:
    data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    try:
        datetime.strptime(data_nasc, '%d/%m/%Y')
        break
    except ValueError:
        print("Data inválida! Use o formato DD/MM/AAAA.")

# Solicitando o CPF e validando
while True:
    cpf = input("Digite seu CPF (apenas números ou formatado): ")
    cpf_numeros = re.sub(r'\D', '', cpf)

    if len(cpf_numeros) == 11 and cpf_numeros != cpf_numeros[0] * 11:
        # Cálculo do primeiro dígito
        soma = 0
        for i in range(9):
            soma += int(cpf_numeros[i]) * (10 - i)
        dig1 = (soma * 10 % 11) % 10

        # Cálculo do segundo dígito
        soma = 0
        for i in range(10):
            soma += int(cpf_numeros[i]) * (11 - i)
        dig2 = (soma * 10 % 11) % 10

        if cpf_numeros[-2:] == f"{dig1}{dig2}":
            break
    print("CPF inválido! Verifique e tente novamente.")

# Formatando o CPF
cpf_formatado = f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"

# Exibindo os dados
print("\nDados informados:")
print(f"NOME: {nome}")
print(f"Data Nascimento: {data_nasc}")
print(f"CPF: {cpf_formatado}")
