# Tarea 1: DCCiudad 🚈🐈

## ¡Consideraciones generales!

1. El metodo cambiar_planos asume que el archivo a abrir esta dentro de una carpeta llamada "data" si es que no es asi el metodo no funcionara.

2. En la consola al identificar un error en los comandos de linea entregados (**no se encuentra archivo/estacion invalida**) el programa se detiene de manera automatica. 

3. Fue creada la libreria personal `auxiliares.py`, esta debe estar en el mismo directorio en el que se encuentra el archivo `main.py` de lo contrario no sera importado de manera correcta. 

    - IMPORTANTE: *LA GRAN MAYORIA DE LOS METODOS EN `red.py` UTILIZAN ESTA LIBRERIA*

### Cosas implementadas y no implementadas (づ￣ ³￣)づ

Esta parte del README esta estructurada en base a la hoja de calculo **"T1 Distribucion Puntaje"** entregado en el enunciado de la tarea.

#### 🟠 Automatización!

- RedMetro informacion_red: ¡Funciona de manera adecuada! (\~˘▾˘)\~

- RedMetro agregar_tunel: ¡Funciona de manera adecuada! (\~˘▾˘)\~

- RedMetro tapar_tunel: ¡Funciona de manera adecuada! (\~˘▾˘)\~

- RedMetro invertir_tunal: ¡Funciona de manera adecuada! (\~˘▾˘)\~

- RedMetro nivel_conexiones: ¡Falla en el test_case n°5!   ┬──┬ ノ( ゜-゜ノ)

- RedMetro rutas_posibles: ¡Funciona correctamente! (\~˘▾˘)\~

- RedMetro ciclo_mas_corto: ¡Funciona correctamente! (\~˘▾˘)\~

- RedMetro estaciones_intermedias: ¡Funciona correctamente! (\~˘▾˘)\~

- RedMetro estaciones_intermedias_avanzado: ¡Funciona correctamente! (\~˘▾˘)\~

- RedMetro cambiar_planos: Funciona correctamente siempre y cuando se cumpla la condicion detallada en las **concideraciones generales**. (ʘ‿ʘ)

- RedMetro asegurar_ruta: 
    - ¡Soluciona algunos de los casos faciles!  ┬──┬ ノ( ゜-゜ノ)
    - ¡No soluciona los casos dificiles! ┬──┬ ノ( ゜-゜ノ)
    - ¡Reconoce casos sin solución! (\~˘▾˘)\~

#### ✅¡Menú!

##### Consola 

- ¡Se puede entregar el nombre de la red y nombre de la estacion mediante argumento de consola! (\~˘▾˘)\~

- ¡Se verifica correctamente el nombre de la red y se avisa si es que este es invalido! (\~˘▾˘)\~

- ¡Se verifica correctamente el nombre de la estacion y se avisa si es que este es invalido! (\~˘▾˘)\~

##### Menú de acción

- ¡El menu de accion es aprueba de todo tipo de error! (\~˘▾˘)\~

- ¡Esta la opción de mostrar_red y llama a la funcion correspondiente del modulo dcciudad.pyc! (\~˘▾˘)\~

- ¡Esta la opción ciclo mas corto y llama al metodo correspondiente del modulo red.py! (\~˘▾˘)\~

- ¡Esta la opcion de Asegurar ruta y llama al metodo correspondiente del modulo red.py! (\~˘▾˘)\~

- ¡Esta la opcion de salir en el menu y permite cerrar el programa! (\~˘▾˘)\~

- Luego de ejecutar cada opcion distinta a salir, se vuelve al menu! (\~˘▾˘)\~

#### 🟠 Aspectos Generales!

- Modularización: ¡Ningun archivo supera las 400 lineas! (\~˘▾˘)\~
    
- PEP8
    - No exceder el maximo de 100 caracteres por linea, Duda

    - Uso de variables declarativas y aclarativas, Duda

    - ¡Uso adecuado de CamelCase y snake_case! (\~˘▾˘)\~

    - ¡Espacio despues de coma! (\~˘▾˘)\~

    - ¡Uso de espacios para indentación y no de tabulaciones!(\~˘▾˘)\~

    - ¡No se usaron variables globales! (\~˘▾˘)\~

    - Utilizar correctamente los import! (\~˘▾˘)\~


## Ejecución ♥╣[-_-]╠♥
El módulo principal de la tarea a ejecutar es  ```main.py```. 


## Librerías (͠≖ ͜ʖ͠≖)

### Librerias proporcionadas con la tarea

Desconozco si por nomenclatura los modulos `dcciudad.pyc` y `red.py` deberian estar incluidos en librerias propias o en librerias externas, por ende, quedan en esta categoria de "proporiciondas con la tarea" (a pesar de que una de ellas fue desarrollada por el autor de este README)

1. ```dcciudad.pyc```  
2. ```red.py```

### Librerías externas utilizadas

La lista de librerías externas que utilicé fue la siguiente:

1. ```os```
2. ```sys```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```auxiliares```: incluye los metodos: 
    - `obtener_coordenadas`: Utilizada en `red.py` para no repetir codigo 
    - `imprimir_menu`: Utilizada en `main.py` para no repetir codigo

## Supuestos y consideraciones adicionales ᕙ(⇀‸↼‶)ᕗ

- Sin supuestos, tarea realizada en estricto seguimiento del enunciado ᕙ(▀̿ĺ̯▀̿ ̿)ᕗ

- Consideracion adicional: El menu presenta error unicamente cuando se le pide ejecutar la opcion n°3 con agunas redes de p_intermedias = 2 y con casi cualquier p_intermedia > 2. Entendiendo que el problema no esta en el flujo del menu es que en el apartado de cosas implementadas este figura como completado al 100%. 

PD: `auxiliares.py` tiene que estar en el mismo directorio de `main.py` para que el programa se ejecute de forma correcta.

## Referencias de código externo :book:

Tarea realizada sin codigo externo!