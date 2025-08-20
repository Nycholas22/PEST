numero = int(input("digite um número de 5 dígitos: "))
d1 = numero // 10000
d2 = (numero // 1000) % 10
d3 = (numero // 100) % 10
d4 = (numero // 10) % 10
d5 = numero % 10

if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or \
   d2 == d3 or d2 == d4 or d2 == d5 or \
   d3 == d4 or d3 == d5 or \
   d4 == d5:
    print("o número contém dígitos repetidos")
else:
    print("o número não contém dígitos repetidos")
    
