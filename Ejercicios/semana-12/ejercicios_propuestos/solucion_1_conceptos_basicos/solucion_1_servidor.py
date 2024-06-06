import socket
import threading


class Bot:

    def __init__(self, port: int, host: str) -> None:
        print("Inicializando servidor...")

        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind_and_listen()
        self.accept_connections()
        
        self.nuevo_caso_chile = 138846
        self.nuevo_caso_mundo = 108918
        self.casos_chile = 7039918
        self.casos_mundo = 4696
        self.actualizar_info()

    def bind_and_listen(self) -> None:

        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}...")

    def accept_connections(self) -> None:

        thread = threading.Thread(target=self.accept_connections_thread)
        thread.start()

    def accept_connections_thread(self) -> None:

        print("Servidor aceptando conexiones...")

        while True:
            client_socket, _ = self.socket_server.accept()
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, ),
                daemon=True)
            listening_client_thread.start()
            

    @staticmethod
    def send(value: any, sock: socket.socket) -> None:

        stringified_value = str(value)
        msg_bytes = stringified_value.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        sock.send(msg_length + msg_bytes)
    
    def sendall(self, value: any) -> None:
        pass

    def listen_client_thread(self, client_socket: socket.socket) -> None:

        print("Servidor conectado a un nuevo cliente...")
        
        while True:
            response_bytes_length = client_socket.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            response = bytearray()

            while len(response) < response_length:
                print("alo?")
                read_length = min(4096, response_length - len(response))
                response.extend(client_socket.recv(read_length))

            received = response.decode()
            self.handle_command(received, client_socket)
            

    def handle_command(self, opcion: str, client_socket: socket.socket) -> None:
        if opcion == "0": 
            msg = self.info["0"]
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)
        elif opcion == "1": 
            msg = self.info["1"]
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)
        elif opcion == "2": 
            msg = self.info["2"]
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)
        elif opcion == "3": 
            msg = self.info["3"]
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)
        elif opcion == "4": 
            msg = self.info["4"] 
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)
        else: 
            msg = "No seleccionaste ninguna opcion. \
            Envia 0 para recibir el menu de opciones"
            msg = msg.encode("utf-8")
            largo_mensaje = len(msg)
            client_socket.sendall(largo_mensaje.to_bytes(4, byteorder="big"))
            client_socket.sendall(msg)

    def actualizar_info(self) -> None:
        self.info = {'0' : '\n Menú de opciones \n' \
                            '[1] Casos en Chile \n' \
                            '[2] Casos en el Mundo \n' \
                            '[3] Consejos contra el Coronavirus \n' \
                            '[4] Reportar un nuevo caso',
                     '1' : f' Total (new) cases  \n Chile \n {self.casos_chile} ' \
                           f'confirmed cases ({self.nuevo_caso_chile}) \n 2264 deaths (627)',
                     '2' : f' Total (new) cases  \n Global \n {self.casos_mundo} ' \
                           f'confirmed cases ({self.nuevo_caso_mundo}) \n 404396 deaths (3539)',
                     '3' : 'Consejos \n' \
                            ' - Wash your hands frequently \n' \
                            ' - Avoid touching your eyes, mouth and nose \n' \
                            ' - Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze \n' \
                            ' - Avoid crowded places \n' \
                            ' - Stay at home if you feel unwell - even with a slight fever and cough \n' \
                            ' - If you have a fever, cough and difficulty breathing, seek medical care early - but call by phone first',
                     '4' : 'Se reportó un nuevo caso en Chile '
                }
    def actualizar_casos(self) -> None:
        pass


if __name__ == "__main__":
    port = 8080
    host = 'localhost'

    server = Bot(port, host)