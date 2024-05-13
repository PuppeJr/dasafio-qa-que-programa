# Solicita ao usuário que insira os números separados por espaços
entrada = input("Por favor, insira os números separados por espaços: ")

# Divide a entrada do usuário em uma lista de strings usando o método split()
numeros_str = entrada.split()

# Converte os números de strings para inteiros usando list comprehension
numeros = [int(numero) for numero in numeros_str]

# Ordena a lista de números usando o método sorted()
numeros_ordenados = sorted(numeros)

# Exibe os números ordenados
print("Números ordenados:", numeros_ordenados)
