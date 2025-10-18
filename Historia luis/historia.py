#VARIABLES


texto ="𝕋𝕠𝕞𝕒 𝕝𝕒 𝕔𝕒𝕣𝕟𝕖, 𝕔𝕠́𝕣𝕥𝕒𝕝𝕒 𝕖𝕟 𝕥𝕣𝕠𝕔𝕚𝕥𝕠𝕤, 𝕒𝕟̃𝕒𝕕𝕖𝕝𝕖 𝕦𝕟𝕒 𝕡𝕚𝕫𝕔𝕒 𝕕𝕖 𝕤𝕒𝕝 𝕪 𝕔𝕒𝕝𝕚𝕖𝕟𝕥𝕒 𝕡𝕠𝕣 𝟛𝟘 𝕞𝕚𝕟𝕦𝕥𝕠𝕤 𝕖𝕟 𝕝𝕒..."
guardian = 0
Grimorio = 0

#FUNCIONES
def inicio():
    op = input("Selecciona qué hacer.\nA) Gritas fuertes para pedir ayuda.\nB) Golpeas la puerta. \nC) Te asomas por la ventana pequeña.\nEscribe tu opción (a, b o c)\n")
    if op=="A" or op=="a":
        gritar()
    elif op=="B" or op=="b":
        golpearPuerta()
    elif op=="C" or op=="c":
        mirarVentanuco()
    else:
        print("Esta no era una opción, mueres de estupidez.")

def gritar():
    global guardian
    if guardian == 0:
        print("Escuchas a lo lejos unas pisadas... Se acercan rápido hacia la puerta. Justo cuando parecía que esas pisadas derribarían la puerta, se detienen. Alguien se ha quedado esperando en la puerta...\n")
        guardian = 1;
        inicio()
    #CONTINÚA AQUÍ LA HISTORIA...
    else:
        print("Escuchas un ruido, alguien intenta abrir la puerta...")
    #CONTINÚA AQUÍ LA HISTORIA...

def golpearPuerta():
    print("Parece que el mantenimiento del castillo deja mucho que desear, tras el segundo golpe, la puerta se abre...")
    print("Escuchas unas pisadas metalicas corriendo hacia tu dirección, que debes hacer?")
    op1 = input("Selecciona que hacer.\nA)Esconderte en tu celda.\nB)Salir corriendo en la otra dirección.\nC)Efrentarte a lo que sea que venga.\nEscribe la opción (a, b o c)\n")
    if op1=="A" or op1=="a":
        Esconderte()
    elif op1=="B" or op1=="b":
        Correr()
    elif op1=="C" or op1=="c":
        LucharPuño()
    else:
        print("Esta no era una opción, mueres de estupidez.")
        
def LucharPuño():
    print("Intestas embestir a lo que se viene con toda tu valentía y luchar con todo tu corazón")
    print("Luchar contra una armadura desarmado no era la mejor idea...")
    print("Moriste de una manera valientemente estúpida")
def Esconderte():
    print("Te has escondido en tu celda, escuchaste a la pisadas metalicas parar por un segundo y volver a su camino")
    Correr()
    
def Correr():
    print("Llegas a una sala llena de armas, escuchas pisadas corriendo hacia tu dirección, que debes hacer?")
    op3= input("Selecciona que hacer.\nA)Tomar una Maza.\nB)Tomar una espada.\nC)Tomar un grimorio.\nEscribe la opción (a, b o c)\n")
    if op3=="A" or op3=="a":
        TomarMaza()
    elif op3=="B" or op3=="b":
        TomarEspada()
    elif op3=="C" or op3=="c":
        TomarGrimorio()
        
def TomarMaza():
    print("Tomas el martillo y das un golpe fuerte a la armadura metalica, solo para darte cuenta que fallaste porque la armadura era enana...")
    print("Te mato la comicamente pequeña armadura")

def TomarEspada():
    print("Al intentar tomar la espada colgada de la pared terminas abriendo un pasillo oculto, decides bajar por el pasillo")
    pasillo()
    
def TomarGrimorio():
    print("abres el grimorio cuando la armadura llega y empiezas a conjurar")
    print(texto)
    print("hay un silencio incomodo y etereo en la habitación...HASTA QUE LA ARMADURA EMPIEZA A ARDER HASTA QUEDAR HECHA POLVO")
    print("Eso fue... Anticlimatico")
    print("Otra arma de más no vendría mal")
    Grimorio = 1
    TomarEspada()

def mirarVentanuco():
    print("Parece que no llegas a ver nada, aunque parece que fuera hace bueno y los pájaros cantan.")
    op = input("Selecciona qué hacer.\nA) Gritas fuertes para pedir ayuda.\nB) Golpeas la puerta.\nEscribe tu opción (a, b o c)\n")
    if op=="A" or op=="a":
        gritar()
    elif op=="B" or op=="b":
        golpearPuerta()
    else:
        print("Esta no era una opción, mueres de estupidez.")

def pasillo():
    print("Deciendes hasta")

#COMIENZO DE LA HISTORIA
print("Te acabas de despertar, lo último que recuerdas es que caminabas por el bosque, dirección al castillo encantado con intención de salvar a tu noble dragón, prisionero del malvado Mago Pitón. Miras a tu alrededor y te das cuenta de que estás encerrado en una sala de piedra. Solo hay una puerta y una pequeña ventana... \n")

inicio()