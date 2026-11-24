soma = 0
quantidade = 0
anterior = 0
crescente = True

while True:
    entrada = input("Digite um inteiro positivo ou S para sair: ")

    if entrada.lower() == "s":
        break

    try:
        numero = int(entrada)
    except ValueError:
        print("Digite um número inteiro válido.")
        continue

    ##############  TESTE  ##################
    if numero <= 0:
        print("O número deve ser maior que zero.")
        continue

    ###############  SOMA  #################
    soma += numero
    quantidade += 1

    ###############   CONTA SEQUENCIA   ###############
    if numero <= anterior:
        crescente = False
        break

    anterior = numero

############### RESULTADO  #################
print("\n--- RESULTADOS ---")

if quantidade == 0:
    print("Nenhum número válido foi informado.")
elif crescente:
    print("A sequência é crescente.")
else:
    print("A sequência não é crescente.")

print(f"Soma dos números: {soma}")
print(f"Quantidade de números: {quantidade}")