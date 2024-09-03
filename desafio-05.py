# Desafio 05 - Interruptores

#Código para a simulação da questão
def simula():
    return {
        'Lâmpada 1': 1,
        'Lâmpada 2': 2,
        'Lâmpada 3': 3
    }

def verificar_lampadas(lampadas, estados):
    for lampada, interruptor in lampadas.items():
        estado = estados[lampada]
        if estado == 'quente e ligada':
            print(f"{lampada} está quente e ligada, então é controlada pelo segundo interruptor.")
        elif estado == 'quente e desligada':
            print(f"{lampada} está quente e desligada, então é controlada pelo primeiro interruptor.")
        elif estado == 'fria e desligada':
            print(f"{lampada} está fria e desligada, então é controlada pelo terceiro interruptor.")
        elif estado == 'fria e ligada':
            print(f"{lampada} está fria e ligada, então não é possível identificar. Isso é um erro.")
        else:
            print(f"Estado desconhecido para {lampada}.")

def main():
    lampadas = simula()

    #Mude os estados para verificar a relação entre os interruptores e as salas.
    estados = {
        'Lâmpada 1': 'quente e desligada',  
        'Lâmpada 2': 'quente e ligada',   
        'Lâmpada 3': 'fria e desligada',      
    }

    verificar_lampadas(lampadas, estados)

if __name__ == "__main__":
    main()

