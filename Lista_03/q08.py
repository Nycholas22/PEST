binario = int(input("Digite um número em binário: "))

decimal = 0
potencia = 0 

while binario > 0:
    digito = binario % 10
    decimal += digito * (2 ** potencia)
    binario = binario // 10
    potencia += 1

print("Valor em decimal:", decimal)
