import matplotlib.pyplot as plt
import numpy as np
from mostrarCalculadora import mostrarCalculadora

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
    """
print(calculator)


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"


def plot_quadratica():
    x = np.linspace(-10, 10, 100)
    y = x ** 2
    plt.plot(x, y)
    plt.title('Gráfico da função quadrática: y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def plot_linear():
    x = np.linspace(-10, 10, 100)
    y = 2 * x + 3
    plt.plot(x, y)
    plt.title('Gráfico da função linear: y = 2x + 3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def exponencial(a, x):
    return a ** x


def plot_exponencial(valor1, valor2):
    x = np.linspace(-6, 6, 100)
    y = np.exp(x)
    plt.plot(x, y)
    plt.title(f'Gráfico da função exponencial: {valor1}**{valor2}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def plot_logaritmica():
    x = np.linspace(0.1, 5, 100)
    y = np.log(x)
    plt.plot(x, y)
    plt.title('Gráfico da função logarítmica: y = log(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Função para plotar o gráfico de uma função raiz quadrada


def plot_raiz_quadrada():
    x = np.linspace(0, 5, 100)
    y = np.sqrt(x)
    plt.plot(x, y)
    plt.title('Gráfico da função raiz quadrada: y = sqrt(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def print_calculator():

    mostrarCalculadora("""Inicie uma operação       
                                
    1: Básicas
    2: Funções 
    3: Sair""")


def print_basica():
    mostrarCalculadora("""Escolha sua  Opção     
                       
  1: Soma       
  2: Subtração  
  3: Multip.   
  4: Divisão    
  5: Voltar""")


def print_funcoes():
    mostrarCalculadora("""Escolha sua Função    
                                 
      1: Exponencial       
      2: Logarítmica  
      3: Quadrática    
      4: Linear    
      5: Fatorial
      6. Raiz
      7. Voltar""")


def init():
    print_calculator()

    escolha = int(input("\nEscolha uma opção para iniciar: "))

    while escolha != 3:
        if escolha == 1:
            print_basica()

            categoria = int(input("\nEscolha uma categoria: "))
            while categoria != 5:

                if categoria == 1:
                    print("\nVocê escolheu SOMA")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("Digite o segundo valor: "))
                    print(f"\nO resultado é {soma(valor1,valor2)}")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("Digite o segundo valor: "))
                    print(f"\nO resultado é {subtracao(valor1, valor2)}")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("Digite o segundo valor: "))
                    print(f"\nO resultado é {multiplicacao(valor1, valor2)}")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("Digite o segundo valor: "))
                    print(f"\nO resultado é {divisao(valor1, valor2)}")
                    break
                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 7:

                if funcao == 1:
                    print("\nVocê escolheu a função Exponencial (a**x)")
                    valor1 = int(input("\nDigite o valor de a: "))
                    valor2 = int(input("Digite o valor de x: "))
                    print(
                        f"O resultado da exponencial foi: {exponencial(valor1, valor2)}")

                    plot_exponencial(valor1, valor2)
                    break

                elif funcao == 2:

                    plot_logaritmica()
                    break

                elif funcao == 3:
                    plot_quadratica()
                    break

                elif funcao == 4:
                    plot_linear()
                    break

                elif funcao == 5:
                    print("Ok")

                elif funcao == 6:
                    plot_raiz_quadrada()
                    break

                elif categoria == 7:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()
