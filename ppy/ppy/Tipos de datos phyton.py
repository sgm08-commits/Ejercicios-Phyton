#tipos de datos de phyton

#1 tipos primitivos

def datosprimitivos():
    print("Ejercicio 1: Datos primitivos en python")

    codigoEquipo = "EQ-127"
    cantidadDisponible = 15
    preciounitario = 3250000.90
    requerimientoMantenimiento = False

    print(f"Codigo del equipo {codigoEquipo} -> es de tipo {type(codigoEquipo).__name__}")
    print(f"cantidadDisponible {cantidadDisponible} -> es de tipo {type(cantidadDisponible).__name__}")
    print(f"preciounitario {preciounitario} -> es de tipo {type(preciounitario).__name__}")
    print(f"requerimientoMantenimiento {requerimientoMantenimiento} -> es de tipo {type(requerimientoMantenimiento).__name__}")

#datosprimitivos()

def conversionTipoDatos():
    horastexto = "3"
    tarifatexto = "5000.88"

    horas = int(horastexto)
    tarifa = float(tarifatexto)

    total = horas * tarifa

    print(f"El total es {total}")

    print(f"Tipo de dato {type(horastexto)}")
    print(f"Tipo de dato {type(horas)}")

#conversionTipoDatos()
#listas en python se crean con corchetes

def listaSalas():
    print("Ejercicio 3: Listas en Python")

    salas = ["Sala Linux","Sala Multimedia","Sala Mac"]

    

    

    print(f"Imprimir lista completa: {salas}")
    print(f"Imprimir primer elemento de la sala: {salas[0]}")
    print(f"Imprimir ultimo elemento de la sala: {salas[-1]}")


    salas.append("Sala IA")

    print(f"Imprimir lista completa nueva: {salas}")

    salas.remove("Sala Linux")

    print(f"Imprimir lista completa actualizada: {salas}")

    salas.append("Sala Arduino")

    salas.append("Sala Servidores")

    

    print(f"Imprimir lista completa {salas.sort}")

    print(f"Número de salas {salas.__len__}")

    #nueva sala IA
    #como agregar elementos al final de la lista
    #eliminar con remove


    #Tarea deben agregar 2 salas a la lista
    #despues ordenar la lista alfabeticamente usando el metodo salas.sort()

    #Contar e imprimir las salas de la lista usando el metodo .length

    

#listaSalas()

def tublasHorarioClase():

    print("Ejercicio 4: Tublas de ubicación")

    horario = ("Lunes", "7:00","10:00")

    #desempaquetar tupla
    dia, inicio, final = horario
    print(f"Imprimir Tupla completa: {horario}")
    print(f"El horario es de {dia} iniciando a las {inicio} y terminando a las {final}")

#tublasHorarioClase()

def diccionarioEquipo():
    print("Ejercicio 5: Diccionario de Equipo")

    equipo = {"CodigoEquipo":"EQ-101",
              "nombreEquipo": "Proyector",
              "tipoEquipo": "Audiovisual",
              "precio": 2500000,
              "disponible": True
              }
    print(f"Imprimir el diccionario completo {equipo}")
    print(f"El tipo de equipo es: {equipo["tipoEquipo"]}")
    print(f"Claves disponibles: {list(equipo.keys())}")
    print(f"Valores disponibles: {list(equipo.values())}")

diccionarioEquipo()


