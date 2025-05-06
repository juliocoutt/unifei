"""Escreva um programa para ler as notas da 1ª e 2ª avaliações de um aluno,
calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores
válidos durante a leitura (0 a 10) para cada nota"""

# USEI WHILE TRUE PARA ASSUMOR QUE A CONDIÇÃO É VERDADEIRA N O LOOP

while True: # USUARIO ENTRA COM OS
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10: # VALIDO QUE OS DADOS ESTÃO DENTRO DO INTERVALO CORRETO 
        media = (nota1 + nota2) / 2
        print("Média:", media)
        break  # INSERIR O BREAK PARA FORÇAR O ENCERRAMENTO DO LOOP 
    else:
        print("Uma das notas está incorreta.")
