# Desafio 01 - Fibonacci

def fibonacci(numero):
    a = 0
    b = 1

    while a < numero:
        temp = a
        a = b 
        b += temp
    return a == numero

numero_escolhido = 144 #Troque pelo número que desejar
    
if fibonacci(numero_escolhido):
    print(f"O número {numero_escolhido} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_escolhido} não pertence à sequência de Fibonacci.")
