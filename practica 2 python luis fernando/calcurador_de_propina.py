print("ingrese el costo de la comida")
costocomida = int(input("> "))

print("ingrese el porcentaje de propina a pagar")
propina = float(input("> "))

if propina < 0:
    propina *= -1 

print("ingrese el total de personas que pagaran")
personas = int(input("> "))

if personas < 0:
    personas *= -1 
elif personas == 0:
    personas = 1

total_a_pagar = costocomida + ((propina / 100) * costocomida)

total_individual = total_a_pagar / personas

print(f"""
      el costo de la comida es de {costocomida}
      la propina es de {propina}%
      las personas que pagaran son {personas}
      cada persona debe pagar: {total_individual}""")