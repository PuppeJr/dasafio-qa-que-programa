import time

def temporizador_progressivo(segundos):
    print("Temporizador progressivo iniciado.")
    for i in range(segundos + 1):
        print("Tempo decorrido:", i, "segundos")
        time.sleep(1)
    print("Temporizador progressivo concluído.")

def temporizador_regressivo(segundos):
    print("Temporizador regressivo iniciado.")
    for i in range(segundos, -1, -1):
        print("Tempo restante:", i, "segundos")
        time.sleep(1)
    print("Temporizador regressivo concluído.")

print("Bem-vindo ao Temporizador!")

opcao = input("Escolha uma opção:\n1. Temporizador Progressivo\n2. Temporizador Regressivo\n")

if opcao == "1":
    segundos = int(input("Digite a quantidade de segundos para o temporizador progressivo: "))
    temporizador_progressivo(segundos)
elif opcao == "2":
    segundos = int(input("Digite a quantidade de segundos para o temporizador regressivo: "))
    temporizador_regressivo(segundos)
else:
    print("Opção inválida.")
