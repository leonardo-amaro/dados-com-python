# Questão 3 – NumPy básico
#
# Com a biblioteca NumPy, crie um array com os números de 1 a 20 e:
# - Mostre apenas os múltiplos de 3.
# - Calcule a média e o desvio padrão desse array.
import numpy as np

arr = np.arange(1, 21)

print(f"Os múltiplos de 3 são: {arr[arr % 3 == 0]}")
print(f"Média do Array é: {arr.mean()}")
print(f"O desvio padrão é: {arr.std()}")