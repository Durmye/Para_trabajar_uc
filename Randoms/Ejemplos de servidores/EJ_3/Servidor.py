# Este es el receptor del archivo.
import socket

host = 'localhost'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # IPv4         , TCP
sock.bind((host, port))
sock.listen()
print("Escuchando...")

# Aceptamos un cliente.
sock_cliente, (host_cliente, port_cliente) = sock.accept()
print("Conexión entrante aceptada.")

# Leemos la información y la guardamos en un archivo.
#datos = sock_cliente.recv(4096)
#with open('files/recibido.bin', 'wb') as binfile:
#    binfile.write(datos)

print("¡Archivo recibido!")
# Le enviamos una respuesta a la contraparte.
sock_cliente.sendall("Gracias.".encode('utf-8'))

input()
# Cerramos los sockets.
sock_cliente.close()
sock.close()


'''
Comentarios: 
    1. sock es un objeto del modulo socket, permite acceder al objeto fisico del computador
    que se conecta a la red. Correspondiente a la ip local y al puerto "12345" 
    2. En este caso inmediatamente despúes se "vincula" el sock al puerto y luego queda 
    escuchando informacion que podria ser enviada. 
    3. Mediante sock.accept() se permite el envio de información por parte de un cliente

    4. En este ejemplo el servidor lee unicamente 4096 bytes, esto es debido a que no 
    se sabe que tan grande es el mensaje a recibir. 
    
Dudas: 
    1. Si se comentan las lineas 18-20, ¿ocurre algun error?, ¿O sencillamente se pierde la
    información? 
        -> Respuesta: No se recibe ningun arhcivo y el programa se cierra de manera 
        satisfactoria. Sin embargo en el terminal del cliente aparece un error de conexión,
        especificamente, ConnectionAbortedError, significa esto que: ¿el programa
        del servidor actuo "mas rapido" que el programa del cliente? 

            - Si la respuesta es si, ¿esto es producto de haber comentado las lineas 
            18-20?
            - Si la respuesta es no, ¿esto por que ocurre? 
    2. Siguiendo la situación de la pregunta n°1, como evitar que esto ocurra si es que
    el servidor no esta leyendo la información de un archivo, o haciendo cualquier tarea
    que "asegure" que efectivamente se cerrara despúes del cliente. 
'''