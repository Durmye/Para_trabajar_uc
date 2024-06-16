from typing import Generator
from functools import reduce
from itertools import combinations
import auxiliares_gen as gen_aux

def animales_segun_edad(generador_animales: Generator,
    comparador: str, edad: int) -> Generator:
    if comparador == "<": 
        return map(lambda animal: animal.nombre, 
                   filter(lambda animal: animal.edad < edad, generador_animales))
    elif comparador == ">": 
        return map(lambda animal: animal.nombre, 
                   filter(lambda animal: animal.edad > edad, generador_animales))
    elif comparador == "=": 
        return map(lambda animal: animal.nombre, 
                   filter(lambda animal: animal.edad == edad, generador_animales))
    
def animales_que_votaron_por(generador_votos: Generator,
    id_candidato: int) -> Generator:    
    return map(lambda voto_filtrado: voto_filtrado.id_animal_votante, 
            filter(lambda voto: voto.id_candidato == id_candidato, generador_votos))

def cantidad_votos_candidato(generador_votos: Generator,
    id_candidato: int) -> int:
    return reduce(lambda sum, element: sum + 1, 
                  filter(lambda voto: voto.id_candidato == id_candidato, generador_votos)
                  , 0)

def ciudades_distritos(generador_distritos: Generator) -> Generator:
    # Consultar. 
    generador_elementos = map(lambda distrito: distrito.provincia, generador_distritos)
    
    return reduce(lambda conjunto, nombre: conjunto.add(nombre), 
        map(lambda distrito: distrito.provincia, generador_distritos),
        set(generador_elementos))

def filtrar_especies_postulantes(generador_especies: Generator) -> Generator:
    especies_unicas = list(set(generador_especies))
    for especie in especies_unicas: 
        yield especie

def especies_postulantes(generador_candidatos: Generator,
    postulantes: int) ->Generator:

    lista_candidatos = [candidato for candidato in generador_candidatos]

    generador_especies = map(lambda candidato: candidato.especie, gen_aux.candidatos(lista_candidatos))
    especies_unicas = filtrar_especies_postulantes(generador_especies)
    
    for nombre_especie in especies_unicas: 
        generador_especies = map(lambda candidato: candidato.especie, gen_aux.candidatos(lista_candidatos))
        resultado = reduce(lambda sum, especie: sum + 1 if especie == nombre_especie else sum + 0,
                           generador_especies, 0)
        if resultado >= postulantes:
            yield nombre_especie
    
def pares_candidatos(generador_candidatos: Generator) -> Generator:
    
    generador_nombres = map(lambda candidato: candidato.nombre, generador_candidatos)
    for element in combinations(generador_nombres, 2):
        yield element
    
def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
    local: int) -> Generator:
    
    return filter(lambda voto: voto if voto.id_candidato == candidato and voto.id_local == local
                  else False, 
           generador_votos)

def locales_mas_votos_comuna (generador_locales: Generator,
    cantidad_minima_votantes: int, id_comuna: int) -> Generator:
    return map(lambda local: local.id_local, 
                filter(lambda local: local if len(local.id_votantes) >= cantidad_minima_votantes 
                  and local.id_comuna == id_comuna else False, generador_locales
                  ))

def votos_candidato_mas_votado(generador_votos: Generator) -> Generator: 
    
    '''
    # Paso 1: Obtener todos los ids de los candidatos
    # Paso 2: Obtener la cantidad de votos de cada candidato
    # Paso 3: Obtener el id del candidato mas votado
    # Paso 4: Retornar los votos del candidato mas votado. 
    '''

    pass
