# Função para adicionar um novo contato
def adicionar_contato(contatos):
    nome = input("Digite o nome do contato: ").strip()
    telefone = input("Digite o número de telefone do contato: ").strip()
    email = input("Digite o e-mail do contato: ").strip()

    # Verifica se o contato já existe
    for contato in contatos:
        if contato['nome'] == nome:
            print("Contato já existe.")
            return

    contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    print(f"Contato {nome} adicionado com sucesso!")

# Função para listar todos os contatos
def listar_contatos(contatos):
    if not contatos:
        print("Nenhum contato na agenda.")
    else:
        print("\nLista de Contatos:")
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

# Função para buscar um contato pelo nome
def buscar_contato(contatos):
    nome = input("Digite o nome do contato a ser buscado: ").strip()
    for contato in contatos:
        if contato['nome'].lower() == nome.lower():
            print(f"Contato encontrado: Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
            return
    print("Contato não encontrado.")

# Função para excluir um contato pelo nome
def excluir_contato(contatos):
    nome = input("Digite o nome do contato a ser excluído: ").strip()
    for i, contato in enumerate(contatos):
        if contato['nome'].lower() == nome.lower():
            del contatos[i]
            print(f"Contato {nome} excluído com sucesso!")
            return
    print("Contato não encontrado.")

# Função para exibir o menu e interagir com o usuário
def menu():
    contatos = []

    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Excluir contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1/2/3/4/5): ").strip()

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            listar_contatos(contatos)
        elif opcao == '3':
            buscar_contato(contatos)
        elif opcao == '4':
            excluir_contato(contatos)
        elif opcao == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicializa o programa
if __name__ == '__main__':
    menu()
