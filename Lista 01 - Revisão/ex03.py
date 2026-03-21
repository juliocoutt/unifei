"""Escreva um programa em python que calcule o dígito verificador de um CPF informado pelo
usuário. O programa deverá validar se os dados informados são números e, caso não sejam, deverá
enviar uma mensagem para o usuário solicitando que o mesmo informe um número válido. Após
apresentar o resultado, o programa deverá retornar ao início, para que o usuârio possa realizar
outra operação. O programa somente deverá ser finalizado, caso o usuário digite a letra "F"."""

# Loop principal do programa
while True:
    # Solicita ao usuário o CPF
    cpf = input("Digite o CPF (ou 'F' para finalizar): ")
    if cpf.upper() == 'F':
        print("Programa finalizado.")
        break

    # Valida se o CPF é válido (apenas números e 11 dígitos)
    if not cpf.isdigit() or len(cpf) != 11:
        print("Por favor, informe um CPF válido (apenas números e 11 dígitos).")
        continue

    # Calcula os dígitos verificadores
    def calcular_digito_verificador(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Pesos para os dígitos verificadores
    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Calcula os dígitos verificadores
    digito1 = calcular_digito_verificador(cpf[:9], peso1)
    digito2 = calcular_digito_verificador(cpf[:9] + digito1, peso2)

    # Exibe o resultado dos dígitos verificadores
    print(f"O CPF informado é: {cpf[:9]}-{digito1}{digito2}")
