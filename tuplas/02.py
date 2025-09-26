import random as rd

print("=== Sorteador de números ===")

tupla = rd.randint(1, 60), rd.randint(1, 60), rd.randint(1, 60), rd.randint(1, 60), rd.randint(1, 60)
print(f"Os números sorteados foram: {tupla}")
print(f"O maior número foi: {sorted(tupla)[-1]}")
print(f"O menor número foi: {sorted(tupla)[0]}")

print("=== Fim ===")