# Tarea 3: DCCome Lechuga 🐢🍉🥬
## Consideraciones generales :octocat:

Lo implementado a grandes rasgos: 
1. Frontend (Parcial)
2. Flujo del cliente (parcial)

Lo que no se implemento a grandes rasgos: 
1. Servidor 
2. Parte de flujo del cliente

### Cosas implementadas y no implementadas 

#### Entidades: 18.5 pts (21%)
##### ✅ Pepa 
1. Se muestra consistencia con las teclas de movimiento que se presioanan, y la direccion hacia donde pepa avanza. ✅
2. El movimiento de pepa es discreto en las casillas, mientras que la animacion del movimiento es fluido y animado entre casillas ✅
3. Pepa solo se puede mover hasta chocar con los limites del tablero ✅
4. Al presionar la tecla g, mientras pepa esta en una celda llena o con lechuga, Pepa come la lechuga y deja la casilla en blanco ✅  
5. Al presionar la tecla G, mientras pepa esta en una celda vacia o blanca, pepa hace poop y posteriormente aparece una lechuga ✅ 
##### ❌ Sandías
1. Las sandias no fueron implementadas :C
2. Las sandias no fueron implementadas :C
3. Las sandias no fueron implementadas :C

#### Interfaz gráfica: 27 pts (30%)
##### ✅ Ventana Inicio
1. Se visualiza correctamente la ventana. Se muestran todos los elementos minimos solicitados en el enunciado, sin superponerse entre si. ✅ 
2. Se valida correctamente el nombre de usuario cumpla con todas las restricciones indicadas en el enunciado❌
3. Las validaciones se realizan mediante una correcta comunicacion fron-end/back-end. notificando a través de la interfaz en caso de que no se cumpla algún requisito. ❌
    - No se lleva acabo ninguna validacion.
4. La informacion del Salón de la Fama se actualiza correctamente al terminar un puzzle❌
5. El boton de salir cierra la ventana y termina el programa✅ 


##### ✅ Ventana Juego
1. Se carga correctamente la informacion del puzzle (numeros asociados a cada fila y columna) ✅ 
2. Se visualiza correctamente la informacion del juego y todos los elementos minimos. ✅
3. El tiempo restante se actualiza a medida que progresa el juego ✅
4. El botón de comprobacion, comprueba la solucion del usuario. ❌
5. El boton de pausa detien las animaciones, el tiempo de todas las entidades y oculta el tablero. ✅
6. El boton de salir cierra la ventana actual y sale del programa. 🟠
    - Sale de la ventana pero devuelve al menu principal, permitiendo iniciar otro juego nuevamente
7. Se utilizan donde corresponde locks para evitar problemas de concurrencia en la zona critica. ❌
    - No se utilizan locks en todo el programa. 
##### ❌ Fin del *puzzle*
- No implementado

#### Interacción: 13 pts (14%)
##### ❌ *Cheatcodes*
- No implementado
##### 🟠 Sonidos
1. Las acciones implementadas (comer, lechuga, poop, click sobre la sandia) tienen su sonido correspondiente correctamente integrado. 🟠
    - Sandia no implementada
- El resto no fue implementado

#### *Networking*: 20.5 pts (23%)
##### ❌ Arquitectura
- no implementado 
##### ❌ *Networking*
- no implementado 
##### ❌ Codificación y decodifición
- no implementado 


#### Archivos: 11 pts (12%)
##### 🟠 *sprites*
##### 🟠 *puzzle*
##### ❌ JSON
##### 🟠 parámetros.py

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es `main.py` en la carpeta del cliente. Se debe ingresar el puerto como argumento de linea de comandos (a pesar de que no se ocupe, !) 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt6```: ```función() / módulo```
2. ```os.path```: ```función() / módulo``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```backend.cliente```: Contiene a la clase `cliente` la cual es utilizada en `main.py` para conectar señales e interactuar con el backend
2. ```backend.funciones.py```: Hecha para mejorar la legibilidad de `cliente.py`
3. ```frontend.threads.py```: Contiene todos los threads utilizados por `ventana_juego.py`
4. `frontend.ventana_inicio.py`: Contiene la clase `ventana_inicio`
5. `frontend.ventana_juego.py`: Contiene la clase `ventana_juego` y el intento de la clase `sandia` :c
6. `frontend.funciones.py` : hecha para mejorar la legibildiad ~~ahorrar lineas de codigo~~ en los modulos "4" y "5"

## Supuestos y consideraciones adicionales

1. Pepa > punto_5: Si se presiona rapidamente "g" despues de haber comido la lechuga pepa come su "poop". Si se espera a la transformacion de esta el programa funciona de forma correcta.


Confio en el cariño del ayudante que este revisando esta tarea. 

-------

## Referencias de código externo 

Para realizar mi tarea saqué código de:

1. https://forum.qt.io/topic/139569/how-to-get-correct-screen-size-in-pyqt6/3: Utilizado para extraer el tamaño de la resolucion del usuario.

    - linea 41-44 en `ventana_juego.py`
    - linea 24-27 en `ventana_inicio.py`

2. https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/: Utilizado para crear un "scrollable" en la interfaz del usuario. 

    - linea 50-61 en `ventana_inicio.py` 

3. https://www.pythonguis.com/docs/qcombobox/: Utilizado para crear un "desplegable" en la interfaz del usuario.

    - lineas 70, 71 en `ventana_inicio.py` 


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).