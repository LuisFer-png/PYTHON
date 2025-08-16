nota1 = int(input("ingrese la nota 1: "))
nota2 = int(input("ingrese la nota 2: "))
nota3 = int(input("ingrese la nota 3: "))

total = nota1 + nota2 + nota3
promedio = total / 3

print(f"el promedio de las notas es de {promedio}")
if promedio >= 35:
    print("pasaste el año")
elif promedio > 29:
    print("puedes pasar con la recuperación")
elif promedio > 10:
    print("perdiste el año")
else:
    print("que pendejo")