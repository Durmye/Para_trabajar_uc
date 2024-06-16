import os



def puntaje(tiempo_restante, n, m, CONSTANTE, tiempo_utilizado) -> float: 
    #Devuelve valor de puntaje aproximado a dos decimales
    puntaje = (tiempo_restante * n * m * CONSTANTE) / tiempo_utilizado
    puntaje = round(puntaje, 2)
    return puntaje

def nombre_alphanum(nombre_usuario) -> bool: 
    pass


### Funciones de puntajes
## Funciones para mostrar puntajes en salon de la fama 
def leer_puntajes() -> list: 
    puntajes = []
    ruta = os.path.join("puntaje.txt")
    with open(ruta, "r") as ptjs_file: 
        ptjs_list = ptjs_file.readlines()
        for ptj in ptjs_list: 
            ptj_list = ptj.rstrip("\n").split(",")
            puntajes.append(ptj_list)
    return puntajes

def ordenar_puntajes(lista_puntajes) -> list: 
    sorted(lista_puntajes, key = lambda ptj: ptj[1])
    return lista_puntajes
## Funciones para guardar puntajes en el salon de la fama



# 
