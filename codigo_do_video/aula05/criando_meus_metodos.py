class Restaurante:
    todos_restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.todos_restaurantes.append(self)

    def __str__(self):
       return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.todos_restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} ')

restaurante01 = Restaurante('Dona Maria', 'Caseiro')
restaurante02 = Restaurante('Shiman', 'Japonesa')

Restaurante.listar_restaurantes()