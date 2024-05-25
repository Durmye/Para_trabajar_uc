#!/usr/bin/python 
# -*- coding: utf-8 -*- 
from math import pi 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREN = '\033[92m'
    OKYEOW = '\033[93m'
    OKREDS = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_number(n):
    try:
        float(n)   # Intentamos transformar la variable a float, si no funciona devolverá error
    except ValueError:
        return False
    return True

def obtener_radio():
    valido = False
    ingreso = ""
    while (not valido):
        ingreso = input("\nIngrese el radio del círculo: ")
        valido = is_number(ingreso)
    return float(ingreso)

radio = obtener_radio()
opcion = ""

while (opcion != "E"):
    print("\n" + bcolors.UNDERLINE + "Escoge una opción (R={0:.2f})" .format(radio) + bcolors.ENDC )
    print("a) Calcular el diámetro.")
    print("b) Calcular el perímetro.")
    print("c) Calcular el área.")
    print("d) Reingresar el radio.")
    print("e) Salir.")
    opcion = input(bcolors.OKYEOW + "Teclea a, b, c, d ó e y pulsa el retorno de carro: " + bcolors.ENDC)
    opcion = opcion.upper()
    if opcion == "A":
        diametro = 2 * radio 
        print("\n" + bcolors.HEADER + "El diámetro es {0:.2f} unidades" .format(diametro) + bcolors.ENDC)
    elif opcion == "B":
        perimetro = 2 * pi * radio
        print("\n" + bcolors.HEADER + "El perímetro es {0:.2f} unidades" .format(perimetro) + bcolors.ENDC)
    elif opcion == "C":
        area = pi * pow(radio,2)
        print("\n" + bcolors.HEADER + "El área es {0:.2f} unidades cuadradas" .format(area) + bcolors.ENDC)
    elif opcion == "D":
        radio = obtener_radio()
    elif opcion == "E":
        print("Hasta Luego!")
    else: 
        print(bcolors.OKREDS + "Solo hay cuatro opciones: a, b, c, d ó e. Tú has tecleado " + opcion + bcolors.ENDC)
"""
Marzal Varó, A. García Sevilla, P. y Gracia Luengo, I. (2016). 
Introducción a la programación con Python 3:
( ed.). Castelló de la Plana, 
Spain: D - Universitat Jaume I. Servei de Comunicació i Publicacions. 
Recuperado de https://elibro.net/es/ereader/ipp/51760?page=129.
Edición: Pablo Rodríguez R.
"""