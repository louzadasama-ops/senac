print ("DALE DALE!")
# Faça um programa que solicite ao usuario informar 3 valores e mostrar no final o maior valor, menor valor, o valor do meio.

# Entrada dos valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Identificação dos valores
maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)
meio = valor1 + valor2 + valor3 - maior - menor
media = (valor1 + valor2 + valor3) / 3

# Exibição dos resultados
print(f"Maior valor: {maior}")
print(f"Valor do meio: {meio}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")