from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, \
      QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import pyqtSignal, Qt, QUrl
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPixmap, QGuiApplication, QColor
from frontend.ventana_juego import VentanaJuego
import frontend.funciones as aux
import frontend.constantes as c
from os.path import join
import sys
import time

class VentanaPrincipal(QWidget):
    senal_abrir_juego = pyqtSignal(str, str)
    senal_cerrar_juego = pyqtSignal()
    
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
        ruta_logo = join("frontend","sprites", "logo.png")
        logo_pixmap = QPixmap(ruta_logo)
        self.logo.setPixmap(logo_pixmap)
        self.logo.setScaledContents(True)


        # Botones. Listo
        self.boton_jugar = QPushButton("Jugar!", self)
        self.boton_exit = QPushButton("Salir del juego :c", self)
            ## Geometria botones. Listo
        self.boton_jugar.resize(int(ancho/16), int(largo/16))
        self.boton_exit.resize(int(ancho/16), int(largo/16))
            ## Conexion botones
        self.boton_jugar.clicked.connect(self.jugar)
        self.boton_exit.clicked.connect(self.salir)


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
        self.desplegable_puzzles = QComboBox()
        self.desplegable_puzzles.addItems(c.LISTA_PUZZLES)

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
        vbox_inferior1.addWidget(self.desplegable_puzzles)
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

        # Musica
        self.media_player = QSoundEffect(self)
        path_musica = QUrl.fromLocalFile(join("frontend", "sonidos", "musica_2.wav"))
        self.media_player.setSource(path_musica)
        self.media_player.play()

    def salir(self): 
        self.senal_cerrar_juego.emit()
        self.media_player.stop()

    def jugar(self): 
        # Emite señal de iniciar juego con los parametros: 
        #   1.- Nombre de usuario ingresado.
        #   2.- Mapa seleccionado.
        nombre_archivo = self.desplegable_puzzles.currentText()
        nombre_usuario = self.editable_usuario.text()
        self.media_player.stop()
        self.senal_abrir_juego.emit(nombre_usuario, 
                                    nombre_archivo)
