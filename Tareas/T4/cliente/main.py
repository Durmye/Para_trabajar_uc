'''
Tiempo total utilizado en el cliente: 
14/06 -> 2 horas
15/06 -> 2 horas 20 min 
20/06 -> 6 horas
21/06 -> 6 horas


*Pagina de incio terminada* 

'''

from PyQt6.QtWidgets import QApplication 
from frontend.ventana_inicio import VentanaPrincipal
from frontend.ventana_juego import VentanaJuego
from backend.cliente import Cliente
import sys 

class Programa: 
    def __init__(self, puerto): 
        
        ## Frontend
        self.ventana_inicio = VentanaPrincipal()

        ## Backend
        self.cliente = Cliente(1, 2)

        ## Servidor
        self.puerto = int


    def iniciar(self):
        self.conectar_senales_1()
        self.ventana_inicio.show()
        

    def conectar_senales_1(self):

        # Inicio de juego 
        self.ventana_inicio.senal_abrir_juego.connect(
            self.cliente.iniciar_juego)
            ## Instancia la ventana de juego 
        self.cliente.senal_iniciar_juego.connect(
            self.instanciar_ventana_juego)
        
    def conectar_senales_2(self):
        # Movimiento de pepa 
        self.ventana_juego.senal_movimiento_pepa.connect(
            self.cliente.actualizar_pepa)

        # Interaccion de pepa con el mapa 
        self.ventana_juego.senal_interaccion_casilla.connect(
            self.cliente.actualizar_mapa)
        
        # Salir de las ventanas 
            # Salir ventana juego
        self.ventana_juego.senal_cerrar_ventana.connect(
            self.salir_venatana_juego)
        
            # Salir ventana inicio 
        self.ventana_inicio.senal_cerrar_juego.connect(
            self.salir_ventana_incio)
        
    def instanciar_ventana_juego(self, nombre_archivo): 
        self.ventana_juego = VentanaJuego(nombre_archivo)
        self.conectar_senales_2()
        self.ventana_inicio.hide()
        self.ventana_juego.show()

    def salir_venatana_juego(self): 
        self.ventana_juego.hide()
        self.ventana_inicio.show()

    def salir_ventana_incio(self): 
        sys.exit(aplicacion.exec())


if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    if len(sys.argv) < 2:
        print("Error en la syntaxis al ejectuar el programa")
    elif not sys.argv[1].isnumeric():
        print("Recuerda especificar un puerto.")
    else:
        puerto = int(sys.argv[1])
        aplicacion = QApplication([])
        juego = Programa(puerto)
        juego.iniciar()
        sys.exit(aplicacion.exec())