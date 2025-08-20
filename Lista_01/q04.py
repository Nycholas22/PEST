hora_atual = int(input("Digite a hora atual (12h): "))


horas_espera = int(input("Digite o número de horas a esperar pelo alarme: "))


hora_alarme = (hora_atual + horas_espera) % 24


print(f"O alarme irá tocar às {hora_alarme} horas.")
