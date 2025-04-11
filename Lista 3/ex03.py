'''

Faça um programa Python que receba o valor de um salário e um percentual de aumento
a ser aplicado. Calcular o novo salário e imprimir o resultado obtido. Caso o novo salário
seja maior do R$ 2.000,00 imprima a mensagem "Novo salário é Acima da média
nacional brasileira". Caso contrário imprima "Novo salário é Abaixo da média
nacional brasileira ". 

'''
#ENTRADAS
salarioatual = float (input (" Digite o seu salario atual em R$ :  "))
percentualAlmento = float (input( "Digite o percetual de aumento (% : )"))

#PROCESSAMENTO
novosalario = float (salarioatual + (salarioatual* (percentualAlmento/100)))


#SAIDA 
print (f"\n Seu novo salario é de {novosalario}\n")

if novosalario > 2000:
    print ("Novo salário é Acima da média nacional brasileira")
else:
    print ("Novo salário é Abaixo da média nacional brasileira")
                     