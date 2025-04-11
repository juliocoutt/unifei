#Faça um programa em Python que receba um número e caso ele seja par imprima “O
#número informado é Par.”, caso contrário se este número for ímpar imprima “O número
#informado é Ímpar.”.


# Declaraão da variavel e pedindo ao usuario para digitar o numero na entrada
numero = int (input("Digite um número: "))


#processamento e comparativo se o resto é igual a zero ou não 
if numero%2 == 0:
    print("Par")
else:
    print("Impar")

# A saída acontece no processamento pois a comaparação é feita diretamente na condicional.