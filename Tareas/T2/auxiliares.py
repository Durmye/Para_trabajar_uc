import clases as c
import subclases as sub
import os
from parametros import PRECIO_MAG, PRECIO_GUE, PRECIO_CAB, \
    PRECIO_ARMADURA, PRECIO_LANZA, PRECIO_CURA, PRECIO_PERGAMINO

def iniciar_ejercitos_enemigos(nombre_archivo: str):

    ruta_relativa = os.path.join("data", nombre_archivo)

    #varaibles auxiliares
    ejercitos = []

    #lee archivo
    if os.path.exists(ruta_relativa): 
        with open(ruta_relativa) as enemigos:

            #Desempaqueta informacion del archivo
            info = enemigos.readlines() 
            for line in info: 
                ronda = c.Ejercito()
                info_guerreros = line.strip("\n").split(";")

                #Crea instancias a partir de la informacion de cada guerrero 
                for str_guerrero in info_guerreros: 
                    info_guerrero = str_guerrero.split(",")
                    
                    #Lista utilizada al instanciar guerreros
                    paquete = [info_guerrero[0],int(info_guerrero[2]),
                           int(info_guerrero[3]), int(info_guerrero[4]),
                           int(info_guerrero[5]), int(info_guerrero[6]),
                            ]

                    #Revisa que la vida este entre valores aceptados
                    if int(info_guerrero[2]) > 100 or int(info_guerrero[2]) < 0:
                        print(f"Error en los datos de archivo de unidades enemigas, vida_maxima") 
                        print("Saliendo del programa...")
                        return [False] 
                
                    #Revisa que la defensa este entre valores aceptados
                    elif int(info_guerrero[3]) > 20 or int(info_guerrero[3]) < 1:
                        print(f"Error en los datos de archivo de unidades de la tienda, defensa") 
                        print("Saliendo del programa...")
                        return [False]
                
                    #Revisa que el poder este entre valores aceptados
                    elif int(info_guerrero[4]) > 10 or int(info_guerrero[4]) < 1: 
                        print(f"Error en los datos de archivo de unidades de la tienda, poder") 
                        print("Saliendo del programa...")
                        return [False]
                
                    #Revisa que la agilidad este entre valores aceptados
                    elif int(info_guerrero[5]) > 10 or int(info_guerrero[5]) < 1: 
                        print(f"Error en los datos de archivo de unidades de la tienda, agilidad") 
                        print("Saliendo del programa...")
                        return [False]
                
                    #Revisa que la resistencia este entre valores aceptados
                    elif int(info_guerrero[6]) > 10 or int(info_guerrero[6]) < 1: 
                        print(f"Error en los datos de archivo de unidades de la tienda, resistencia") 
                        print("Saliendo del programa...")
                        return [False]
                    
                    #Revisa que la clase al guerrero a instanciar sea adecuada
                    elif   info_guerrero[1] == "GUE":
                        ronda.añadir_guerrero(sub.Guerrero(*paquete))
                    elif info_guerrero[1] == "CAB": 
                        ronda.añadir_guerrero(sub.Caballero(*paquete))
                    elif info_guerrero[1] == "MAG": 
                        ronda.añadir_guerrero(sub.Mago(*paquete))
                    elif info_guerrero[1] == "CAR":
                        ronda.añadir_guerrero(sub.Caballero_Arcano(*paquete))
                    elif info_guerrero[1] == "PAL":
                        ronda.añadir_guerrero(sub.Paladin(*paquete))
                    elif info_guerrero[1] == "MDB":
                        ronda.añadir_guerrero(sub.Mago_Batalla(*paquete))

                    #En caso de que no se cumpla la condicion anterior se sale del programa
                    else:
                        print(f"Error en los datos del archivo ingresado, tipo") 
                        print(f"Saliendo del programa...")
                        return [False]
                    
                #Añade instancia de ejercito con sus respectivos guerreros a lista "ejercitos"
                ejercitos.append(ronda)
        return [True, ejercitos] 
    
    #En caso de que no se encuentre el nombre del archivo sale del programa
    else: 
        print("Error en el nombre del archivo ingresado")
        print("Saliendo del programa...")
        return [False]
    
def iniciar_tropas_tienda(): 

    ruta_relativa = os.path.join("data", "unidades.txt")
    lista_tienda = []

    #Lee archivo
    if os.path.exists(ruta_relativa):
        with open(ruta_relativa) as shop: 
            unidades_str = shop.readlines()
            #Revisa que los datos del archivo no tengan errores
            # inicia instancias de guerreros y las agrega a la lista de la tienda
            for linea_str in unidades_str: 
                info_linea = linea_str.strip("\n").split(",")

                #lista utilizada al instanciar guerreros
                paquete = [info_linea[0],int(info_linea[2]),
                           int(info_linea[3]), int(info_linea[4]),
                           int(info_linea[5]), int(info_linea[6]),
                            ]

                #Revisa que la vida_maxima este entre valores aceptados
                if int(info_linea[2]) > 100 or int(info_linea[2]) < 0:
                    print(f"Error en los datos de archivo de unidades de la tienda, vida_maxima") 
                    print("Saliendo del programa...")
                    return [False] 
                
                #Revisa que la defensa este entre valores aceptados
                elif int(info_linea[3]) > 20 or int(info_linea[3]) < 1:
                    print(f"Error en los datos de archivo de unidades de la tienda, defensa") 
                    print("Saliendo del programa...")
                    return [False]
                
                #Revisa que el poder este entre valores aceptados
                elif int(info_linea[4]) > 10 or int(info_linea[4]) < 1: 
                    print(f"Error en los datos de archivo de unidades de la tienda, poder") 
                    print("Saliendo del programa...")
                    return [False]
                
                #Revisa que la agilidad este entre valores aceptados
                elif int(info_linea[5]) > 10 or int(info_linea[5]) < 1: 
                    print(f"Error en los datos de archivo de unidades de la tienda, agilidad") 
                    print("Saliendo del programa...")
                    return [False]
                
                #Revisa que la resistencia este entre valores aceptados
                elif int(info_linea[6]) > 10 or int(info_linea[6]) < 1: 
                    print(f"Error en los datos de archivo de unidades de la tienda, resistencia") 
                    print("Saliendo del programa...")
                    return [False]
                
                #Revisa que la clase del guerrero a instanciar sea basica
                # y agrega instancias correspondientes
                elif   info_linea[1] == "GUE":
                    lista_tienda.append(sub.Guerrero(*paquete))
                elif info_linea[1] == "CAB": 
                    lista_tienda.append(sub.Caballero(*paquete))
                elif info_linea[1] == "MAG":
                    lista_tienda.append(sub.Mago(*paquete))

                #En caso de que no se cumpla la condicion anterior sale del programa
                else: 
                    print(f"Error en los datos de archivo de unidades de la tienda, tipo") 
                    print("Saliendo del programa...")
                    return [False]
                
        return [True, lista_tienda]
    
    #En caso de que no se encuentre el archivo sale del programa
    else: 
        print("Error en el nombre del archivo ingresado")
        print("Saliendo del programa...")
        return [False]

def imprimir_menu_principal(ejercito_jugador: c.Ejercito):
    print("-"*10, "¡Bienvenido a DCCombatiente!","-"*10)
    print()
    print(f"Dinero disponible: {ejercito_jugador.oro}")
    print(f"Ronda actual: {ejercito_jugador.numero_ronda}")
    print()
    print("[1] Tienda")
    print("[2] Ejercito")
    print("[3] Combatir")
    print()
    print("[0] Salir del programa (¡sin guardado!)")

def imprimir_menu_tienda():
    print("-"*10, "¡Bienvenido a la tienda!", "-"*10)
    print("\n"*2)
    print(" "*8, "Producto", " "*5, "Precio")
    print("[1] Gato Mago      ", " "*5, f"{PRECIO_MAG}")
    print("[2] Gato Guerrero  ", " "*5, f"{PRECIO_GUE}")
    print("[3] Gato Caballero ", " "*5, f"{PRECIO_CAB}")
    print("[4] Item Armadura  ", " "*5, f"{PRECIO_ARMADURA}")
    print("[5] Item Pergamino ", " "*5, f"{PRECIO_PERGAMINO}")
    print("[6] Item Lanza     ", " "*5, f"{PRECIO_LANZA}")
    print("[7] Curar Ejercito ", " "*5, f"{PRECIO_CURA}")
    print("\n"*2)
    print("[0] Salir al menu principial")

def imprimir_menu_seleccion_gato(candidatos: list):
    
    contador = 1
    for combatiente in candidatos: 
        print(" "*5, "Clase", " "*5, "Nombre")
        print(f"[{contador}] {combatiente.tipo}  {combatiente.nombre}")
        print()
        print("[0] para cancelar compra")
        contador += 1
        
        
def combatientes_adecuados(ejercito_jugador: c.Ejercito, item: c.Item):
    if item.tipo == "Armdaura":
        for combatiente in ejercito_jugador.ejercito: 
            if combatiente.tipo == "Mago" or combatiente.tipo == "Guerrero": 
                combatientes_adecuados.append()
        if len(combatientes_adecuados) > 0: 
            return [True, combatientes_adecuados]
        else: 
            return [False]