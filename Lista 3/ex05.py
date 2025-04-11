'''Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
'''

#entrada
idade =int(input("Digite sua idade: "))
tempoDeServico = float(input("Tempo de serviço: "))

#PROCESSAMENTO E SAIDA 
if ((idade>=65 ) or (idade>=60 and tempoDeServico>= 25) or (tempoDeServico>= 30)):
    print ("Você pode se aposentar !")
else:
    print("Tempo de serviço ou idade inferior ao necessarios. Você não pode se aposentar")