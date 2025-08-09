print("dijite las horas trabajadas")
horas_trabajadas = int(input("> "))

print("dijite el salario de la hora individual")
salario_hora = int(input("> "))

print("el pago es de =", horas_trabajadas * salario_hora)
if salario_hora>10000:
    print("Eres millonario")
elif salario_hora >= 5000:
    print("vas a Mitad de Camino")
else:
    print("Tienes que chambear mas")
