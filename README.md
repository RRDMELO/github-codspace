# Projeto: Exemplos de Códigos em Python

Este projeto contém exemplos de códigos em Python que demonstram conceitos básicos de manipulação de strings, operações matemáticas, verificações condicionais e cálculos simples. O projeto foi desenvolvido utilizando o [Coldspace Github](https://github.com/coldspace).

## Índice

1. [Concatenando Dados](#1---concatenando-dados)
2. [Repetindo Textos](#2---repetindo-textos)
3. [Operações Matemáticas Simples](#3---operações-matemáticas-simples)
4. [Verificando Números Pares e Ímpares](#4---verificando-números-pares-e-ímpares)
5. [Calculando Média de Notas](#5---calculando-média-de-notas)
6. [Verificando Palíndromos](#6---verificando-palíndromos)

## 1 - Concatenando Dados

### Descrição
Recebemos dois dados diferentes do usuário e concatenamos em uma única string.

### O que aprenderemos?

- Manipulação de Strings (string)
- Concatenação
- Entrada de dados
- Utilização eficiente do Github Copilot

### Código
```python
# Abrir e ler o arquivo de entrada
with open('entrada.txt', 'r') as file:
    linhas = file.readlines()

# Extrair os dados das linhas
dado1 = linhas[0].strip().split(": ")[1]
dado2 = linhas[1].strip().split(": ")[1]

# Concatenar os dados
resultado = dado1 + " " + dado2

# Exibir o resultado
print("O resultado da concatenação é:", resultado)
```

## 2 - Repetindo Textos

### Descrição
Solicitamos uma string e um número inteiro como entrada. Depois retornamos a string repetida o número de vezes informado.

### O que aprenderemos?

- Manipulação de Strings (string)
- Números Inteiros (int)
- Múltiplas repetições
- Entrada de dados
- Aproveitar as sugestões do Github Copilot

### Código
```python
# Solicitar uma string e um número inteiro como entrada
string = input("Digite uma string: ")
num = int(input("Digite um número inteiro: "))

# Repetir a string o número de vezes informado
resultado = string * num

# Exibir o resultado
print("O resultado da repetição é:", resultado)
```

## 3 - Operações Matemáticas Simples

### Descrição
Solicitamos como entrada dois números e depois realizamos uma operação simples entre eles.

### O que aprenderemos?

- Operações Matemáticas Básicas
- Entrada de dados
- Utilização eficiente do Github Copilot

### Código
```python
# Solicitar dois números como entrada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar uma operação simples (soma)
resultado = num1 + num2

# Exibir o resultado
print("O resultado da soma é:", resultado)
```

## 4 - Verificando Números Pares e Ímpares

### Descrição
Recebemos um número inteiro e verificamos se ele é par ou ímpar. Utilizamos condicionais para realizar a verificação.

### O que aprenderemos?

- Utilização de condicionais em Python (if, else) para realizar verificações
- Introdução ao conceito de operador de módulo (%) para verificar se um número é par ou ímpar
- Exploração do uso de uma ferramenta de IA, como o Github Copilot, para otimizar a estrutura do código

### Código
```python
# Solicitar um número inteiro como entrada
num = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

## 5 - Calculando Média de Notas

### Descrição
Calculamos a média de três notas fornecidas na entrada do usuário. Utilizamos operadores aritméticos para realizar o cálculo da média.

### O que aprenderemos?

- Uso de variáveis para armazenar dados fornecidos pelo usuário
- Aplicação de operadores aritméticos (+, /) para calcular a média de um conjunto de valores
- Prática na solicitação e manipulação de entrada do usuário

### Código
```python
# Solicitar três notas como entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibir a média
print("A média das notas é:", media)
```

## 6 - Verificando Palíndromos

### Descrição
Testamos se uma palavra é um palíndromo. Utilizamos conceitos de manipulação de strings para inverter a palavra e comparar com a original.

### O que aprenderemos?

- Manipulação de strings em Python, especialmente invertendo uma string
- Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo
- Introdução ao conceito de palíndromos e sua aplicação em problemas de programação

### Código
```python
# Solicitar uma palavra como entrada
palavra = input("Digite uma palavra: ")

# Verificar se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
```