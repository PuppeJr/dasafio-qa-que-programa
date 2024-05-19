import requests

# Função para obter as taxas de câmbio da API
def obter_taxas(moeda_base):
    url = f'https://open.er-api.com/v6/latest/{moeda_base}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Erro ao acessar a API de conversão de moedas.")
        return None
    
    dados = response.json()
    if dados['result'] == 'error':
        print("Erro na resposta da API: ", dados['error-type'])
        return None
    
    return dados['rates']

# Função para converter o valor entre duas moedas
def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_destino not in taxas:
        print("Moeda de destino inválida.")
        return None
    
    taxa_conversao = taxas[moeda_destino]
    valor_convertido = valor * taxa_conversao
    return valor_convertido

# Função principal
def main():
    moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
    taxas = obter_taxas(moeda_origem)
    
    if not taxas:
        return
    
    valor = float(input(f"Digite o valor em {moeda_origem}: "))
    moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()
    
    valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
    
    if valor_convertido is not None:
        print(f"{valor} {moeda_origem} é equivalente a {valor_convertido:.2f} {moeda_destino}.")

if __name__ == '__main__':
    main()
