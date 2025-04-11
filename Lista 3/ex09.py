'''
Faça um programa para a Polícia Civil de Minas Gerais com a finalidade de ajudar
aclassificar o envolvimento de uma pessoa em um crime. Para isso, o seu programa
deverá fazer 5 perguntas para uma pessoa sobre um crime, sendo elas:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa
nocrime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Casocontrário, ele será
classificado como "Inocente".

'''
#ENTRADA 
nome = str  (input( " Qual o nome da pessoal: "))

cont = 0

#PROCESSAMENTO 
# PERGUNTAS
print("Telefonou para a vítima? (S/N)")
resposta = input()
if resposta == 'S':
    cont += 1

print("Esteve no local do crime? (S/N)")
resposta = input()
if resposta == 'S':
    cont += 1

print("Mora perto da vítima? (S/N)")
resposta = input()
if resposta == 'S':
    cont += 1

print("Devia para a vítima? (S/N)")
resposta = input()
if resposta == 'S':
    cont += 1

print("Já trabalhou com a vítima? (S/N)")
resposta = input()
if resposta == 'S':
    cont += 1
#SAÍDA 
# CLASSIFICAÇÃO
if cont == 2:
    print(f"{nome} é classificado(a) como Suspeita\n ")
elif 3 >= cont <= 4:
    print(f"{nome} é classificado(a) como Cúmplice \n ")
elif cont == 5:
    print(f"{nome} é classificado(a) como Assassino\n ")
else:
    print(f"{nome} é classificado(a) como Inocente\n ")