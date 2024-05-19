import random
import string

def obter_criterios():
    comprimento = int(input("Digite o comprimento da senha: "))
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'
    
    return comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais

def gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais):
    caracteres = ''
    if incluir_numeros:
        caracteres += string.digits
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Pelo menos um critério deve ser selecionado!")
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais = obter_criterios()
    
    try:
        senha = gerar_senha(comprimento, incluir_numeros, incluir_maiusculas, incluir_minusculas, incluir_especiais)
        print(f"Senha gerada: {senha}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
