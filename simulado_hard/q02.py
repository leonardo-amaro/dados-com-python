# Questão 2 – Pandas: Filtragem e Estatística
#
# Dado o DataFrame:
import pandas as pd

df = pd.DataFrame({
    "Produto": ["A", "B", "A", "C", "B", "A", "C"],
    "Vendas": [100, 200, 150, 300, 250, 180, 400],
    "Estoque": [50, 30, 20, 15, 25, 10, 5]
})

# 1. Filtre os produtos que têm Vendas > 150 e Estoque < 30
# 2. Calcule a média de vendas desses produtos filtrados

df_filtrado = df.loc[(df["Vendas"] > 150) & (df["Estoque"] < 30)]
print(df_filtrado["Vendas"].mean())
