import random
Cara =1
Cruz = 2
Dinero = 10
Game = 1
print("Tienes 10$, quieres apostarlos?")
while Game == 1:
    print("Cara o Cruz?")
    Respuesta = input()
    str(input())
    numero_maquina = random.randint(1,2)

    if Respuesta == "Cara":
        if numero_maquina == 1:
            print("Ganaste, duplicando dinero")
            print("Ahora tienes", Dinero*2, "$")
        elif numero_maquina == 2:
            print("Perdiste, perdiendo dinero")
            print("Ahora tienes", Dinero/2, "$")
    elif Respuesta == "Cruz":
        if numero_maquina == 1:
            print("Perdiste, perdiendo dinero")
            print("Ahora tienes", Dinero/2, "$")
        elif numero_maquina == 2:
            print("Ganaste, duplicando dinero")
            print("Ahora tienes", Dinero*2, "$")
    print("¿Quieres jugar de nuevo?")
    input()
    if input() == "Sí":
        Game = 1
    else:
        Game = 0
