import red
import os
import sys
import auxiliares as aux
import dcciudad as dcc

if len(sys.argv) != 3: 
    print("Cantidad de comandos de linea inadecuados, saliendo programa...")
    sys.exit(1)
else:
    pass

if __name__ == "__main__": 
    ruta = os.path.join("data", sys.argv[1])
    
    ## Revisa existencia del archivo 
    metro = red.RedMetro([], [])
    if os.path.exists(ruta): 
        print("La red de metro ha sido cargada")
    else: 
        print("Lo sentimos, su red de metro no existe :C")
        sys.exit(1) 
    metro.cambiar_planos(sys.argv[1])
    if sys.argv[2] in metro.estaciones:
            print(f"La estacion {sys.argv[2]} a sido seleccionada")
    else:
        print(f"La estacion {sys.argv[2]} no fue encontrada.")
        sys.exit(1)
    print("-"*30)
    print("")
    print("¡Bienvenido al menu de acciones!")
    print("Para ejecutar una opcion ingresa el numero de opcion")
    print("")
    print("-"*30)
    aux.imprimir_opciones()
    while True:
        
        usuario = input("Selecione una opcion del 1 al 4: ")
        if usuario == str(1): 
            print("")
            dcc.imprimir_red(metro.red, metro.estaciones)
            aux.imprimir_opciones()
        
        
        elif usuario == str(2):
            print("")
            print(f"El ciclo mas corto corresponde a: {metro.ciclo_mas_corto(sys.argv[2])}")
            aux.imprimir_opciones()


        elif usuario == str(3):
            
            # Solicita y maneja casos de destino
            print("")
            print("Seleccione una de las siguientes estaciones: ")
            for i in range(1, len(metro.estaciones)+1):
                print(f"{i}.- {metro.estaciones[i-1]}")
            destino = input("Ingrese el numero de su selección: ")

            loop = True
            while loop:
                if destino.isnumeric():
                    destino = int(destino)
                    if destino >= 1 and destino <= len(metro.estaciones):
                        loop = False
                    else: 
                        destino = input(f"Por favor ingrese valor entre 1 y {len(metro.estaciones)}: ")
                else: 
                    destino = input(f"Por favor ingrese valor entre 1 y {len(metro.estaciones)}: ")
            
            # Solicita y maneja casos de p_intermedias
            p_intermedias = input("Ingrese la cantidad de paradas intermedias deseadas : ")    

            loop = True
            while loop: 
                if p_intermedias.isnumeric(): 
                    p_intermedias = int(p_intermedias)
                    if p_intermedias >= 0:
                        loop = False    
                    else:
                        p_intermedias = input("Por favor ingrese valor mayor o igual a 0 ")
                else:
                    p_intermedias = input("Por favor ingrese valor mayor o igual a 0: ")
            
            #Ejecuta funcion
            print("")
            print(metro.asegurar_ruta(sys.argv[2], destino-1, p_intermedias))

            #Vuelve a menu 
            aux.imprimir_opciones()


        elif usuario == str(4):
            print("")
            print("Cerrando programa, ¡Adios!")
            sys.exit(0)


        else: 
            
            aux.imprimir_opciones()
            print("")
            print("-"*20)
            print("")
            print("Por favor ingrese un valor del 1 al 4")
            print("")
            print("-"*20)
            print("")
