def estructuraCombinada():
    print("Lista que contiene diccionarios")

    inventario = [
        {"codigo":"EQ:001","nombre":"Portatil DELL","tipo":"Computador"},
        {"codigo":"EQ:002","nombre":"Proyector EPSON","tipo":"Audiovisual"},
        {"codigo":"EQ:003","nombre":"Silla ergonómica","tipo":"Mobiliario"},
    ]

    for equipo in inventario:
        print(f"{equipo['codigo']}: {equipo['nombre']} ({equipo['tipo']})")

estructuraCombinada()

