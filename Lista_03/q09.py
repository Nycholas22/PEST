n = int(input("Digite um número: "))


ordem = len(str(n))

soma = 0
temp = n

while temp > 0:
    digito = temp % 10
    soma += digito ** ordem
    temp //= 10

if soma == n:
    print(n, "é um número de Armstrong")
else:
    print(n, "não é um número de Armstrong")
