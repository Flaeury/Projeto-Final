
# TODO: Operações básicas: Soma, Subtração, Divisão e Multiplicação.
# TODO: Operações com funções: Exponencial, logarítmica, quadrática, lineares e fatoriais e raiz.
# TODO: Operações Trigonométricas: Seno, Cosseno, Tangente.
# ? Fazer plot de gráfico em Op. de funções.

def print_calculator():
    calculator = """
     _________________
    |  _____________  |
    | |_____________| |
    | |             | |
    | | x² √  CE  C | |
    | | 7  8  9   / | |
    | | 4  5  6   * | |
    | | 1  2  3   - | |
    | | 0  .  =   + | |
    | |_____________| |
    |_________________|
    
     ________________
    |                |
    |   Inicie uma   |
    |    Operação    |
    |                |
    |  1: Básicas    |
    |  2: Funções    |
    |  3: Trigonom.  |
    |  4: Sair       |
    |                |
    |________________|
    """
    print(calculator)


def init():
    print_calculator()

    escolha = int(input("Escolha uma categoria: "))

    while escolha != 4:
        if escolha == 1:
            calculador = """
           ________________
          |                |
          |   Inicie uma   |
          |    Operação    |
          |                |
          |  1: Soma       |
          |  2: Subtração  |
          |  3: Multip.    |
          |  4: Divisão    |
          |  5: Sair       |
          |                |
          |________________|
          """
            print(calculador)


init()
