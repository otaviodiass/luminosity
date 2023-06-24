import socket
import threading
from trataCliente import TrataCliente

clientes = []
temp = ''

print("Aguardando conexão de um cliente")


def novo_cliente():
    while True:
        try:
            cliente, porta = server.accept()
            clientes.append(cliente)
            print("Conectado em :", porta)
            threading.Thread(target=troca_mensagem, args=(cliente, porta)).start()
        except:
            print('Erro na conexão com o cliente.')


def troca_mensagem(cliente, porta):
    while True:
        try:
            mensagem = cliente.recv(2048)
            mensagem_decodificada = mensagem.decode()
            trata = TrataCliente(mensagem_decodificada)
            data = trata.tratament()

            global temp

            if data['condicao']:
                envia_mensagem(temp)
            else:
                temp = data['resposta']
                data = {}
        except:
            print('Erro com a mensagem do cliente.')


def envia_mensagem(mensagem):
    clientes[1].send(mensagem.encode())


if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))
    server.listen(5)
    threading.Thread(target=novo_cliente(), args=()).start()
