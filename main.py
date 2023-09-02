# Exercícios: Conceitos Básicos em Python

# 1. Faça um Programa que peça um número e então mostre a
# mensagem: -> O número informado foi [número].

# n = float(input("Digite um número:" '\n'))
# print ("O numero informado foi:", n)

# # 2. Faça um Programa que peça dois números e imprima a soma.

# n1 = float(input("Digite o primeiro número:" '\n'))
# n2 = float(input("Digite o segundo número:" '\n'))
# print (n1+n2)

# 3. Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit. 
#F = 1.8 × C + 32 e C é a temperatura em Celsius e F é a temperatura correspondente em Fahrenheit.

tempC = float(input("Escreva a temperatura em graus Celcius:" '\n'))
F = 1.8 * tempC + 32
print ("A temperatura" , tempC, "em Fahrenheit é:", F)


# 4. Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês.