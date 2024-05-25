from typing import List
from clases import Tortuga
import pickle


###################
#### ENCRIPTAR ####
###################

def serializar_tortuga(tortuga: Tortuga) -> bytearray:
    # Completar
    try:
        tortuga_serializada = pickle.dumps(tortuga)
    except AttributeError: 
        raise ValueError("Parametro debe ser de la clase \"Tortuga\"")
    return bytearray(tortuga_serializada)


def verificar_rango(mensaje: bytearray, inicio: int, fin: int) -> None:
    # Completar
    if inicio > fin or len(mensaje) < fin or inicio < 0: 
        raise AttributeError("Error en el rango entregado")
    else: 
        return None        

def codificar_rango(inicio: int, fin: int) -> bytearray:
    # Completar
    inicio_codificado = inicio.to_bytes(3, "big")
    fin_codificado = fin.to_bytes(3, "big")
    rango_codificado = bytearray(inicio_codificado + fin_codificado)
    return bytearray(rango_codificado)

def codificar_largo(largo: int) -> bytearray:
    # Completar
    largo_codificado = bytearray(largo.to_bytes(3, "big"))
    return largo_codificado


def separar_msg(mensaje: bytearray, inicio: int, fin: int) -> List[bytearray]:
    m_extraido = bytearray()
    m_con_mascara = bytearray()
    # Completar
    
    # Primer array
    largo = fin - inicio + 1
    # Si es impar
    if largo % 2 == 1:  
        m_extraido = mensaje[inicio:fin+1]
        m_extraido.reverse()
        print(m_extraido)
    # Si es par    
    else: 
        m_extraido = mensaje[inicio:fin+1]

    # Segundo Array
    m_con_mascara = mensaje
    contador = 0 
    for i in range(inicio, fin+1):
        m_con_mascara[i] = contador
        contador += 1

    return [m_extraido, m_con_mascara]


def encriptar(mensaje: bytearray, inicio: int, fin: int) -> bytearray:
    # No modificar
    verificar_rango(mensaje, inicio, fin)

    m_extraido, m_con_mascara = separar_msg(mensaje, inicio, fin)
    rango_codificado = codificar_rango(inicio, fin)
    return (
        codificar_largo(fin - inicio + 1)
        + m_extraido
        + m_con_mascara
        + rango_codificado
    )


######################
#### DESENCRIPTAR ####
######################
def deserializar_tortuga(mensaje_codificado: bytearray) -> Tortuga:
    # Completar
    try:
        tortuga = pickle.loads(mensaje_codificado)
    except ValueError: 
        raise AttributeError("Mensaje!")
    return tortuga


def decodificar_largo(mensaje: bytearray) -> int:
    # Completar
    largo_rango_bytes = mensaje[0:3]
    largo_rango = int.from_bytes(largo_rango_bytes, byteorder="big")    
    return largo_rango


def separar_msg_encriptado(mensaje: bytearray) -> List[bytearray]:
    m_extraido = bytearray()
    m_con_mascara = bytearray()
    rango_codificado = bytearray()
   
    # Completar

    # Decodifica largo
    largo = decodificar_largo(mensaje)
    print(largo)
    
    #Extrae el rango, siempre son los ultimos 6 elementos de la lista
    rango_codificado = mensaje[len(mensaje)-6:]

    #Extrae los bytes del mensaje original
    m_extraido = mensaje[3:largo+3]
    #Invierte el orden de ser necesario.
    if len(m_extraido) % 2 == 1: 
        m_extraido.reverse()
    
    #Extrae el mensaje con mascara 
    m_con_mascara = mensaje[largo+3:-6]

    return [m_extraido, m_con_mascara, rango_codificado]


def decodificar_rango(rango_codificado: bytearray) -> List[int]:
    inicio = None
    fin = None
    # Completar
    inicio_codificado = rango_codificado[:3]
    fin_codificado = rango_codificado[3:]

    inicio = int.from_bytes(inicio_codificado, byteorder="big")
    fin = int.from_bytes(fin_codificado, byteorder="big")

    return [inicio, fin]


def desencriptar(mensaje: bytearray) -> bytearray:
    # Completar
    m_extraido, m_con_mascara, rango_codificado = separar_msg_encriptado(mensaje)

    inicio, fin = decodificar_rango(rango_codificado)

    m_con_mascara[inicio: fin+1] = m_extraido

    #En realidad ahora no tiene mascara, pero bueno.
    return m_con_mascara 


if __name__ == "__main__":
    # Tortuga
    tama = Tortuga("Tama2")
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)
    print(tama.celebrar_anivesario())
    print()

    # Encriptar
    original = serializar_tortuga(tama)
    print("Original: ", original)
    encriptado = encriptar(original, 6, 24)
    print("Encriptado: ", encriptado)
    print()

    # Desencriptar
    mensaje =  bytearray(b'\x00\x00\x13roT\x07\x8c\x94sesalc\x06\x8c\x00\x00\x00\x00\x00\x80\x04\x958\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12tuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x05Tama2\x94\x8c\x04edad\x94K\x01ub.\x00\x00\x06\x00\x00\x18')
    desencriptado = desencriptar(mensaje)
    tama = deserializar_tortuga(desencriptado)

    # Tortuga
    print("Tortuga: ", tama)
    print("Nombre: ", tama.nombre)
    print("Edad: ", tama.edad)