import csv
import os
from datetime import datetime

# Nome do arquivo CSV
csv_file = 'despesas.csv'

# Função para criar o arquivo CSV com cabeçalhos, se não existir
def criar_arquivo_csv():
    if not os.path.isfile(csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Data', 'Categoria', 'Descrição', 'Valor'])

# Função para registrar uma nova despesa
def registrar_despesa():
    data = input('Digite a data da despesa (DD/MM/AAAA): ')
    categoria = input('Digite a categoria da despesa: ')
    descricao = input('Digite a descrição da despesa: ')
    valor = input('Digite o valor da despesa: ')
    
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([data, categoria, descricao, valor])
    print(f'Despesa registrada com sucesso!')

# Função para gerar o resumo das despesas por categoria
def resumo_por_categoria():
    despesas = {}
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalhos
        for row in reader:
            categoria = row[1]
            valor = float(row[3])
            if categoria in despesas:
                despesas[categoria] += valor
            else:
                despesas[categoria] = valor
    
    print("\nResumo das despesas por categoria:")
    for categoria, total in despesas.items():
        print(f"{categoria}: R$ {total:.2f}")

# Função para gerar o resumo das despesas por data específica
def resumo_por_data():
    data_especifica = input('Digite a data para o resumo (DD/MM/AAAA): ')
    total = 0.0
    despesas_na_data = []

    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalhos
        for row in reader:
            if row[0] == data_especifica:
                despesas_na_data.append(row)
                total += float(row[3])
    
    if despesas_na_data:
        print(f"\nResumo das despesas em {data_especifica}:")
        for despesa in despesas_na_data:
            print(f"Categoria: {despesa[1]}, Descrição: {despesa[2]}, Valor: R$ {despesa[3]:.2f}")
        print(f"Total: R$ {total:.2f}")
    else:
        print(f"Nenhuma despesa encontrada em {data_especifica}.")

# Função para exibir o menu e interagir com o usuário
def menu():
    while True:
        print("\nMenu:")
        print("1. Registrar nova despesa")
        print("2. Resumo das despesas por categoria")
        print("3. Resumo das despesas por data específica")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")
        
        if opcao == '1':
            registrar_despesa()
        elif opcao == '2':
            resumo_por_categoria()
        elif opcao == '3':
            resumo_por_data()
        elif opcao == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Cria o arquivo CSV, se necessário, e inicia o menu
criar_arquivo_csv()
menu()
