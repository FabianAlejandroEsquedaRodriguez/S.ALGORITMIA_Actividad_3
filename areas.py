#Calcular el areas de algunas figuras
import math#importamos math, la cual tiene funciones matemáticas

#Funcion para el area del cuadrado
def cuadrado(lado):
    return lado * lado

#Funcion para el area del triangulo
def triangulo(base, altura):
    return (base * altura)/2

#Funcion para el area del circulo
def circulo(radio):
    return (3.1416 * math.pow(radio, 2))#O bien se puede hacer esto -> math.pi * radio**2

print("\nÁrea del cuadrado\n")

lado = float(input("Lado: "))
print("El área del cuadrado es: ", cuadrado(lado))

print("\nÁrea del triángulo\n")

base = float(input("Base: "))
altura = float(input("Altura: "))
print("El área del triángulo es: ", triangulo(base, altura))

print("\nÁrea del círculo\n")

radio = float(input("Radio: "))
print("El área del círculo es: ", circulo(radio))