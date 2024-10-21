from modelos.avaliacao import Avaliacao

class Restaurante:
    todos_restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.todos_restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} |  {"Status"}')
        for restaurante in cls.todos_restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '--'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media