#Ejercicio 01 creación de variables

#Creación de la función
#En phyton las funciones se crean con la palabra reservada "def"
def datos_estudiantes():
    print("Ejercicio 1: Datos del Estudiante")
    nombre = "Samuel"
    apelliddo = "Giraldo Murillo"
    ciclo = 2
    programa = "Desarrollo de software"
    correo = "sgiraldomurillo@utede.edu.co"
    Activo = True
    módulo = "Modelado de sistemas"

    #Vamos a imprimir la información almacenada en variables
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apelliddo}")
    print(f"Ciclo: {ciclo}")
    print(f"Programa: {programa}")
    print(f"Email: {correo}")
    print(f"Estado: {"Activo" if Activo else "Inactivo"}")
    print(f"Modulo: {módulo}")

#Vamos a entender como se reasignan valores a una variable
def contadorLaboratorio():
    print("Ejercicio 2: Contador de estudiantes en el laboratorio")
    personasEnSala = 0
    print(f"Cantidad de estudiantes en sala al abrir: {personasEnSala}")
    #tomo el valor de la variable y le sumo 1
    personasEnSala = personasEnSala + 1
    print(f"Entro un estudiante: {personasEnSala}")
    personasEnSala += 1
    print(f"Entro un estudiante: {personasEnSala}")
    personasEnSala += 1
    print(f"Entro un estudiante: {personasEnSala}")
    personasEnSala += 1
    print(f"Entro un estudiante: {personasEnSala}")
    personasEnSala += 1
    print(f"Entro un estudiante: {personasEnSala}")
    personasEnSala -= 1
    print(f"Salio un estudiante: {personasEnSala}")
    personasEnSala -= 1
    print(f"Salio un estudiante: {personasEnSala}")

    #intercambiar valores de variables

def intercambioTurnos():
    print("Ejercicio 3: Intercambio de turnos en sala")

    turno_sala101 = "Manana"
    turno_sala102 = "Noche"
    turno_sala103 = "Tarde"

    print(f"Antes sala 101: {turno_sala101} Sala 102: {turno_sala102} Sala 103 {turno_sala103}")
    #hacer un intercambio de valores entre variables

    turno_sala101, turno_sala102, turno_sala103 = turno_sala102,turno_sala103,turno_sala101
    print(f"Despues sala 101: {turno_sala101} Sala 102: {turno_sala102} Sala 103 {turno_sala103}")

    #crear una varianble turno sala 103 = tarde
    #rotar los valores entre las tres variables
    #la 101 pasa a ser 1'2
    #la 102 pasa a ser 103
    #103 pasa a ser 102

def registroPorconsola():
    nombre_estudiante = input("Ingrese su nombre: ")
    print(f"El nombre del estudiante es: {nombre_estudiante}")
    apellido_estudiante = input("Ingrese sus apellidos: ")
    print(f"Los apellidos del estudiante es: {apellido_estudiante}")
    ciclo_programa = input("Ingrese su ciclo: ")
    print(f"El ciclo del estudiante es: {ciclo_programa}")
    programa_ = input("Ingrese su programa: ")
    print(f"El programa del estudiante es: {programa_}")
    Emai_l = input("Ingrese su email: ")
    print(f"El email del estudiante es: {Emai_l}")
    activo = input("Esta activo: ")
    print(f"Activo: {activo}")
    Modulo = input("Ingrese su modulo: ")
    print(f"El modulo del estudiante es: {Modulo}")




    



#Para invocar la función hacemos lo siguiente
#Hacemos el llamado a la función
#datos_estudiantes()
#contadorLaboratorio()
#intercambioTurnos()
registroPorconsola()