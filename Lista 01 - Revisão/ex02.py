""" Escreva um programa em python que realize as funções básicas (soma, adição, multiplicação e
divisão) de uma calculadora, recebendo dois números informados pelo usuário. O programa deverá
perguntar ao usuário qual das 4 (quatro) funções básicas será realizada. O programa deverá validar
se os dados informados são números e, caso não sejam, deverá enviar uma mensagem para o
usuário solicitando que o mesmo informe um número válido. Após apresentar o resultado, o
programa deverá retornar ao início, para que o usuário possa realizar outra operação.
O programa somente deverá ser finalizado, caso o usuário digite a letra "F"."""

# Loop principal do programa
while True:
    # Solicita ao usuário os números e a operação desejada
    num1 = input("Digite o primeiro número (ou 'F' para finalizar): ")
    if num1.upper() == 'F':
        print("Programa finalizado.")
        break
    num2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Valida se os números são válidos
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Por favor, informe números válidos.")
        continue

    # Realiza a operação escolhida
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Divisão por zero não é permitida.")
            continue
    else:
        print("Operação inválida. Por favor, escolha entre +, -, *, /.")
        continue

    # Exibe o resultado da operação
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado:.2f}")