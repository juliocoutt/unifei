'''
Faça um programa em Python que leia duas notas N1 e N2 de um aluno, e
informe se ele foi aprovado ou não numa disciplina.
Considere que a média final é dada pela equação:
média = 0.4 * N1 + 0.6 * N2
E que o aluno está se a média for maior ou igual a 5.0 e, reprovado caso contrário.

'''
#Entrada
n1 = float (input("Digite a Nota 1:"))
n2 = float (input("Digite a  Nota 2:"))
#processamento
media= float( 0.4 * n1 + 0.6 * n2)
#saida
if media >= 5.0:
    print (f"Sua Nota nesta diciplina é de {media}. Portando você está APROVADO !")
else:
    print  (f"Sua Nota nesta diciplina é de {media}. Portando você está REPROVADO !")