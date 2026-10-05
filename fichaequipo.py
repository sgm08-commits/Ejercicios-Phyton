## Ejercicio 1 ficha de un equipos de computo

# Variable para guardar codigo de los equipos
codigo = "EQ-004"; #str
nombre = "Proyector Epson X200";
tipoequipo = "Audiovisual";
aniocompra = 2024
anioactual = 2026
preciodecompra = "$ 2.500.000"; #int
disponible = False; #bool
antiguedad = anioactual - aniocompra

# Imprimir valores en consola = print()
print(f"Codigo del Equipo: {codigo}");
print(f"Nombre del Equipo: {nombre}");
print(f"Tipo de Equipo: {tipoequipo}");
print(f"Precio: {preciodecompra}");
print(f"Estado del Equipo: {'Disponible' if disponible else 'No disponoble'}");
print(f"Este equipo tiene: {antiguedad} anios");

# Reto

#1- Agregar una variable anio_compra (int) y otra anio_actual (int).
#2- Calcular antiguedad = anio_actual - anio_compra
#3- Imprime : "Este equipo tiene (antiguedad) anios de uso"