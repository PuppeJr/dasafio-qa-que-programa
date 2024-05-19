# Lista de perguntas, cada uma é um dicionário com a pergunta, opções e a resposta correta
quiz = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["1. Paris", "2. Londres", "3. Berlim", "4. Madri"],
        "resposta": "1"
    },
    {
        "pergunta": "Qual é o maior planeta do Sistema Solar?",
        "opcoes": ["1. Terra", "2. Júpiter", "3. Saturno", "4. Marte"],
        "resposta": "2"
    },
    {
        "pergunta": "Qual é a fórmula química da água?",
        "opcoes": ["1. CO2", "2. H2O", "3. O2", "4. NaCl"],
        "resposta": "2"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["1. Miguel de Cervantes", "2. William Shakespeare", "3. J.K. Rowling", "4. Mark Twain"],
        "resposta": "1"
    },
    {
        "pergunta": "Qual é a linguagem de programação mais usada para desenvolvimento web?",
        "opcoes": ["1. Java", "2. C++", "3. Python", "4. JavaScript"],
        "resposta": "4"
    }
]

def iniciar_quiz(quiz):
    print("Bem-vindo ao Quiz de Conhecimentos Gerais!")
    print("Responda às perguntas selecionando o número da opção correta.\n")

    pontuacao = 0

    for pergunta in quiz:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        resposta_usuario = input("Digite o número da sua resposta: ").strip()

        if resposta_usuario == pergunta["resposta"]:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta errada. A resposta correta é {pergunta['resposta']}.\n")

    print(f"Quiz terminado! Sua pontuação final é {pontuacao} de {len(quiz)}.\n")

# Inicia o quiz
iniciar_quiz(quiz)
