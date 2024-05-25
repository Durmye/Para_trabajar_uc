from abc import ABC, abstractmethod
import auxiliares as aux 
from parametros import ORO_INICIAL, ORO_GANADO, \
    PRECIO_MAG, PRECIO_GUE, PRECIO_CAB, PRECIO_PERGAMINO, \
    PRECIO_ARMADURA, PRECIO_LANZA, PRECIO_CURA, CURAR_VIDA

class Tienda: 
    def __init__(self, lista_guerreros: list) -> None:

        #Atributos 
        self.precio_mago = PRECIO_MAG
        self.precio_guerrero = PRECIO_GUE
        self.precio_caballero = PRECIO_CAB
        self.precio_pergamino = PRECIO_PERGAMINO
        self.precio_armadura = PRECIO_ARMADURA
        self.precio_lanza = PRECIO_LANZA
        self.precio_cura = PRECIO_CURA
        self.cantidad_cura = CURAR_VIDA

        self.lista_guerreros = lista_guerreros

    def comprar_guerrero(self, tipo: str, ejercito_jugador):

        if tipo == str(1): 
            for mago in self.lista_guerreros: 
                contador = 0
                if mago.tipo == "MAG": 
                    if ejercito_jugador.oro >= self.precio_mago:
                        ejercito_jugador.oro -= self.precio_mago
                        ejercito_jugador.append(mago)
                        self.lista_guerreros.pop(contador)
                        return True
                    else: 
                        print("No dispones de suficiente dinero :c")
                        return False
                else: 
                    pass
            print("No quedan guerreros de este tipo :C")
            return False

        elif tipo == str(2):
            contador = 0
            for guerrero in self.lista_guerreros: 
                if guerrero.tipo == "GUE": 
                    if ejercito_jugador.oro >= self.precio_guerrero:
                        ejercito_jugador.oro -= self.precio_guerrero
                        ejercito_jugador.append(guerrero)
                        self.lista_guerreros.pop(contador)
                        return True 
                    else: 
                        print("No dispones de suficiente dinero :c")
                        return False 
                else: 
                    pass
            print("No quedan guerreros de este tipo :C")
            return False

        elif tipo == str(3): 
            contador = 0
            for caballero in self.lista_guerreros: 
                if caballero.tipo == "CAB": 
                    if ejercito_jugador.oro >= self.precio_caballero:
                        ejercito_jugador.oro -= self.precio_caballero
                        ejercito_jugador.append(caballero)
                        self.lista_guerreros.pop(contador)
                        return True
                    else: 
                        print("No dispones de suficiente dinero :c")
                        return False
                else: 
                    pass
                contador += 1
            print("No quedan guerreros de este tipo :C")
            return False

    #Completar
    def comprar_item(self, item: str, ejercito_jugador):
        #El string item, corresponde a la variable general_tienda (main.py)
        if item == str(4) and ejercito_jugador.oro >= PRECIO_ARMADURA: 
            #inicializa item necesario para utilizar el metodo evolucionar
            armadura = Item("Armadura", self.precio_armadura)
            # Se verifica que exista guerrero adecuado para el item
            resultados = aux.combatientes_adecuados(ejercito_jugador, armadura)
            if resultados[0]:
                # Se imprime menu de seleccion de gato
                aux.imprimir_menu_seleccion_gato()
                seleccion = input("Seleccione el gato a evolucionar: ")
                #Loop hasta seleccionar opcion disponible o salir de la compra
                while seleccion != str(0):
                    if int(seleccion) > len(resultados[1]) or int(seleccion) < 1:
                        seleccion = input("Por favor ingrese una opcion valida: ")
                    elif seleccion == str(0): 
                        pass
                    else:
                        #Busca al combatiente a reemplazar utilizando el nombre
                        escogido = resultados[1][int(seleccion)-1]
                        contador = 0
                        for combatiente in ejercito_jugador.ejercito: 
                            #Una vez encontrado reemplaza al combatiente por su evolucion
                            # manteniendo los stats del original
                            if escogido.nombre == combatiente.nombre:
                                a_evolucionar = ejercito_jugador.ejercito.pop(contador)
                                resultado_2 = a_evolucionar.evolucionar(armadura)
                                ejercito_jugador.ejercito.insert(resultado_2[1], contador)
                                ejercito_jugador.oro -= self.precio_armadura
                                return True
                            contador += 1
            else: 
                print("No se puede llevar acabo la accion :c")
                return False
            
        #El string item, corresponde a la variable general_tienda (main.py)
        elif item == str(5): 
            #inicializa item necesario para utilizar el metodo evolucionar
            pergamino = Item("Pergamino", self.precio_armadura)
            # Se verifica que exista guerrero adecuado para el item
            resultados = aux.combatientes_adecuados(ejercito_jugador, pergamino)
            if resultados[0] and ejercito_jugador.oro >= PRECIO_PERGAMINO:
                # Se imprime menu de seleccion de gato
                aux.imprimir_menu_seleccion_gato()
                seleccion = input("Seleccione el gato a evolucionar: ")
                #Loop hasta seleccionar opcion disponible o salir de la compra
                while seleccion != str(0):
                    if int(seleccion) > len(resultados[1]) or int(seleccion) < 1:
                        seleccion = input("Por favor ingrese una opcion valida: ")
                    elif seleccion == str(0): 
                        pass
                    else:
                        #Busca al combatiente a reemplazar utilizando el nombre
                        escogido = resultados[1][int(seleccion)-1]
                        contador = 0
                        for combatiente in ejercito_jugador.ejercito: 
                            #Una vez encontrado reemplaza al combatiente por su evolucion
                            # manteniendo los stats del original
                            if escogido.nombre == combatiente.nombre:
                                a_evolucionar = ejercito_jugador.ejercito.pop(contador)
                                resultado_2 = a_evolucionar.evolucionar(armadura)
                                ejercito_jugador.ejercito.insert(resultado_2[1], contador)
                                ejercito_jugador.oro -= self.precio_armadura
                                return True
                            contador += 1
            else: 
                print("No se puede llevar acabo la accion :c")
                return False


        #El string item, corresponde a la variable general_tienda (main.py)
        elif item == str(6): 
            #inicializa item necesario para utilizar el metodo evolucionar
            lanza = Item("Lanza", self.precio_armadura)
            # Se verifica que exista guerrero adecuado para el item
            resultados = aux.combatientes_adecuados(ejercito_jugador, lanza)
            if resultados[0] and ejercito_jugador.oro >= PRECIO_PERGAMINO:
                # Se imprime menu de seleccion de gato
                aux.imprimir_menu_seleccion_gato()
                seleccion = input("Seleccione el gato a evolucionar: ")
                #Loop hasta seleccionar opcion disponible o salir de la compra
                while seleccion != str(0):
                    if int(seleccion) > len(resultados[1]) or int(seleccion) < 1:
                        seleccion = input("Por favor ingrese una opcion valida: ")
                    elif seleccion == str(0): 
                        pass
                    else:
                        #Busca al combatiente a reemplazar utilizando el nombre
                        escogido = resultados[1][int(seleccion)-1]
                        contador = 0
                        for combatiente in ejercito_jugador.ejercito: 
                            #Una vez encontrado reemplaza al combatiente por su evolucion
                            # manteniendo los stats del original
                            if escogido.nombre == combatiente.nombre:
                                a_evolucionar = ejercito_jugador.ejercito.pop(contador)
                                resultado_2 = a_evolucionar.evolucionar(armadura)
                                ejercito_jugador.ejercito.insert(resultado_2[1], contador)
                                ejercito_jugador.oro -= self.precio_armadura
                                return True
                            contador += 1
            else: 
                print("No se puede llevar acabo la accion :c")
                return False
        
        else: 
            print("No se puede llevar acabo la accion :c")
            return False

    def curar_tropas(self, ejercito_jugador):
        if len(ejercito_jugador.ejercito) > 0:
            for guerrero in ejercito_jugador.ejercito:
                guerrero.curarse(CURAR_VIDA)
            return True 
        else: 
            print("No tienes ningun guerrero que curar!")
            return False

class Item:
    def __init__(self, nombre: str,
                 valor: int) -> None:
        self.nombre = nombre
        self.valor = valor

    #Completar
    def utilizar(self, guerrero):
        pass

class Combatiente(ABC):
    def __init__(self, 
                 nombre: str, vida_maxima: int, 
                 poder: int, defensa: int, 
                 agilidad: int, resistencia: int,
                ) -> None:
        #
        #Propertys 
        #
        self._vida_maxima = vida_maxima
        self._poder = poder
        self._defensa = defensa
        self._agilidad = agilidad
        self._resistencia = resistencia

        self._vida = self.vida_maxima


        #
        #Atributos 
        #
        self.nombre = nombre 
        self.tipo = ""

    @property
    def ataque(self):
        return round( (self.poder + self.agilidad + self.resistencia) * ((2 * self.vida) / self.vida_maxima) )

    @property
    def vida_maxima(self):
        #La primera linea de esta property se asegura de siempre entregar un valor adecuado
        self._vida_maxima = self._vida_maxima
        return self._vida_maxima
    @vida_maxima.setter
    def vida_maxima(self, p): 
        if p > 100: 
            self._vida_maxima = 100
        elif p < 0 : 
            self._vida_maxima = 0
        else: 
            self._vida_maxima = p

    @property
    def vida(self):
        #la primera linea de esta property se asegura de siempre entregar un valor adecuado
        self.vida = self._vida
        return self._vida 
    @vida.setter
    def vida(self, p):
        if p > self.vida_maxima:
            self._vida = self.vida_maxima
        elif p < 0: 
            self._vida = 0
        else: 
            self._vida = p

    @property 
    def poder(self):
        #la primera linea de esta property se asegura de siempre entregar un valor adecuado
        self.poder = self._poder
        return self._poder
    @poder.setter
    def poder(self, p):
        if p > 10:
            self._poder = 10
        elif p < 1:
            self._poder = 1
        else: 
            self._poder = p
    
    @property
    def defensa(self):
        #la primera linea de esta property se asegura de siempre entregar un valor adecuado
        self.defensa = self._defensa
        return self._defensa
    @defensa.setter
    def defensa(self, p):
        if p > 20:
            self._defensa = 20
        elif p < 1: 
            self._defensa = 1
        else: 
            self._defensa = p
    
    @property
    def agilidad(self):
        #la primera linea de esta property se asegura de siempre entregar un valor adecuado
        self.agilidad = self._agilidad
        return self._agilidad
    @agilidad.setter
    def agilidad(self, p):
        if p > 10:
            self._agilidad = 10
        elif p < 1: 
            self._agilidad = 1
        else: 
            self._agilidad = p
    
    @property 
    def resistencia(self):
        #la primera linea de esta property se asegura de siempre entregar un valor adecuado
        self.resistencia = self._resistencia
        return self._resistencia
    @resistencia.setter
    def resistencia(self, p):
        if p > 10: 
            self._resistencia = 10 
        elif p < 1: 
            self._resistencia = 1
        else:
            self._resistencia = p

    #Metodo atacar queda por definir en cada clase. 
    @abstractmethod
    def atacar(self, guerrero):
        pass

    def curarse(self, cura): 
        self.vida += cura

    def evolucionar(self, item: Item):
        pass

    def __str__(self) -> str:
        msg = f"Mi nombre es {self.nombre}, combatiente de tipo {self.tipo}, con {self.vida} / {self.vida_maxima}, {self.ataque} y {self.defensa}"
        return msg

class Ejercito: 
    def __init__(self) -> None:

        #Atributos 
        self.ejercito = []
        self.oro = ORO_INICIAL
        self.numero_ronda = 1

    def añadir_guerrero(self, guerrero): 
        self.ejercito.append(guerrero)

    def presentarse(self):
        if len(self.ejercito) > 0: 
            print(f"** ¡El poderoso ejercito gatuno se presenta ante ti! **")
            for combatiente in self.ejercito: 
                print(combatiente) 
        elif len(self.ejercito) == 0: 
            print()
            print(f"** ¡El no existente ejercito gatuno no se puede presentar ante ti! **")
            print()
            
    def combatir(self, enemigo):

        #variables
        termino = ""
        combate = True 
        combatiente_aliado = self.ejercito.pop()
        combatiente_enemigo = enemigo.ejercito.pop()

        while combate: 
            #Mientras los combatientes sigan vivos el combate siga
            while combatiente_aliado.vida > 0 or combatiente_enemigo.vida > 0: 
                combatiente_aliado.atacar(combatiente_enemigo)
                print(f"{combatiente_aliado.nombre} a atacado a {combatiente_enemigo.nombre}")
                combatiente_enemigo.atacar(combatiente_aliado)
                print(f"{combatiente_enemigo.nombre} a atacado a {combatiente_aliado.nombre}")
            
            #Checkea si se cumplen las condiciones para perder o ganar se cumplen
            if len(self.ejercito) == 0 and combatiente_aliado.vida == 0: 
                if len(enemigo.ejercito) == 0 and combatiente_enemigo.vida == 0: 
                    combate = False
                    termino = "Empate"
                else: 
                    combate = False 
                    termino = "Derrota"
            elif len(enemigo.ejercito) == 0 and combatiente_enemigo.vida == 0:
                combate = False
                termino = "Victoria"

            #Cambia combatiente 
            if len(self.ejercito) > 0 and combatiente_aliado.vida == 0: 
                combatiente_aliado = self.ejercito.pop()
            if len(enemigo.ejercito) > 0 and combatiente_enemigo.vida == 0: 
                combatiente_enemigo = enemigo.ejercito.pop()

        self.numero_ronda += 1
        self.oro += ORO_GANADO
        return termino