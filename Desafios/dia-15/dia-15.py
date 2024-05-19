import csv
import os

# Nome do arquivo CSV
csv_file = 'biblioteca.csv'

# Função para criar o arquivo CSV com cabeçalhos, se não existir
def criar_arquivo_csv():
    if not os.path.isfile(csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Título', 'Autor', 'Ano de Publicação'])

# Função para adicionar um novo livro
def adicionar_livro():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    ano = input('Digite o ano de publicação do livro: ')
    
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, autor, ano])
    print(f'O livro "{titulo}" foi adicionado com sucesso!')

# Função para visualizar a lista de livros
def visualizar_livros():
    if not os.path.isfile(csv_file):
        print("Nenhum livro encontrado.")
        return

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        livros = list(reader)
        if len(livros) == 1:
            print("Nenhum livro encontrado.")
            return
        
        print("\nLista de livros disponíveis:")
        for i, livro in enumerate(livros[1:], start=1):  # Pula os cabeçalhos
            print(f"{i}. Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

# Função para exibir o menu e interagir com o usuário
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo livro")
        print("2. Visualizar lista de livros")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1/2/3): ")
        
        if opcao == '1':
            adicionar_livro()
        elif opcao == '2':
            visualizar_livros()
        elif opcao == '3':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Cria o arquivo CSV, se necessário, e inicia o menu
criar_arquivo_csv()
menu()
