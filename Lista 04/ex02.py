# Programa para ler 10 notas e calcular a média

notas = 0 
cont = 1 #defino o contado igual 1 para que ele apareça no controle e chegue até 10

while cont <= 10:
    nota = int(input(f"Digite a nota do aluno {cont}: ")) #solicito ao usuario que digite a nota dos alinos
    notas += nota # faço o somatorio das notas digitadas 
    cont += 1 # acrescento + 1 ao contador

media = notas / 10 #calculo a media de acordo e apresente aos uauario a media
print("A média dos alunos é de:", media)
