import socket
import time
from random import randint


def publicar():
    while True:
        try:
            time.sleep(5)
            luminosidade = randint(0, 100)
            client.send(f'PUBLICAR, LUMINOSIDADE, {str(luminosidade)}'.encode())
        except:
            print('Erro ao publicar mensagem.')


if __name__ == '__main__': 
    HOST = 'localhost'
    PORTA = 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    publicar()
