import random

def escolher_palavra():
    palavras = ["python", "programacao", "desafio", "computador", "jogo", "forca"]
    return random.choice(palavras)

def exibir_progresso(palavra, letras_adivinhadas):
    return ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6
    
    print("Bem-vindo ao jogo da forca!")
    
    while tentativas_restantes > 0:
        print(f"\nPalavra: {exibir_progresso(palavra, letras_adivinhadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        
        tentativa = input("Adivinhe uma letra: ").lower()
        
        if tentativa in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
            continue
        
        letras_adivinhadas.add(tentativa)
        
        if tentativa in palavra:
            print("Boa! Você adivinhou uma letra.")
        else:
            print("Errado! Essa letra não está na palavra.")
            tentativas_restantes -= 1
        
        if all(letra in letras_adivinhadas for letra in palavra):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()
