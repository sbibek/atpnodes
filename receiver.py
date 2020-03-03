import socket
import sys

PORT = 3333

def log(message):
    print('[receiver] {}'.format(message))

class G_SERVER:
    def __init__(self, port=3333):
        self.port = port

        self.da_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.da_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.da_socket.bind(('0.0.0.0', self.port))


    def start(self):
        # starts the DA server
        log('listening on {}:{}'.format('0.0.0.0', self.port))
        self.da_socket.listen()

        while True:
            try:
                connection, address = self.da_socket.accept()
                log('{} connected '.format(address))
                self.__service_loop(connection)
            except KeyboardInterrupt:
                log('ctrl+c signalled, exiting')
                self.stop()
                break

    def __service_loop(self, client):
        while True:
            try:
                request = client.recv(1024)

                if not request:
                    raise 'request received was none, so cnc might have exited'

                log("received request of {} bytes".format(len(request)))

            except Exception as e:
                print(e)
                log('exception in service loop {}'.format(str(e)))
                # this means that client has exited
                client.close()
                break

    def stop(self):
        log("closing server")
        self.da_socket.close()


a = G_SERVER(port=PORT)
a.start()