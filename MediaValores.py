qtd = 0
soma = 0
media = 0
valor = float(input("Informe o valor da nota: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de valores
    valor = float(input("Informe o valor da nota: "))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n total da Soma: ", soma)
print("\n total da Media: ", media)
print("\n Quantidade de valores digitados: ", qtd)