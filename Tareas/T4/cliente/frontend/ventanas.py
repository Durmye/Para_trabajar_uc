from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, \
      QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, \
      QGridLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap, QGuiApplication, QColor
import funciones as aux
import sys
import os
import constantes as c
import time

class VentanaPrincipal(QWidget):
    senal_abrir_juego = pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        
        # Nombre de la ventana. Listo
        self.setWindowTitle("DCCome Lechuga")

        # Geometria de la ventana, se adapata a la resolucion del usuario. Listo
        r_s = QGuiApplication.primaryScreen().geometry()
        ancho = r_s.width()
        largo = r_s.height()
        self.setGeometry(r_s.x(), r_s.y(), ancho, largo)


        # Logo. Listo
        self.logo = QLabel()
        ruta_logo = os.path.join("sprites", "logo.png")
        logo_pixmap = QPixmap(ruta_logo)
        self.logo.setPixmap(logo_pixmap)
        self.logo.setScaledContents(True)


        # Botones. Listo
        self.boton_jugar = QPushButton("Jugar!", self)
        self.boton_exit = QPushButton("Salir del juego :c", self)
            ## Geometria botones. Listo
        self.boton_jugar.resize(int(ancho/16), int(largo/16))
        self.boton_exit.resize(int(ancho/16), int(largo/16))

        # "Scroll" salon de la fama. Listo
        self.salon_fama_scroll = QScrollArea()
        self.salon_fama_widget = QWidget()
        self.salon_fama_vbox = QVBoxLayout()

        puntajes = aux.leer_puntajes()
        puntajes_ordenados = aux.ordenar_puntajes(puntajes)
        
        for puntaje in puntajes_ordenados: 
            posicion = QLabel(f"Nombre: {puntaje[0]}, puntaje = {puntaje[1]}")
            self.salon_fama_vbox.addWidget(posicion)

        self.salon_fama_widget.setLayout(self.salon_fama_vbox)

            ## Propiedades del scroll
        self.salon_fama_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.salon_fama_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.salon_fama_scroll.setWidgetResizable(True)
        self.salon_fama_scroll.setWidget(self.salon_fama_widget)

        # Selector de puzzles. Listo
        desplegable_puzzles = QComboBox()
        desplegable_puzzles.addItems(c.LISTA_PUZZLES)

        # Texto editable. Listo
        self.editable_usuario = QLineEdit("", self)

        # Estructura general. Listo
        vbox_superior = QVBoxLayout()
            # Agrega logo a la vertical superior 
        vbox_superior.addWidget(self.logo)
            
        hbox_inferior1 = QHBoxLayout()
            # Agrega salon de la fama a horizontal inferior
        hbox_inferior1.addWidget(self.salon_fama_scroll)

        vbox_inferior1 = QVBoxLayout()
            # Agrega elementos a vertical inferior 
        vbox_inferior1.addWidget(self.editable_usuario)
        vbox_inferior1.addWidget(desplegable_puzzles)
            # Agrega horizontal inferior 2 con elementos de ella
        hbox_inferior2 = QHBoxLayout()
        hbox_inferior2.addWidget(self.boton_jugar)
        hbox_inferior2.addWidget(self.boton_exit)
        vbox_inferior1.addLayout(hbox_inferior2)

            # Agrega vertical inferior a horizontal inferior 
        hbox_inferior1.addLayout(vbox_inferior1)
            #Agrega horizontal inferior a Estructura general
        vbox_superior.addLayout(hbox_inferior1)
        self.setLayout(vbox_superior)

        self.show()

class VentanaJuego(QWidget): 

    def __init__(self) -> None: 
        super().__init__()
        self.setWindowTitle("Puzzle")
        #Agregar geometria de la ventana utilizando resolucion adapatable 
        r_s = QGuiApplication.primaryScreen().geometry()
        ancho = r_s.width()
        largo = r_s.height()
        self.setGeometry(r_s.x(), r_s.y(), ancho, largo)
        
        ##Elementos de la ventana

        #Botonoes 
        self.pausa = QPushButton("Pausa", self)
        self.verificar = QPushButton("Verificar", self)
        self.salir = QPushButton("Salir", self)
        
        #Entidades 
        #self.pepa
        #self.lechuga
        #self.poop

        #Puzzle 
        grilla = QGridLayout()
        
        puzzle = aux.leer_base("intermedio_3")
        dimension = aux.dimension_grilla(puzzle)
        columnas = aux.obtener_columnas(puzzle)
        filas = aux.obtener_filas(puzzle)
        max_hint_columna = aux.obtener_max_columna(columnas)
        max_hint_fila = aux.obtener_max_fila(filas)

        print(f"puzzle: {puzzle}")
        print(f"dimension: {dimension}")
        print(f"columnas: {columnas}")
        print(f"filas: {filas}")
        print(f"max_hint_columna: {max_hint_columna}")
        print(f"max_hint_filas: {max_hint_fila}")

        posiciones = [(i, j) for i in range(dimension + max_hint_columna)
                      for j in range(dimension + max_hint_fila)]
        
        for i in range(len(posiciones)):
            posicion = posiciones[i]
            print(posicion[0], posicion[1])
            # Revisa que no inicie informacion dentro de cuadrado superior izquierdo
            if posicion[0] < max_hint_fila and posicion[1] < max_hint_columna: 
                pass
            # Revisa inicio de hints de columnas
            elif posicion[1] >= max_hint_fila and posicion[0] < max_hint_columna: 
                print("ALOOOOOOOOOOOOOOOooo")
                # Revisa que no se exceda indice max de la lista 
                if len(columnas[posicion[1] - max_hint_fila]) > posicion[0]: 
                    hint = QLabel(columnas[posicion[1] - max_hint_fila][posicion[0]], self)
                    grilla.addWidget(hint, *posicion)
                    print("Alo columnas!")
            # Revisa inicio de hints de filas 
            elif posicion[1] < max_hint_fila and posicion[0] >= max_hint_columna:
                #Revisa que no se exceda indice max de la lista 
                if len(filas[posicion[0] - max_hint_columna]) > posicion[1]: 
                    hint = QLabel(filas[posicion[0] - max_hint_columna][posicion[1]], self)
                    grilla.addWidget(hint, *posicion)
                    print("Alo filas")
            # Revisa inicio del mapa.
            elif posicion[0] >= max_hint_fila and posicion[1] >= max_hint_columna: 
                casilla = QLabel()
                casilla_pixmap = QPixmap("sprites/sandia.png")
                casilla.setPixmap(casilla_pixmap)
                grilla.addWidget(casilla, *posicion)
    

        #Distribucion de la ventana a nivel general 
        secciones = QHBoxLayout()
        secciones.addLayout(grilla)

        hbox_inferior = QVBoxLayout()
        hbox_inferior.addWidget(self.verificar)
        hbox_inferior.addWidget(self.pausa)
        hbox_inferior.addWidget(self.salir)

        secciones.addLayout(hbox_inferior)
        
        self.setLayout(secciones)
        self.show()
        

    '''
    Pepa:
        Movimiento de pepa dado por: WASD
        Interaccion con casillas dado por: G
        Interaccion con sandias dado por: click
    CheatCodes: 
        I + N + F = tiempo infinito, setea puntaje a PUNTAJE_INF
        M + U + T + E = Desactiva el uso de todos los sonidos durante
                        la partida acutal 
    
    '''

if __name__ == "__main__":
    def hook(type_, value, traceback): 
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    #ventana = VentanaPrincipal()
    juego = VentanaJuego()
    sys.exit(app.exec())