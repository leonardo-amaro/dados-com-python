# Questão 1 – List Comprehension Avançada
#
# Dada a lista de números de 1 a 50:
numeros = list(range(1, 51))

# Crie uma list comprehension que gere uma lista de tuplas (n, "Fizz", "Buzz", "FizzBuzz") seguindo a regra do FizzBuzz:
# - "Fizz" se n for múltiplo de 3
# - "Buzz" se n for múltiplo de 5
# - "FizzBuzz" se n for múltiplo de 3 e 5
# - Caso contrário, apenas n

def fizzbuzz(inteiro):
    if inteiro % 3 == 0 and inteiro % 5 == 0:
        return "FizzBuzz"
    elif inteiro % 3 == 0:
        return "Fizz"
    elif inteiro % 5 == 0:
        return "Buzz"
    else:
        return inteiro

fizzbuzz_tupla = [(n, fizzbuzz(n)) for n in numeros]
print(fizzbuzz_tupla)
