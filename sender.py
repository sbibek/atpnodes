import socket
import sys
import time
import os


G_HOST = '127.0.0.1'
G_PORT = 3333 
G_DATA = os.urandom(1000)
G_TOTAL_SENDS = 100


def log(message):
    print('[sender] {}'.format(message))


class Sender:
    def __init__(self, da_host, da_port):
        self.da_host = da_host
        self.da_port = da_port

        self.da_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.da_socket.connect((self.da_host, self.da_port))

    def start(self):
        for i in range(G_TOTAL_SENDS):
            # send data
            self.da_socket.send(G_DATA)
            time.sleep(0.01) 

    def stop(self):
        self.da_socket.close()


a = Sender(G_HOST, G_PORT)
a.start()
a.stop()