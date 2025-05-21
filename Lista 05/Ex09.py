'''Faça um programa em Python que calcule a média de 4 (quatro) números informados
pelo usuário. Caso o resultado da média seja maior ou igual ao valor 60, imprima a
mensagem "AlunoAprovado". Caso contrário, imprima "Aluno Reprovado". Você deverá
validar a informação dos 4 números informados e, deverá aceitar somente informações
do tipo int e ou float. Ou seja, você precisará criar uma lógica para verificar os
informados e, caso o usuário não informe um valor do tipo float e ou int, o seu programa
não pode cancelar (apresentar erro) e deverá exibir a seguinte mensagem: “Favor
informar um número válido para cada uma das 4 (quatro) notas”.'''

#ENTRADA
#recebendo as notas
notas = []
for i in range(4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Favor informar um número válido para cada uma das 4 (quatro) notas.")    

#PROCESSAMENTO
#calculando a media
media = sum(notas) / len(notas)
#saindo do loop

#SAIDA
if media >= 60:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
# Exibindo a média
print(f"A média das notas é: {media:.2f}")
# Exibindo as notas
print(f"As notas informadas foram: {notas}")
# Exibindo a média

