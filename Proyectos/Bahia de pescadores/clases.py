class Bahia:

    def __init__(self, jugadores: list,
                 nombre: str, costo_vida: int) -> None:
        
        #Como implementar eficiencia de pesca? 
        #Funciones de crecimiento y decrecimiento de la bahia

        self.jugadores = jugadores
        self.nombre = nombre 
        
        self.valor_pescado = 1000

        self._poblacion = 100
        self._tasa_crecimiento = 1.2
        self._tasa_muerte = 0.1
        self._costo_vida = costo_vida


        @property
        def poblacion(self):
            return self._poblacion
        
        @poblacion.setter
        def poblacion(self, p):
            if p > 150: 
                self._poblacion = 150
            elif p < 0:
                print(f"Los peces se han extinguido en la bahia :C")
                self._poblacion = 0
            else: 
                self._poblacion = p

        def pasar_turno(self):
            for jugador in jugadores: 
                cantidad_pesca = input(f"Pescado a capturar el dia de hoy por {jugador.nombre}: ")
                ganancia = jugador.pescar(cantidad_pesca, self.valor_pescado)



class Jugador:
    def __init__(self, nombre: str,
                 dinero: int,) -> None:

        self.nombre = nombre 
        self.lanchas = 0

        self._dinero = 3000

        @property 
        def dinero(self):
            return self._dinero 
        @dinero.setter
        def dinero(self, p):
            if p < 0: 
                self._dinero = 0
            else: 
                self._dinero = p   

    def pescar(self, cantidad_pesca, valor_pescado):

        # Calcula ganancia del jugador durante el turno.
        ganancia =  valor_pescado * cantidad_pesca
        self._dinero += ganancia 
        return ganancia

    def pasar_turno(self, costos_vida):
        self.dinero -= costos_vida
        






        