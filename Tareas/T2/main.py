import sys 
import auxiliares as aux
import clases as c
import subclases as sub
from parametros import PRECIO_MAG, PRECIO_GUE, \
    PRECIO_CAB, PRECIO_ARMADURA, PRECIO_LANZA, \
    PRECIO_PERGAMINO, PRECIO_CURA

#Revisa que se inicie el programa con la correcta cantidad de cla 
if len(sys.argv) != 2: 
    print("Cantidad de argumentos de linea de comando inadecuados")
    print("Saliendo del programa...")
    sys.exit(1)
else: pass

#Flujo principal del programa 
if __name__ == "__main__":
    
    #Inicia ejercitos enemigos de acuerdo a la dificultad seleccionada
    resultado_1 = aux.iniciar_ejercitos_enemigos(sys.argv[1])
    if resultado_1[0]:
        ejercitos = resultado_1[1]
        resultado_2 = aux.iniciar_tropas_tienda() 
    else: 
        sys.exit(2)

    #Inicia guerreros de la tienda desde el archivo "unidades"
    if resultado_2[0]:
        guerreros_tienda = resultado_2[1]
    else: 
        sys.exit(3)
    
    #Instancia de Ejercito del jugador 
    tienda = c.Tienda(guerreros_tienda)
    ejercito_jugador = c.Ejercito()
    while True:
        aux.imprimir_menu_principal(ejercito_jugador)
        general = input("Ingrese su eleccion: ") 
        
        if general == str(0):
            print()
            print("DCCombatientes te espera de vuelta :D")
            print("Saliendo del progrma...") 
            sys.exit(4)

        elif general == str(1):
            aux.imprimir_menu_tienda()
            while general == str(1): 

                general_tienda = input("Ingrese su eleccion: ")
                
                if general_tienda == str(0): 
                    general = 1
                elif general_tienda == str(1): 
                    tienda.comprar_guerrero("MAG", ejercito_jugador)
                elif general_tienda == str(2):
                    tienda.comprar_guerrero("GUE", ejercito_jugador)
                elif general_tienda == str(3): 
                    tienda.comprar_guerrero("CAB", ejercito_jugador)
                elif general_tienda == str(4): 
                    if tienda.comprar_item(general_tienda, ejercito_jugador):
                        print("Compra realizada con exito")
                        general = 1
                    else: 
                        general = 1
                elif general_tienda == str(5): 
                    if tienda.comprar_item(general_tienda, ejercito_jugador):
                        print("Compra realizada con exito")
                        general = 1
                    else: 
                        general = 1
                elif general_tienda == str(6): 
                    if tienda.comprar_item(general_tienda, ejercito_jugador):
                        print("Compra realizada con exito")
                        general = 1
                    else: 
                        general = 1
                elif general_tienda == str(7): 
                    if ejercito_jugador.oro >= 7: 
                        if tienda.curar_tropas(ejercito_jugador):
                            print("Tropas curadas!")
                            general = 1
                        else: 
                            general = 1
                else: 
                    general_tienda = input("Por favor ingrese un valor entre 0 y 7: ")

        elif general == str(2): 
            ejercito_jugador.presentarse()

        elif general == str(3):
            resultado = ejercito_jugador.combatir(ejercitos.pop(-1))

        else: 
            general = input("Por favor ingrese un valor entre 0 y 3")

        if ejercito_jugador.numero_ronda == 3:
            print("Haz derrotado a gatochico derrocando su ineficiente gobierno")
            print("El juego se cerrara, ¡hasta luego!")
    

