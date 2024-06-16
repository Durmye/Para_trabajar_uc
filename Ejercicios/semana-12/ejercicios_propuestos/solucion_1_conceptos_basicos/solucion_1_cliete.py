import socket
import threading


class Usuario:

    def __init__(self, port: int, host: str) -> None:

        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.connect_to_server()
            self.listen()
            self.repl()
        except ConnectionError:
            print("Conexión terminada.")
            self.socket_client.close()
            exit()

    def connect_to_server(self) -> None:

        self.socket_client.connect((self.host, self.port))

    def listen(self) -> None:


        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def send(self, msg: str) -> None:

        msg_bytes = msg.encode()
        msg_length = len(msg_bytes).to_bytes(4, byteorder='big')
        self.socket_client.sendall(msg_length + msg_bytes)

    def listen_thread(self) -> None:
        while True:
            response_bytes_length = self.socket_client.recv(4)
            response_length = int.from_bytes(
                response_bytes_length, byteorder='big')
            response = bytearray()

            while len(response) < response_length:
                read_length = min(4096, response_length - len(response))
                response.extend(self.socket_client.recv(read_length))

            print(f"{response.decode()}\n>>> ", end='')

    def repl(self) -> None:


        print("------ Whatsapp WHO ------\n Apreta 0 para recibir el menú de opciones\n>>> ", end='')
        while True:
            msg = input()
            response = self.send(msg)



if __name__ == "__main__":
    port = 8080
    host = 'localhost'

    client = Usuario(port, host)