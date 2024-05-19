def exibir_menu():
    print("Construtor de Consultas SQL")
    print("1. Criar consulta SQL SELECT")
    print("2. Criar comando SQL UPDATE")
    print("3. Criar comando SQL INSERT")
    print("4. Sair")

def criar_select():
    colunas = input("Digite as colunas a serem selecionadas (separadas por vírgula): ")
    tabela = input("Digite o nome da tabela: ")
    where_clause = input("Digite a cláusula WHERE (opcional): ")
    
    consulta = f"SELECT {colunas} FROM {tabela}"
    if where_clause:
        consulta += f" WHERE {where_clause}"
    
    print(f"\nConsulta SQL SELECT gerada:\n{consulta}\n")

def criar_update():
    tabela = input("Digite o nome da tabela: ")
    set_clause = input("Digite as colunas e novos valores (ex: coluna1=valor1, coluna2=valor2): ")
    where_clause = input("Digite a cláusula WHERE (opcional): ")
    
    comando = f"UPDATE {tabela} SET {set_clause}"
    if where_clause:
        comando += f" WHERE {where_clause}"
    
    print(f"\nComando SQL UPDATE gerado:\n{comando}\n")

def criar_insert():
    tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite as colunas (separadas por vírgula): ")
    valores = input("Digite os valores (separados por vírgula): ")
    
    comando = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
    
    print(f"\nComando SQL INSERT gerado:\n{comando}\n")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1/2/3/4): ").strip()
        
        if escolha == '1':
            criar_select()
        elif escolha == '2':
            criar_update()
        elif escolha == '3':
            criar_insert()
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
