# Este es el emisor del archivo.
import socket

host_receptor = 'localhost'   ## Si lo ejecutas en otro computador, aquí debes poner 
                                       ## debes poner su dirección IP
puerto_receptor = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # IPv4         , TCP

# Nos conectamos al receptor del archivo, que ya debería estar escuchando.
sock.connect((host_receptor, puerto_receptor))
print("Conexión establecida.")

# Leemos el archivo y lo enviamos.
with open('files/enviar.bin', 'rb') as binfile:
    datos = binfile.read()
    sock.sendall(datos)

print("¡Archivo enviado!")

'''
Lecutra y envio por parte del servidor
'''

# Imprimimos lo que nos responda la contraparte.
print("Respuesta:", sock.recv(4096).decode('utf-8'))

# Cerramos el socket.
sock.close()


'''
Comentarios: 
    1. hostreceptor = localhost para que el programa no se caiga
    2. Recordar que la cantidad maxima de puertos es igual a 2^16, 12345 < 2^16
    3. sock es una variable de tipo socket, Objeto del modulo socket.
    4. Se DEBE iniciar el socket con los mismos protocolos y sistemas de direcciones que 
    el servidor, de lo contrario no seran capaces de comunicarse. 

Dudas: 
    1. Si despúes de enviar el archivo el servidor no responde nada, ¿que ocurre con 
    la linea 27?, ¿Pasa directamente a la linea 30 y cierra el socket? 
        -> Respueta: Se genera un error del tipo, ConnectionResetError, WinError 10054,
        corresponde al cierre del socket por parte del receptor. 
'''