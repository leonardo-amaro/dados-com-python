# Questão 6 – Estatística básica
#
# Implemente um código em Python que calcule:
# - Média
# - Mediana
# - Variância
# De uma lista de valores

valores = [10, 20, 30, 40]

def media(lista):
    soma = 0
    for l in lista:
        soma += l

    return soma / len(lista)

def mediana(lista):
    if len(lista) % 2 == 0:
        i2 = int(len(lista) / 2)
        i1 = int(i2 - 1)
        return media([lista[i1], lista[i2]])
    else:
        return lista[int(len(lista) / 2)]

def variancia(lista):
    m = media(lista)
    quadrado_desvio = []
    soma = 0
    for l in lista:
        quadrado_desvio.append((l - m) ** 2)
    for q in quadrado_desvio:
        soma += q

    return soma / len(lista)

print(f"Valores: {valores}")
print(f"Média dos valores: {media(valores)}")
print(f"Mediana: {mediana(valores)}")
print(f"Variancia da amostra: {variancia(valores)}")
