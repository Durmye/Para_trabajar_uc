import pickle
import socket

server_host = 'localhost'  # Debemos poner aquí la dirección IP del servidor.
                  # Si no ponemos nada, supone que estamos hablando con un programa en el mismo host.
port = 12345


class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

# Enviaremos esta instancia de la clase Persona.
persona = Persona("Juan Pérez", "jp@ejemplo.com")
mensaje = pickle.dumps(persona)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_host, port))
sock.sendall(mensaje)

data = pickle.loads(sock.recv(4096))
print(f"He recibido bytes de vuelta y los deserialicé a {type(data)}")
print(data.nombre)
sock.close()


'''
Comentarios: 

    1. Windows(11) no acepta el parametro "server_host" como un string vacio, "", 
    levanta un error "OSError", [WinError10049]
        - Para solucionar esto se debe incluir la ip del servidor al que se desea acceder.
        En este caso se dejo como "localhost"
'''