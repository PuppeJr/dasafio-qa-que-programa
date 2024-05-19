import re

def validar_email(email):
    # Expressão regular para validar e-mail
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Usar a função re.match para verificar se a string corresponde ao padrão
    if re.match(regex, email):
        return True
    else:
        return False

# Exemplo de uso
email = input("Digite um endereço de e-mail: ")
if validar_email(email):
    print("E-mail válido!")
else:
    print("E-mail inválido!")
