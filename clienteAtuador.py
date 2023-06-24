import socket
import time


def assinar():
    while True:
        try:
            time.sleep(10)
            mensagem = 'ASSINAR, LUMINOSIDADE'
            client.send(mensagem.encode())

            mensagem = client.recv(2048)
            mensagem_decodificada = mensagem.decode()

            if int(mensagem_decodificada.split(',')[1].strip()) >= 60:
                print('ABRINDO CORTINA')
            else:
                print('FECHANDO CORTINA')
        except:
            print('Erro ao abrir e fechar cortina.')
        

if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    assinar()
