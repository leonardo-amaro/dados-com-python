# Questão 4 – Pandas DataFrame
#
# Crie um DataFrame com os dados abaixo e exiba a média de vendas por produto.

import pandas as pd

dados = {
    "Produto": ["A", "B", "A", "C", "B", "A"],
    "Vendas": [100, 200, 150, 300, 250, 180]
}

df = pd.DataFrame(dados) # Carregando os dados dentro do DataFrame
vendas_a = df.loc[df["Produto"] == "A"]
vendas_b = df.loc[df["Produto"] == "B"]

print(f"Média de vendas do produto A: {vendas_a['Vendas'].mean()}")
print(f"Média de vendas do produto B: {vendas_b['Vendas'].mean()}")
