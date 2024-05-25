import sys
from PyQt6.QtWidgets import QWidget, QApplication

class MiVentana(QWidget): 
    def __init__(self) -> None:
        super().__init__()

        # Definicion de la geometria de la ventana integrada en el init
        # Orden de los parametros (x_superior_izq, y_superior_izq, ancho, alto)
        
        self.setGeometry(300, 500, 300, 300) 

        # Nombre a la ventana

        self.setWindowTitle("¡Mi primera ventana!")

if __name__ == "__main__":

    """
    El codigo entre lineas comentadas corresponde a 
    una funcion que entrega el error en caso de que 
    """
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([]) #Instancia de Aplicacion
    ventana = MiVentana()  #Instancia de MiVentana, Widget
    ventana.show()         #Muestra la instancia de ventana 
    sys.exit(app.exec())   #Termina el programa al salir de la ventana.}

"""
1. La linea 28 corresponde a la creacion de una aplicacion grafica, 
    sin esta no se puede ejecutar ningun widget. Al borrar esta linea 
    el programa lanza error.

    - Si se duplica la linea el programa se cae puesto que no pueden 
    haber dos aplicaciones al mismo tiempo

    - ¿Que significa la lista dentro de QApplication? 

2. La linea 29 corresponde a la instancia de la ventana. 

    - Si esta linea esta comentada el programa lanza un error al no 
    exisitr una instancia de ventana que mostrar. 

3. La linea 30 "muestra" la ventana, es decir si esta puede estar 
    trabajando "en el fondo" sin que el usuario interactue con ella

    - Si se comenta esta linea el programa corre sin error 
    pero no muestra nada

4. Si se crea otra instancia de ventana y se le hace `instancia.show()`
    se mostraran dos ventanas en simultaneo.

5. La linea 31 es la que mantiene corriendo al progrma hasta que se cierra
    la ventana. 

    - Si esta linea no existe se crea la ventana, se muestra y rapidamente
    se cierra. Sin dar la opcion de interactuar con ella. 

"""