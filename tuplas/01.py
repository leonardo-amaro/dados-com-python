extenso = "um", "dois", "três", "quatro", "cinco"
numero = 0

print("=== Número por extenso ===")
numero = int(input("Por favor, digite um número entre 1 e 5: "))

while True:
    if 0 < numero and numero < 6:
        print(f"Você digitou o número {extenso[numero - 1]}.")
        break
    else:
        print("Número inválido!")
        numero = int(input("Por favor, escolha somente entre 1 e 5: "))

print("=== Fim ===")
