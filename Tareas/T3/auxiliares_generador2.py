import auxiliares_gen as gen_aux
import auxiliares_generador1 as gen_1
from typing import Generator
from functools import reduce
from itertools import compress

def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:
    
    diccionario_edades = {ponderador.especie:float(ponderador.ponderador) 
                          for ponderador in generador_ponderadores}
    
    if comparador == ">":
        return map(lambda animal: animal.nombre,
            filter(lambda animal: animal if animal.edad * diccionario_edades[animal.especie] > edad
                   else False, generador_animales))
        
    if comparador == "<":
        return map(lambda animal: animal.nombre,
            filter(lambda animal: animal if animal.edad * diccionario_edades[animal.especie] < edad 
                   else False, generador_animales))
        
    if comparador == "=":
        return map(lambda animal: animal.nombre,
            filter(lambda animal: animal if animal.edad * diccionario_edades[animal.especie] == edad
                   else False, generador_animales))

def animal_mas_viejo_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator) -> Generator:
    
    # Paso 1: Sacar edades humanes  ---> animales_segun_edad_humana
    # Paso 2: Obtener edad mayor    ---> filtro 
    # Paso 3: Obtener nombres de los animales que cumplen con la edad mayor

    lista_animales = [animal for animal in generador_animales]
    diccionario_ponderadores = {ponderador.especie:float(ponderador.ponderador) 
                        for ponderador in generador_ponderadores}

    edad = max(lista_animales, key=lambda a: a.edad*diccionario_ponderadores[a.especie])
    return map(lambda animal: animal.nombre,
                  filter(lambda animal: animal.edad*diccionario_ponderadores[animal.especie] == 
                  edad.edad*diccionario_ponderadores[edad.especie], 
                  gen_aux.animales(lista_animales)))
    
def votos_por_especie(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    pass

def hallar_region(generador_distritos: Generator,
    generador_locales: Generator, id_animal: int) -> str:

    generador_id_comuna = map(lambda local: local.id_comuna, 
                    filter(lambda local: local if id_animal in local.id_votantes else False, 
                            generador_locales))
    
    id_comuna = next(generador_id_comuna)

    return next(map(lambda distrito: distrito.region, 
        filter(lambda distrito: distrito if distrito.id_comuna == id_comuna else False, 
                generador_distritos)))

def max_locales_distrito(generador_distritos: Generator,
    generador_locales: Generator) -> Generator:
    pass

def votaron_por_si_mismos(generador_candidatos: Generator, 
                          generador_votos: Generator) -> Generator:
    pass
    
    #for candidato in generador_candidatos:
        #filter(lambda voto: voto if candidato.id_candidato == voto.id_candidato and 
                                    #)

def ganadores_por_distrito(generador_candidatos: Generator, 
                           generador_votos: Generator) -> Generator:
    pass