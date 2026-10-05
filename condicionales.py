def ejerciciosIFSimple():
    print("Ejercicios 1: If simple")

    stock = 1

    if stock >= 1:
        print("Stock disponible")
    else:
        print("Sin stock disponible")


#ejerciciosIFSimple()

def ejercicioIFELSE():
    print("Ejercicio 2: If/Else")

    capacidadSala = 30

    tamanoGrupo = 22

    if tamanoGrupo <= capacidadSala:
       print("La sala puede ser prestada")
    else:
        print("La sala no puede ser prestada")    

#ejercicioIFELSE()

def estadosSala(reservasActivas,capacidad):
    if(capacidad == 0):
        return  "En mantenimiento"
    elif reservasActivas == 0:
        return "Libre"
    elif reservasActivas < capacidad:
        return "Parcialmente ocupadas"
    elif reservasActivas > capacidad:
        return "Sobrecupo"
    else:
        return "Llena"


#estadosSala()

def ejercicioEIELIFELSE():
    print("Ejercicio 3: if/elif/else")

    salas = [
        ("Sala Q27",0,30),
        ("Sala Q29",18,30),
        ("Auditorio",120,120),
        ("Lab cocina",0,0),
        ("Gimnasio",20,15)
    ]

    for nombreSala, reservas, capacidad in salas:
        print(f"{nombreSala}: {estadosSala(reservas,capacidad)}")

ejercicioEIELIFELSE()