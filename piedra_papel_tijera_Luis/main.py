import random
from random import randint

inicio=0


Numero_maquina= 0

while inicio == 0:
    print("escoge Piedra(1), Papel(2) o Tijeras(3)")
    X =input(" >")


    if X == "1":
        Eleccion = 1
        print("🪨")
        inicio = 1
    elif X == "2":
        Eleccion = 2
        print("📄")
        inicio = 1
    elif X == "3":
        Eleccion = 3
        print("✂️")
        inicio = 1
    else:
        print("opción no valida")

Numero_maquina =randint(1,3)

print("VS")

while inicio == 1:
    if Numero_maquina == 1:
        EleccionMaquina = 1
        print("🪨")
        inicio =2
    elif Numero_maquina == 2:
        EleccionMaquina = 2
        print("📄")
        inicio = 2
    elif Numero_maquina == 3:
        EleccionMaquina = 3
        print("✂️")
        inicio = 2

while inicio == 2:
    if Eleccion ==1:
        if EleccionMaquina ==1:
            print("Empate")
            inicio = 0
        elif EleccionMaquina ==2:
            print("Perdiste")
            inicio = 0
        elif EleccionMaquina ==3:
            print("Ganaste")
            inicio = 0
    elif Eleccion ==2:
        if EleccionMaquina ==1:
            print("Ganaste")
            inicio = 0
        elif EleccionMaquina ==2:
            print("Empate")
            inicio = 0
        elif EleccionMaquina ==3:
            print("Perdiste")
            inicio = 0
    elif Eleccion ==3:
        if EleccionMaquina ==1:
            print("Perdiste")
            inicio = 0
        elif EleccionMaquina ==2:
            print("Ganaste")
            inicio = 0
        elif EleccionMaquina ==3:
            print("Empate")
            inicio = 0