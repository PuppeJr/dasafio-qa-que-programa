def km_para_milhas(km):
    return km * 0.621371

def milhas_para_km(milhas):
    return milhas / 0.621371

def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes / 3.28084

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Escolha a conversão que deseja realizar:")
print("1. Quilômetros para Milhas")
print("2. Milhas para Quilômetros")
print("3. Metros para Pés")
print("4. Pés para Metros")
print("5. Graus Celsius para Fahrenheit")
print("6. Graus Fahrenheit para Celsius")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    km = float(input("Digite a quantidade de quilômetros: "))
    print(km, "quilômetros são", km_para_milhas(km), "milhas.")
elif opcao == 2:
    milhas = float(input("Digite a quantidade de milhas: "))
    print(milhas, "milhas são", milhas_para_km(milhas), "quilômetros.")
elif opcao == 3:
    metros = float(input("Digite a quantidade de metros: "))
    print(metros, "metros são", metros_para_pes(metros), "pés.")
elif opcao == 4:
    pes = float(input("Digite a quantidade de pés: "))
    print(pes, "pés são", pes_para_metros(pes), "metros.")
elif opcao == 5:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    print(celsius, "graus Celsius são", celsius_para_fahrenheit(celsius), "graus Fahrenheit.")
elif opcao == 6:
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    print(fahrenheit, "graus Fahrenheit são", fahrenheit_para_celsius(fahrenheit), "graus Celsius.")
else:
    print("Opção inválida.")
