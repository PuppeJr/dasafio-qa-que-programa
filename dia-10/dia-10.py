import random  # Importa o módulo random para gerar números aleatórios

def jogo_de_adivinhacao():
    """Função que implementa o jogo de adivinhação."""
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas_restantes = 7  # Define o número de tentativas
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {tentativas_restantes} tentativas.")

    while tentativas_restantes > 0:
        tentativa = int(input("Digite sua tentativa: "))  # Solicita a tentativa do jogador
        
        if tentativa == numero_secreto:  # Verifica se o jogador acertou
            print("Parabéns! Você adivinhou o número correto!")
            return  # Sai da função após o jogador acertar
        elif tentativa < numero_secreto:  # Se a tentativa for menor que o número secreto
            print("O número secreto é maior.")
        else:  # Se a tentativa for maior que o número secreto
            print("O número secreto é menor.")
        
        tentativas_restantes -= 1  # Decrementa o número de tentativas restantes
        print(f"Tentativas restantes: {tentativas_restantes}")
    
    print("Fim de jogo! O número secreto era:", numero_secreto)

jogo_de_adivinhacao()  # Chama a função para iniciar o jogo
