from modelos.restaurante import Restaurante

restaurante01 = Restaurante('Praça', 'Comida de Rua')
restaurante02 = Restaurante('Viagra', 'Gourmet')
restaurante03 = Restaurante('coringa', 'Hambúrguer')
restaurante04 = Restaurante('Sushi do Japa', 'Japonesa')

restaurante03.receber_avaliacao('Paulo', 9)
restaurante03.receber_avaliacao('Ana', 8)
restaurante03.receber_avaliacao('João', 7)
restaurante03.receber_avaliacao('Mathia', 5)
restaurante03.receber_avaliacao('Carlos', 9)

restaurante03.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
