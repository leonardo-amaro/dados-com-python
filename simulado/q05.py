# Questão 5 – Limpeza de dados
#
# Dado o DataFrame:
import pandas as pd
df = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Ana"],
    "Idade": [25, None, 30, 25]
})

# Escreva um código para:
# - Remover as linhas com valores nulos.
# - Remover duplicados.

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print(df)
