import random  # Importa o módulo random para gerar números aleatórios

def eh_primo(numero):
    """Função para verificar se um número é primo."""
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Se o número for divisível por algum outro número, não é primo
    return True  # Se o número não for divisível por nenhum outro número, é primo

pontuacao = 0  # Inicializa a pontuação do jogador

print("Bem-vindo ao jogo Primo ou Não Primo!")
print("Responda 's' para primo e 'n' para não primo.")
print("Para sair do jogo, digite 'exit'.")

while True:
    numero = random.randint(1, 100)  # Gera aleatoriamente um número entre 1 e 100
    print("\nNúmero:", numero)
    
    resposta = input("Primo (s/n)? ").lower()  # Solicita a resposta do jogador, converte para minúsculas
    
    if resposta == 'exit':
        print("Saindo do jogo...")
        break  # Se o jogador digitar 'exit', sai do loop
    
    if resposta == 's' and eh_primo(numero):
        print("Correto! O número é primo.")
        pontuacao += 1  # Incrementa a pontuação se a resposta estiver correta
    elif resposta == 'n' and not eh_primo(numero):
        print("Correto! O número não é primo.")
        pontuacao += 1  # Incrementa a pontuação se a resposta estiver correta
    else:
        print("Incorreto! O número é", "primo." if eh_primo(numero) else "não primo.")
        # Se a resposta estiver incorreta, exibe se o número é primo ou não
    
    print("Pontuação atual:", pontuacao)  # Exibe a pontuação atual do jogador

print("Sua pontuação final:", pontuacao)  # Exibe a pontuação final do jogador ao sair do jogo
