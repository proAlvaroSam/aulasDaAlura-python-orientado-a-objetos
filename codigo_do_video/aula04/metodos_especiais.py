class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
       return f'{self.nome} | {self.categoria}'

restaurante01 = Restaurante('Dona Maria', 'Caseiro')
restaurante02 = Restaurante('Shiman', 'Japonesa')
 
restaurantes = [restaurante01, restaurante02]

print(restaurante01)
print(restaurante02)