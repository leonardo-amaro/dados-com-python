# Questão 2 – Tuplas formatadas

# Dada a tupla:
alunos = (("Ana", 8.5), ("Bruno", 7.0), ("Carla", 9.2))
# Exiba os valores formatados em forma de tabela com duas colunas: Nome e Nota.

cabecalho = ("Nome", "Nota")

print("-" * 17)
print(f"{cabecalho[0]:<10}|{cabecalho[1]:>6}")
print("-" * 17)

for nome, nota in alunos:
    print(f"{nome:<10}|{nota:>6}")

print("-" * 17)
