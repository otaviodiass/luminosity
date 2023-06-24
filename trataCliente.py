class TrataCliente:

    def __init__(self, mensagem):
        self.mensagem = mensagem

    def tratament(self):
        dicionario = {}
        lista = self.mensagem.split(',')
        if lista[0] == 'PUBLICAR':
            temp = f'{lista[1].strip()}, {lista[2].strip()}'
            dicionario = {'condicao': False, 'resposta': temp}
        else:
            dicionario = {'condicao': True}
        return dicionario
