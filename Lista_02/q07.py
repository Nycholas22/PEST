numero = int(input("digite um número de 3 digitos: "))
primeiro = numero // 100
ultimo = numero % 10
if primeiro == ultimo:
    print("o número é palíndromo")
else:
    print("o número não é palíndromo")