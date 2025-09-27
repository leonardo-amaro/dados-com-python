# Questão 8 – Correlação com Pandas
#
# Crie um DataFrame com duas colunas: "Horas_Estudo" e "Nota". Preencha com 5 valores fictícios.
# Depois, calcule e exiba a correlação entre as duas colunas.

import pandas as pd
df = pd.DataFrame({
    "Horas_Estudo": [30, 40, 60, 180, 200],
    "Nota": [6, 7, 8, 9, 10]
})

correlacao = df["Horas_Estudo"].corr(df["Nota"]) # Calcula a correlação entre duas colunas (Series)
print(correlacao)
