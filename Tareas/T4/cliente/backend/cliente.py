from PyQt6.QtCore import QObject, pyqtSignal
from threading import Thread
import backend.funciones as aux
import socket


class Cliente(QObject):
    
    senal_verificar = pyqtSignal(list)
    senal_iniciar_juego = pyqtSignal(str)
    

    def __init__(self, host, puerto): 
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.puerto = puerto

        self.posicion_pepa = [0,0]

    def iniciar_juego(self, nombre_usuario, nombre_archivo_mapa):
        # Guardo nombre de usuario en atributo y obtengo informacion del mapa
        #   Se envia señal para iniciar ventana de juego
        self.nombre_usuario = nombre_usuario 
        self.nombre_mapa = nombre_archivo_mapa
        self.dimension = aux.leer_base(self.nombre_mapa)
        self.mapa = self.instanciar_mapa(self.dimension)
        self.senal_iniciar_juego.emit(self.nombre_mapa)

    def instanciar_mapa(self, dimension): 
        # Se crea lista de lista con todos sus elementos 
        #   iguales a 1. Simulando el mapa con las lechugas 
        #   disponibles
        mapa = []
        for _ in range(self.dimension): 
            fila = []
            for i in range(self.dimension): 
                fila.append(1)
            mapa.append(fila)
        return mapa

    def establecer_conexion_servidor(self): 
        try: 
            self.socket.connect((self.host, self.puerto))
            #thread = Thread(target=,
            #                args=,
            #                daemon= True)
        except ConnectionError: 
            self.cerrar_programa

    def actualizar_pepa(self, x: int, y: int):
        self.posicion_pepa[0] = x
        self.posicion_pepa[1] = y 

    def actualizar_mapa(self, x, y): 
        # Recibe señal del frontend y actualiza el mapa en la memoria del cliente
        if self.mapa[x][y] == 1: 
            self.mapa[x][y] = 0

        elif self.mapa[x][y] == 0: 
            self.mapa[x][y] = 1

    def verificar_puzzle(self): 
        pass

    def recicibir_solucion(self):
        pass

