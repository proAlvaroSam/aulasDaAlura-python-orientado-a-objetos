from modelos.restaurante import Restaurante

restaurante01 = Restaurante('dona maria', 'Caseiro')
restaurante02 = Restaurante('shiman', 'Japonesa')
restaurante03 = Restaurante('coringa', 'Hambúrguer')

restaurante02.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
