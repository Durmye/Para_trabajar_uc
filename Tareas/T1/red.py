import dcciudad
import auxiliares as aux
import os

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones


    def informacion_red(self) -> list:

        # Cantidad de estaciones
        cantidad_estaciones = len(self.estaciones)

        # 1ero Selecciona fila de matriz red.
        # 2do Cuenta la cantidad de tuneles que salen de la estacion.
        # 3ro Forma la lista con las cantidad de conexiones de cada estacion. 
        lista_de_conexiones = []
        for estacion in self.red:
            contador_tuneles = 0
            for indice in range(len(self.estaciones)):
                if estacion[indice] == 1: 
                    contador_tuneles += 1
            lista_de_conexiones.append(contador_tuneles)

        return [cantidad_estaciones, lista_de_conexiones]

    def agregar_tunel(self, inicio: str, destino: str) -> int:

        # A partir de los nombres de las estaciones se obtiene la fila y la columna
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]
        
        #Se agrega tunel y se maneja situacion en la que ya existiese un tunel
        if self.red[fila][columna] == 1: 
            return -1
        else: 
            self.red[fila][columna] = 1
        
        #contar la cantidad de tuneles que quedaron en la estacion inicial
        contador = 0
        for tunel in self.red[fila]:
            if tunel == 1: 
                contador += 1

        return contador

    def tapar_tunel(self, inicio: str, destino: str) -> int:

        # A partir de los nombres de las estaciones se obtiene la fila y la columna
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]

        #Se "tapa" tunel y se maneja situacion en la que no existiese un tunel
        if self.red[fila][columna] == 0: 
            return -1
        else: 
            self.red[fila][columna] = 0
        
        #contar la cantidad de tuneles que quedaron en la estacion inicial
        contador = 0
        for istunel in self.red[fila]:
            if istunel == 1: 
                contador += 1

        return contador

    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:

        lista = aux.obtener_coordenadas(self.red, self.estaciones, estacion_1, estacion_2)
        fila = lista[0]
        columna = lista[1]
        
        #Caso en el que existe la ruta en ambas direcciones.
        if self.red[fila][columna] == 1 and self.red[columna][fila] == 1:
            return True 
        
        #Caso en el que existe la ruta a invertir. 
        elif self.red[fila][columna] == 1 and self.red[columna][fila] == 0: 
            self.tapar_tunel(self.estaciones[fila], self.estaciones[columna])
            self.agregar_tunel(self.estaciones[columna], self.estaciones[fila])
            return True

        elif self.red[columna][fila] == 1 and self.red[fila][columna] == 0:
            self.tapar_tunel(self.estaciones[columna], self.estaciones[fila])
            self.agregar_tunel(self.estaciones[fila], self.estaciones[columna])
            return True 
        else: 
            return False

    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]

        alcanzable = dcciudad.alcanzable(self.red, fila, columna)

        if alcanzable:
            if self.red[fila][columna] == 1: 
                msg = "túnel directo"
                return msg
            elif len(self.estaciones_intermedias(inicio, destino)) >= 1:
                msg = "estación intermedia"
                return msg
        
            else:
                for exponente in range(2, len(self.red)+1):
                    red_elevada_n = dcciudad.elevar_matriz(self.red, exponente)
                    if red_elevada_n[fila][columna] >= 1:
                        msg = "muy lejos"
                        return msg

        else: 
                msg = "no hay ruta"
                return msg 
        
    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int:
        
        #Identifica coordenadas de inicio destino a partir del str
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]
        
        #Crea y retorna la cantidad de rutas con N paradas intermedias. 
        if p_intermedias == 0:
            return self.red[fila][columna]
        elif p_intermedias >= 1:
            for linea in dcciudad.elevar_matriz(self.red, p_intermedias):
                print(linea)
            return dcciudad.elevar_matriz(self.red, p_intermedias)[fila][columna]

    def ciclo_mas_corto(self, estacion: str) -> int:
        
        # Guarda la posicion de la estación
        posicion = int()
        for indice in range(len(self.red)):
            if self.estaciones[indice] == estacion:
                posicion = indice

        # Si es que existe un tunel desde estacion -> estacion se retorna 0
        if self.red[posicion][posicion] == 1: 
            return 0
        # Se comprueba la existencia de una ruta con rutas intermedias.
        else:
            for ruta_intermedia in range(1, len(self.red)):
                #Se utiliza un "+1" puesto que el metodo elevar_matriz acepta en su parametro numeros >= 2
                if dcciudad.elevar_matriz(self.red, ruta_intermedia+1)[posicion][posicion] != 0: 
                    return ruta_intermedia
            return -1

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        
        #Identifica coordenadas de inicio/destino a partir del str
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]


        # Se agrega a la lista "conexiones_inicio" el indice de las estaciones
        # que tienen un tunel desde inicio 
        conexiones_inicio = []
        for conexion_desde_inicio in range(len(self.red)):
            if self.red[fila][conexion_desde_inicio] == destino or self.red[fila][conexion_desde_inicio] == inicio: 
                None
            elif self.red[fila][conexion_desde_inicio] == 1:
                conexiones_inicio.append(conexion_desde_inicio)
        
        # Se agrega a la lista "conexiones_a_destino" el nombre de las estaciones 
        # que tienen un tunel hacia el destino 
        conexiones_a_destino = []
        for conexion_a_destino in conexiones_inicio: 
            if self.red[conexion_a_destino][columna] == 1: 
                conexiones_a_destino.append(self.estaciones[conexion_a_destino])

        return conexiones_a_destino
    
    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        
        #Identifica coordenadas de inicio/destino a partir del str
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]

        # Variables auxiliares
        conexion_1 = []
        conexion_2 = []
        rutas_disponibles = []

        # Guarda indice de las conexiones que tiene inicio.
        for tunel_destino in range(len(self.red)):
            if self.red[fila][tunel_destino] == destino: 
                None
            elif self.red[fila][tunel_destino] == 1: 
                conexion_1.append(tunel_destino)

        # Guarda todas las rutas posibles. 
        for indice_conexion_2 in conexion_1:
            for destino_conexion_2 in range(len(self.red)):
                if self.red[indice_conexion_2][destino_conexion_2] == destino: 
                    None
                elif self.red[indice_conexion_2][destino_conexion_2] == 1: 
                    conexion_2.append([indice_conexion_2, destino_conexion_2])

        # Revisa conexion de la segunda estacion con destino.
        for ruta in conexion_2: 
            if self.red[ruta[1]][columna] == 1: 
                rutas_disponibles.append([self.estaciones[ruta[0]], self.estaciones[ruta[1]]])
        print(rutas_disponibles)
        return rutas_disponibles

    def cambiar_planos(self, nombre_archivo: str) -> bool:
        
        ruta_relativa = os.path.join("data", nombre_archivo)
        nueva_red = []
        nuevas_estaciones = []
        if os.path.exists(ruta_relativa):
            with open(ruta_relativa) as info:
                dimension = info.readline()
                for tuneles in range(int(dimension)):
                    nuevas_estaciones.append(info.readline().rstrip("\n"))
                contador = 0
                linea = []
                estaciones = info.readline().split(",")
                for tunel in range(len(estaciones)):
                    linea.append(int(estaciones[tunel]))
                    contador += 1
                    if contador % int(dimension) == 0:
                        nueva_red.append(linea)
                        linea = []
            self.red = nueva_red
            self.estaciones = nuevas_estaciones
            return True
        else: 
            return False

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        #La funcion de asegurar ruta es cerrar todas las rutas que tengan menos estaciones intermedias que p_itnermedias
        #Identificar coordenadas de inicio y destino.
        lista = aux.obtener_coordenadas(self.red, self.estaciones, inicio, destino)
        fila = lista[0]
        columna = lista[1]
        copia_red = []
        for indice in range(len(self.red)): 
            fila = []
            for sub_indice in range(len(self.red)):
                fila.append(self.red[indice][sub_indice])
            copia_red.append(fila)

            
        #Maneja caso en que se pida una ruta sin estaciones intermedias. 
        if p_intermedias == 0: 
            if copia_red[fila][columna] == 1: 
                return copia_red
            else: 
                return []
            
        #La unica ruta menor en p_interdias = 1 es la de la estacion a la misma estacion. 
        elif p_intermedias == 1: 
            #revisar si existen rutas con p_intermedias = 1
            if len(self.estaciones_intermedias(inicio, destino)) == 0:
                return []
            else:
                copia_red[fila][columna] = 0
                return copia_red
    
        #Casos donde se piden dos rutas intermedias
        elif p_intermedias == 2:
            temporal = self.estaciones_intermedias_avanzado(inicio, destino)
            rutas = [[]]
            for indice in range(len(self.estaciones)):
                if self.estaciones[indice] == temporal[0][0]:
                    rutas[0].append(indice)
            for indice in range(len(self.estaciones)):
                if self.estaciones[indice] == temporal[0][1]:
                    rutas[0].append(indice)
            print(f"Primer print {rutas}")
            if 0 == len(rutas):
                return []
            else: 
                for estaciones in rutas[0]:
                    for indice in range(len(self.estaciones)): 
                        if indice != estaciones and copia_red[estaciones][indice] == 1:
                            copia_red[estaciones][indice] = 0
                return copia_red 
            
        else: 
            return []

                     
