# Solicitar uma palavra como entrada
palavra = input("Digite uma palavra: ")

# Verificar se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
