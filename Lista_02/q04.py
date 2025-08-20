num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

soma = num1 + num2 + num3
if num1 == num2 or num1 == num3 or num2 == num3:
    print("a soma é 0")
else:
    print("a soma é", soma)
