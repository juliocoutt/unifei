'''
Ler uma temperatura em graus Celsus e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F= c* 9 / 5 - 32 sendo F a temperatura em Fahrenheit e C a
temperatura em Celsus. Caso a temperatura em Fahrenheit seja maior do que 90 imprima
a mensagem "Estamos no inverno" e, caso contrário imprima
a mensagem "Estamos no verão".

'''
#ENTRADA
temperaturaCelsius = float (input("Digite a tempertatua em graus Celsius"))
#PROCESSAMENTO
temperaturaFahrenheit= float ((temperaturaCelsius*9/5) + 32)

#SAÍDA
if temperaturaFahrenheit >=90:
    print ("Estamos no inverno.")

else:
    print ("Estamos no verão.")
   