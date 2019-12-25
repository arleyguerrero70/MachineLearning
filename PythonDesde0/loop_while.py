#cantidad de participantes
part_max = int(input("\nIndique la cantidad de participantes \n"))
print("El sistema se ha configurado para aceptar", part_max, "participantes \n \n")

cant_part = 0

#iniciando
while(cant_part<part_max):
    #datos participante
    nombre = str(input("Escribir nombre \n"))
    apellido = str(input("Escribir apellido \n"))
    email = str(input("Ingrese su correo electronico\n"))
    print("\nHola " + nombre,apellido + " su correo electonico es " , email)
    #confirmacion de inscripcion
    print("\nPara confirmar su incripcion escriba 'SI' para cancelarla escriba 'NO' por favor \n") 
    respuesta = input()
    respuesta = respuesta.lower()
    if respuesta == "si":
        print("Bienvendo", nombre + "  su número de participante es ",cant_part)
        cant_part += 1
    else:
        print("\nLa inscripcion se ha cancelado\n")

print("Cantidad máxima alcanzada")