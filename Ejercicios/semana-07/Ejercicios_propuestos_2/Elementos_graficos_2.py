import sys
import os #Para encontrar ruta de imagenes
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap

class Inicio_Sesion(QWidget): 
    def __init__(self) -> None:
        super().__init__()
        self.set_carac()
    
    def set_carac(self):
        #Geometria y titulo de la ventana
        self.setGeometry(600, 100, 400, 500)
        self.setWindowTitle("Inicio de Sesion a Cumming")
        
        #imagen = QWidget.
        
        #Los widgets se añaden como atributos 
            #Qlabels
        self.usuario = QLabel("Usuario: ", self)
        self.correo = QLabel("Correo: ", self)
        self.contraseña = QLabel("Contraseña: ", self)
        self.imagen = QLabel(self)
            #Ubicacion QLabels
        self.usuario.move(15, 150)
        self.correo.move(15, 200)
        self.contraseña.move(15, 250)
        self.imagen.setGeometry(50, 10, 100, 100)

            #QLineEdit 
        self.texto_usuario = QLineEdit("", self)
        self.texto_correo = QLineEdit("", self)
        self.texto_contraseña = QLineEdit("", self)
            #Ubicacion QLineEdit
        self.texto_usuario.move(80, 150)
        self.texto_correo.move(80, 200)
        self.texto_contraseña.move(80, 250)

            #QPushButton
        self.boton = QPushButton("Ingresar", self)
        self.boton.setGeometry(80, 300, 240, 20)

            #QPixmap
        ruta = os.path.join("img", "prob-2-1.png")
        imagen = QPixmap(ruta)
        self.imagen.setPixmap(imagen)
        self.imagen.setScaledContents(True)

        # Muestra imagen 
        self.show()

if __name__ == "__main__": 

    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    inicio = Inicio_Sesion()
    sys.exit(app.exec())


"""
1. QLables, corresponden a las etiquetas
2. QLineEdit, corresponden a las lineas de texto editables por el usuario
3. QPixmap, corresponde a las imagenes. 
4. QPsuhButton, corresponde a botones

Notas: 

1. Recordar agregar "()" a metodos y funciones o estas no son ejecutadas
2. Los distintos widgets se almacenan en atributos del objeto que hereda
    de QWidget. 
    
    -QPixmap es un intermediario para cargar la imagen en la ventana, 
    se utiliza junto a QLabel. 

3. En este caso en particular sizehint se comporto de manera no ideal.
"""