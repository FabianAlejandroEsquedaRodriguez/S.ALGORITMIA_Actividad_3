#Calcular el Numero e (Euler)

#Funcion para sacar el factorial de un numero
def factorial(num: int) -> int:#Va a retornar un entero
    fact = 1

    for i in range(num): #El for va de 0 hasta el valor que le mandemos

        fact *= num #Se multiplica el factorial por el numero
        num -= 1 #Y luego, ese resultado, por el numero - 1 
                #(La var. num, se resta de 1 en 1, para calcular el factorial)

    return fact


limite = 4
n = 0
e = 0

while n < limite:
    e += 1 / factorial(n)
    n += 1

print("\ne: ",e, "\n")#Imprimir el numero e