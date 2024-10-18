class Restaurante:
    todos_restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.todos_restaurantes.append(self)

    def __str__(self):
       return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurant'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.todos_restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'

restaurante01 = Restaurante('Dona Maria', 'Caseiro')
restaurante02 = Restaurante('Shiman', 'Japonesa')

Restaurante.listar_restaurantes()