class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante01 = Restaurante()
restaurante01.nome = 'Dona Maria'
restaurante01.categoria = 'Caseiro'

restaurante02 = Restaurante()

restaurantes = [restaurante01, restaurante02]

print(vars(restaurante01))