class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante01 = Restaurante('Dona Maria', 'Caseiro')
restaurante02 = Restaurante('Shiman', 'Japonesa')
 
restaurantes = [restaurante01, restaurante02]

print(vars(restaurante01))
print(vars(restaurante02))