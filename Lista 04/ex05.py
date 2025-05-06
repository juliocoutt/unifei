""" Escreva um programa para ler 2 valores e se o segundo valor informado for
ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser
aceito o valor zero e imprimir o resultado da divisão do primeiro valor lido pelo
segundo valor lido.
"""

numero2 = 0 # DEFININDO COMO ZERO PARA QUE ELE RODE NO PRIMEIRO LOOP 

while numero2 <= 0: # AQUI SEMPRE QUE O NUMERO FOR MENOR QUE OU IGUAL A ZERO O USUARIO PRECISA DIGITAR UM NOVO DENOMINADOR

    #USUARIO ENTRA COM OS DADOS 
    numero1 = int (input(" Digite o primeiro número: "))
    numero2 = int (input(" Digite o segundo número: "))

    # DENOMINADOR SENDO MAIOR QUE ZERO ELE ENTRA NESSA CONDIÇÃO
    if numero2>0:
        print("Resultado:", numero1/numero2)
    
    # CASO O USUARIO ENTRE COM UM DADO INFERIOR OU IGUAL A ZERO ELE RECEBE ESSA INFORMAÇÃO. 
    else:
        print("Denominado precisa ser maior que ZERO \n \n ")

