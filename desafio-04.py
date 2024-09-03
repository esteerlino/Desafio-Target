# Desafio 04 - Qual o próximo elemento?

# Letra a: 1, 3, 5, 7
# Resposta: 9

sequencia = [1, 3, 5, 7]
proximo = sequencia[-1] + 2

print(f"O proximo numero da sequencia da letra 'a' é {proximo}")


# Letra b: 2, 4, 8, 16, 32, 64
# Resposta: 128

sequencia = [2, 4, 8, 16, 32, 64]
proximo = sequencia[-1] * 2

print(f"O proximo numero da sequencia da letra 'b' é {proximo}")

# Letra c: 0, 1, 4, 9, 16, 25, 36
# Resposta: 49

sequencia = [0, 1, 4, 9, 16, 25, 36]
proximo = len(sequencia) ** 2

print(f"O proximo numero da sequencia da letra 'c' é {proximo}")

# Letra d: 4, 16, 36, 64
# Resposta: 100

sequencia = [4, 16, 36, 64]
proximo = (int(sequencia[-1] ** 0.5) + 2) ** 2

print(f"O proximo numero da sequencia da letra 'd' é {proximo}")

# Letra e: 1, 1, 2, 3, 5, 8
# Resposta: 13

sequencia = [1, 1, 2, 3, 5, 8]
proximo = sequencia[-1] + sequencia[-2]

print(f"O proximo numero da sequencia da letra 'e' é {proximo}")


# Letra f: 2, 10, 12, 16, 17, 18, 19
# Resposta: 200. A sequência apresenta todos os números que começam com a letra "d". Assim, a resposta final é 200.

print(f"O proximo numero da sequencia da letra 'f' é 200")
