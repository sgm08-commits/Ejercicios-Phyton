numM = 0
numF = 0
numNB = 0
numE1 = 0
numE2 = 0
numE3 = 0
numE4 = 0
numE5 = 0
numE6 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0

while True:
    genero = input("Digite el género (M/F/NB/*): ").upper()
    if genero =="M" or genero=="F" or genero=="NB" or genero=="*":
        break
    else:
        print("Genero invalido")
while genero !="*":
    while True:
        edad = int(input("Digite la edad (1 anio en adelante): "))
        if edad > 0:
            break
        else:
            print("Edad invalida")
            
    while True:   
        estrato = int(input("Digite el estrato (1 a 6): "))
        if estrato==1 or estrato==2 or estrato==3 or estrato==4 or estrato==5 or estrato==6:
            break
        else:
            print("Estrato invalido")
           
    if genero=="M":
        numM += 1
    elif genero=="F":
        numF += 1
    else:
        numNB += 1
        
    if estrato== 1:
        numE1 += 1
    elif estrato==2:
        numE2 += 1
    elif estrato==3:
        numE3 += 1
    elif estrato==4:
        numE4 +=1
    elif estrato==5:
        numE5 += 1
    else:
        numE6 += 1
        
    if edad >= 1 and edad <= 17:
        num1 += 1
    elif edad >= 18 and edad <= 28:
        num2 += 1
    elif edad >= 29 and edad <= 55:
        num3 += 1
    else:
        num4 += 1
        

        
    genero = input("Digite el género M/F/NB/*: ")


print(f"Numero de masculinos: {numM}")
print(f"Numero de femeninos: {numF}")
print(f"Numero de no binarios: {numNB}")
print(f"Numero de estratos 1: {numE1}")
print(f"Numero de estratos 2: {numE2}")
print(f"Numero de estratos 3: {numE3}")
print(f"Numero de estratos 4: {numE4}")
print(f"Numero de estratos 5: {numE5}")
print(f"Numero de estratos 6: {numE6}")
print(f"Numero de menores de edad: {num1}")
print(f"Numero de adultos jovenes: {num2}")
print(f"Numero de adutos: {num3}")
print(f"Numero de adultos mayores: {num4}")


    
    
