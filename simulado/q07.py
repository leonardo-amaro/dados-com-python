# Questão 7 – Visualização com Matplotlib
#
# Usando o DataFrame da Questão 4, crie um gráfico de barras mostrando o total de vendas por produto.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Produto": ["A", "B", "A", "C", "B", "A"],
    "Vendas": [100, 200, 150, 300, 250, 180]
})

def total_vendas(produto):
    vendas_df = df.loc[df["Produto"] == produto]
    return vendas_df["Vendas"].sum()

plt.bar(["A", "B", "C"], [total_vendas("A"), total_vendas("B"), total_vendas("C")])
plt.show()
