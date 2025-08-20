N = int(input("Digite um número: "))

invertido = 0 

while N > 0:
    digito = N % 10      
    invertido = invertido * 10 + digito
    N = N // 10

print("Número invertido:", invertido)
