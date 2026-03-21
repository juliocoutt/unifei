"""Escreva um programa em python que calcule o digito verificador de um CNPJ informado pelo
usuário. O programa deverá validar se os dados informados são números e, caso não sejam, deverá
enviar uma mensagem para o usuário solicitando que o mesmo informe um número válido. Após
apresentar o resultado, o programa deverá retornar ao início, para que o usuário possa realizar
outra operação. O programa somente deverá ser finalizado, caso o usuário digite a letra "F"."""

# Loop principal do programa
while True:
    # Solicita ao usuário o CNPJ
    cnpj = input("Digite o CNPJ (ou 'F' para finalizar): ")
    if cnpj.upper() == 'F':
        print("Programa finalizado.")
        break

    # Valida se o CNPJ é válido (apenas números e 14 dígitos)
    if not cnpj.isdigit() or len(cnpj) != 14:
        print("Por favor, informe um CNPJ válido (apenas números e 14 dígitos).")
        continue

    # Calcula os dígitos verificadores
    def calcular_digito_verificador(cnpj, peso):
        soma = sum(int(cnpj[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Pesos para os dígitos verificadores
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6] + peso1

    # Calcula os dígitos verificadores
    digito1 = calcular_digito_verificador(cnpj[:12], peso1)
    digito2 = calcular_digito_verificador(cnpj[:12] + digito1, peso2)

    # Exibe o resultado dos dígitos verificadores
    print(f"O CNPJ informado é: {cnpj[:12]}-{digito1}{digito2}")

