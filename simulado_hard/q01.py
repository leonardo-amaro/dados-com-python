# Questão 1 – List Comprehension Avançada
#
# Dada a lista de números de 1 a 50:
numeros = list(range(1, 51))

# Crie uma list comprehension que gere uma lista de tuplas (n, "Fizz", "Buzz", "FizzBuzz") seguindo a regra do FizzBuzz:
# - "Fizz" se n for múltiplo de 3
# - "Buzz" se n for múltiplo de 5
# - "FizzBuzz" se n for múltiplo de 3 e 5
# - Caso contrário, apenas n

fizzbuzz_tupla = [(n,
                   "FizzBuzz" if n % 3 == 0 and n % 5 == 0
                   else "Fizz" if n % 3 == 0
                   else "Buzz" if n % 5 == 0
                   else n) for n in numeros]
print(fizzbuzz_tupla)
