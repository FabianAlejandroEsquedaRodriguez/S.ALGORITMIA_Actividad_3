#Pedirle al usuario el dia y mes de nacimiento
#para saber su signo zodiacal

print("\t\tSIGNO ZODIACAL\n\n")

dia = int(input("Día de nacimiento: "))
mes = input("Mes de nacimiento (c/letra): ")

if ((dia >= 20 and dia <= 31) and (mes == "enero" or mes == "Enero")) or ((dia >= 1 and dia <= 18) and (mes == "febrero" or mes == "Febrero")):
    print("\n\nTU SIGNO ZODIACAL ES ACUARIO\n\n")

elif ((dia >= 19 and dia <= 28) and (mes == "febrero" or mes == "Febrero")) or ((dia >= 1 and dia <= 20) and (mes == "marzo" or mes == "Marzo")):
    print("\n\nTU SIGNO ZODIACAL ES PISCIS\n\n")

elif ((dia >= 21 and dia <= 31) and (mes == "marzo" or mes == "Marzo")) or ((dia >= 1 and dia <= 19) and (mes == "abril" or mes == "Abril")):
    print("\n\nTU SIGNO ZODIACAL ES ARIES\n\n") 

elif ((dia >= 20 and dia <= 30) and (mes == "abril" or mes == "Abril")) or ((dia >= 1 and dia <= 20) and (mes == "mayo" or mes == "Mayo")):
    print("\n\nTU SIGNO ZODIACAL ES TAURO\n\n") 

elif ((dia >= 21 and dia <= 31) and (mes == "mayo" or mes == "Mayo")) or ((dia >= 1 and dia <= 20) and (mes == "junio" or mes == "Junio")):
    print("\n\nTU SIGNO ZODIACAL ES GÉMINIS\n\n") 

elif ((dia >= 21 and dia <= 30) and (mes == "junio" or mes == "Junio")) or ((dia >= 1 and dia <= 22) and (mes == "julio" or mes == "Julio")):
    print("\n\nTU SIGNO ZODIACAL ES CÁNCER\n\n") 

elif ((dia >= 23 and dia <= 31) and (mes == "julio" or mes == "Julio")) or ((dia >= 1 and dia <= 22) and (mes == "agosto" or mes == "Agosto")):
    print("\n\nTU SIGNO ZODIACAL ES LEO\n\n") 

elif ((dia >= 23 and dia <= 31) and (mes == "agosto" or mes == "Agosto")) or ((dia >= 1 and dia <= 22) and (mes == "septiembre" or mes == "Septiembre")):
    print("\n\nTU SIGNO ZODIACAL ES VIRGO\n\n")

elif ((dia >= 23 and dia <= 30) and (mes == "septiembre" or mes == "Septiembre")) or ((dia >= 1 and dia <= 22) and (mes == "octubre" or mes == "Octubre")):
    print("\n\nTU SIGNO ZODIACAL ES LIBRA\n\n") 

elif ((dia >= 23 and dia <= 31) and (mes == "octubre" or mes == "Octubre")) or ((dia >= 1 and dia <= 21) and (mes == "noviembre" or mes == "Noviembre")):
    print("\n\nTU SIGNO ZODIACAL ES ESCORPIO\n\n") 

elif ((dia >= 22 and dia <= 30) and (mes == "noviembre" or mes == "Noviembre")) or ((dia >= 1 and dia <= 21) and (mes == "diciembre" or mes == "Diciembre")):
    print("\n\nTU SIGNO ZODIACAL ES SAGITARIO\n\n") 

elif ((dia >= 22 and dia <= 31) and (mes == "diciembre" or mes == "Diciembre")) or ((dia>= 1 and dia <= 19) and (mes == "enero" or mes == "Enero")):
    print("\n\nTU SIGNO ZODIACAL ES CAPRICORNIO\n\n") 
 