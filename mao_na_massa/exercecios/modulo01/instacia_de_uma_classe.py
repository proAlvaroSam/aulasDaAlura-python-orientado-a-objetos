class Restaurante:
    todos_restaurantes = []
    def __init__(self, nome, categoria, local):
        self.nome =  nome
        self.categoria = categoria
        self.local = local
        self._ativo = False
        Restaurante.todos_restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.local}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Local'.ljust(20)} | {'Status'}')
        for restaurante in cls.todos_restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.local.ljust(20)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativo'
    
    def alternando_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Comida de Rua', 'Brasil')
restaurante_pizza = Restaurante('Pizza', 'Fast Food', 'Estados Unidos')

restaurante_pizza.alternando_estado()

Restaurante.listar_restaurantes()