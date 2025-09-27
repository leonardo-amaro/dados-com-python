# Questão 1 – Estruturas de dados
#
# Crie uma função que receba uma lista de números inteiros e retorne um dicionário com:
# "pares": lista de números pares
# "ímpares": lista de números ímpares

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def dictPares(list):
    dicionario = {
        "pares": [],
        "impares": []
    }

    for item in list:
        if item % 2 == 0:
            dicionario["pares"].append(item)
        else:
            dicionario["impares"].append(item)
    
    return dicionario

print(dictPares(lista))
