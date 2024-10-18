class Restaurante:
    todos_restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.todos_restaurantes.append(self)

    def __str__(self):
       return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurant'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.todos_restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'
    
    def alternar_estado (self):
        self._ativo = not self._ativo

restaurante01 = Restaurante('dona maria', 'Caseiro')
restaurante02 = Restaurante('shiman', 'Japonesa')
restaurante02.alternar_estado()

Restaurante.listar_restaurantes()