HoraAtual = 14

HorasAdicionais = 51

Alarme = (HoraAtual + HorasAdicionais) % 24

print(f"O alarme irá tocar às {Alarme} horas.")