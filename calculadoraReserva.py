# calculadora costo por hora para reservar

print("Ejercicio 2: Calculadora de reservas")

tarifaHora = 8000
horas = 4
minutosExtra = 17

# Costo base
costoBase = tarifaHora * horas
print(f"El costo de la reserva es: $ {costoBase}")

recargo = (minutosExtra // 5) * 500 # Cobrar 500 pesos por cada 5 minutos de retraso
print(f"Valor cobrado por recargo: $ {recargo}")
recargoTotal = (minutosExtra / 5) * 500
print(f"Valor cobrado por recargo: $ {recargoTotal}")