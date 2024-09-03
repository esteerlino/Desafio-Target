# Desafio 02 - String

palavra = "InformadA" #Troque pela palavra que desejar

def conta_a(palavra):
    minusculo = palavra.lower()
    quantidade = minusculo.count('a')
    
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vez(es) em {palavra.lower()}.")
    else:
        print(f"A letra 'a' não está presente em {palavra.lower()}.")

conta_a(palavra)
