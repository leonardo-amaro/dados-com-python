palavras = ("rato", "gato", "sapato",
            "pato", "capacho", "abacate")

print("=== Analisador de vogais ===")

for p in palavras:
    print(f"\nA palavra {p.upper()} possui as seguintes vogais:", end=" ")
    for v in "aeiou":
        if v in p:
            print(v, end=" ")


print("\n=== Fim ===")