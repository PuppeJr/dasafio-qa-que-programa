# Solicita ao usuário que insira o texto
texto = input("Por favor, insira o texto: ")

# Inicializa um dicionário vazio para armazenar a contagem de cada letra
frequencia_letras = {}

# Itera sobre cada caractere do texto
for caractere in texto:
    # Verifica se o caractere é uma letra do alfabeto
    if caractere.isalpha():
        # Converte o caractere para minúsculo para ignorar diferenças de maiúsculas e minúsculas
        caractere = caractere.lower()
        # Verifica se o caractere já está no dicionário de frequência de letras
        if caractere in frequencia_letras:
            # Se estiver, incrementa sua contagem em 1
            frequencia_letras[caractere] += 1
        else:
            # Se não estiver, adiciona ao dicionário com uma contagem inicial de 1
            frequencia_letras[caractere] = 1

# Exibe a frequência de cada letra
print("Frequência de cada letra:")
for letra, frequencia in frequencia_letras.items():
    print(f"A letra '{letra}' aparece {frequencia} vezes.")
