print("=== Analisador de Tuplas ===")

v1 = int(input("Por favor, digite um número: "))
v2 = int(input("Agora, digite outro número: "))
v3 = int(input("Por favor, digite mais um número: "))
v4 = int(input("Por fim, digite um último número: "))

tupla = v1, v2, v3, v4
contador = 0

for n in tupla:
    if n % 2 == 0:
        contador += 1

try:
    i = tupla.index(3)
except:
    indice = "O número 3 não apareceu em nenhuma posição"
else:
    indice = f"O número 3 apareceu pela primeira vez na posição {i}"

print(f"\nVocê digitou os números {tupla}")
print(f"Você digitou o número 9 apenas {tupla.count(9)} vez(es)")
print(indice)
print(f"Você digitou {contador} números pares")

print("=== Fim ===")