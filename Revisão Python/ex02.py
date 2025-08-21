'''Faça um programa em Python que leia uma sequência de números do
usuário e pare a leitura quando o usuário digitar um número negativo. As seguintes
funcionalidades devem ser implementadas:
a) imprimir a soma dos números positivos lidos
b) imprimir a média de todos os números lidos
c) imprimir o número com maior valor
d) imprimir todos os números negativos'''

def main():
    numeros = []
    negativos = []

    while True:
        try:
            n = int(input("Digite um número (ou um negativo para encerrar): "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue

        if n < 0:
            negativos.append(n)
            break
        numeros.append(n)

    # a) Soma dos positivos
    soma_positivos = sum(x for x in numeros if x > 0)

    # b) Média de todos os números lidos (incluindo negativos)
    todos = numeros + negativos
    media = sum(todos) / len(todos) if todos else 0

    # c) Maior valor
    maior = max(todos) if todos else None

    # d) Lista de negativos
    # já guardamos em `negativos`

    print("\n--- Resultados ---")
    print(f"Soma dos números positivos: {soma_positivos}")
    print(f"Média de todos os números: {media:.2f}")
    print(f"Maior número lido: {maior}")
    print(f"Números negativos digitados: {negativos}")


if __name__ == "__main__":
    main()


