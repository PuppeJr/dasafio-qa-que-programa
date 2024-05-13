# Definindo uma função para exibir o menu de opções
def exibir_menu():
    print("===== Lista de Tarefas =====")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Mostrar Tarefas")
    print("4. Sair")
    print("============================")

# Inicializando uma lista vazia para armazenar as tarefas
tarefas = []

# Loop principal da aplicação
while True:
    # Exibindo o menu de opções
    exibir_menu()

    # Solicitando ao usuário que escolha uma opção
    opcao = input("Selecione uma opção: ")

    # Verificando a opção escolhida pelo usuário
    if opcao == "1":
        # Opção para adicionar uma nova tarefa
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)  # Adicionando a nova tarefa à lista de tarefas
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        # Opção para remover uma tarefa existente
        if len(tarefas) == 0:
            print("A lista de tarefas está vazia.")
        else:
            print("Tarefas:")
            for i, tarefa in enumerate(tarefas):  # Enumerando as tarefas para mostrar o índice
                print(f"{i + 1}. {tarefa}")
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            if 0 <= indice < len(tarefas):  # Verificando se o índice é válido
                tarefa_removida = tarefas.pop(indice)  # Removendo a tarefa da lista de tarefas
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Índice inválido. Tarefa não removida.")
    elif opcao == "3":
        # Opção para mostrar todas as tarefas
        if len(tarefas) == 0:
            print("A lista de tarefas está vazia.")
        else:
            print("Tarefas:")
            for i, tarefa in enumerate(tarefas, 1):  # Enumerando as tarefas para mostrar o índice
                print(f"{i}. {tarefa}")
    elif opcao == "4":
        # Opção para sair do programa
        print("Saindo...")
        break
    else:
        # Opção inválida
        print("Opção inválida. Por favor, selecione uma opção válida.")
