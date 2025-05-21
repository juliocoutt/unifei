'''Faça um programa que leia um endereço de e-mail informado pelo usuário. Caso o email informado esteja no padrão correto, 
ou seja, tenha no mínimo @.com o seu
programa deverá imprimir a mensagem “e-mail informado está correto” e finalizar o
programa, caso contrário deverá imprimir “e-mail inválido” e solicitar que o usuário
informe um novo e-mail válido.'''

#ENTRADA
while True:
    email = input("Digite um e-mail: ")
    # Verifica se tem '@' e '.com' no e-mail
    if "@" in email and ".com" in email:
        print("E-mail informado está correto")
        break
    else:
        print("E-mail inválido. Por favor, informe um e-mail válido.")



