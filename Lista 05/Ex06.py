'''. Faça a um programa que receba do usuário um nome e imprima este mesmo nome sem
as suas vogais. '''


# Solicitando o nome do usuário
nome_usuario = input("Digite seu nome: \n")

# Removendo as vogais do nome
vogais = 'aeiouAEIOU'
nome_sem_vogais = ''

for letra in nome_usuario:
    if letra not in vogais:
        nome_sem_vogais += letra

# Exibindo o resultado
print(f"Seu nome sem vogais é: {nome_sem_vogais}")
