print("=== Listagem de preços ===")

tupla = (("Caderno", 23.59), ("Estojo", 39.99), ("Mochila", 81.69))

for item, valor in tupla:
    print(f"{item:.<20}R${str(valor):>4}")

print("=== Fim ===")