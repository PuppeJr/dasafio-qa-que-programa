import random

# Gera uma lista de 6 números aleatórios entre 1 e 60 sem repetições
numeros_mega_sena = random.sample(range(1, 61), 6)

# Ordena os números gerados
numeros_mega_sena.sort()

# Exibe os números gerados
print("Números da Mega Sena:")
for numero in numeros_mega_sena:
    print(numero)
