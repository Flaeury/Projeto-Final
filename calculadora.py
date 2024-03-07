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


def linear(x, a, b):
    return a*x + b


def plot_linear(a, b):
    axisX = np.linspace(-10, 10, 100)
    axisY = linear(axisX, a, b)
    plt.plot(axisX, axisY)
    plt.title(f'Gráfico da função linear {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def exponencial(a, x):
    return a ** x


def plot_exponencial(valor1, valor2):
    x = np.linspace(-6, 6, 100)
    y = exponencial(valor1, x)
    plt.plot(x, y)
    plt.title(f'Gráfico da função exponencial: {valor1}^{valor2}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def funcao_quadratica(x, a, b, c):
    return a * x ** 2 + b * x + c


def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        raiz_delta = delta ** 0.5
        raiz1 = (-b + raiz_delta) / (2*a)
        raiz2 = (-b - raiz_delta) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "Complicado isso ai"


def plot_quadratica(a, b, c):
    x_values = np.linspace(-10, 10, 50)
    y_values = funcao_quadratica(x_values, a, b, c)
    plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}')
    plt.title('Gráfico de uma Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()


def fatorial(n):

    if n < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def plot_fatorial(n):
    x = list(range(n + 1))
    y = [fatorial(i) for i in x]
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title('Gráfico do Fatorial')
    plt.xlabel('Número')
    plt.ylabel('Fatorial')
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
      2: Quadrática    
      3: Linear    
      4: Fatorial
      5. Voltar""")


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
                    valor2 = int(input("\nDigite o segundo valor: "))
                    print(f"\nO resultado é {soma(valor1,valor2)}")
                    break

                elif categoria == 2:
                    print("\nVocê escolheu SUBTRAÇÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("\nDigite o segundo valor: "))
                    print(f"\nO resultado é {subtracao(valor1, valor2)}")
                    break

                elif categoria == 3:
                    print("\nVocê escolheu MULTIPLICAÇÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("\nDigite o segundo valor: "))
                    print(f"\nO resultado é {multiplicacao(valor1, valor2)}")
                    break

                elif categoria == 4:
                    print("\nVocê escolheu DIVISÃO")
                    valor1 = int(input("\nDigite o primeiro valor: "))
                    valor2 = int(input("\nDigite o segundo valor: "))
                    print(f"\nO resultado é {divisao(valor1, valor2)}")
                    break

                elif categoria == 5:
                    print_basica()

        elif escolha == 2:
            print_funcoes()

            funcao = int(input("\nEscolha uma função: "))

            while funcao != 5:

                if funcao == 1:
                    print("\nVocê escolheu a função EXPONENCIAL (a ** x)")
                    valor1 = int(input("\nDigite o valor de a: "))
                    valor2 = int(input("\nDigite o valor de x: "))
                    print(
                        f"O resultado da exponencial é: {exponencial(valor1, valor2)}")

                    plot_exponencial(valor1, valor2)
                    break

                elif funcao == 2:
                    print(
                        "\nVocê escolheu a função QUADRÁTICA (a * x ** 2 + b * x + c)")
                    valor1 = int(input("\nDigite o valor de a: "))
                    valor2 = int(input("\nDigite o valor de b: "))
                    valor3 = int(input("\nDigite o valor de c: "))
                    print(
                        f"O resultado das raízes ou da raíz é/são: {calcular_raizes(valor1,valor2,valor3)}")
                    plot_quadratica(valor1, valor2, valor3)
                    break

                elif funcao == 3:
                    print(
                        "\nVocê escolheu a função LINEAR f(x) = (a * x + b)")
                    valor1 = int(input("\nDigite o valor de a: "))
                    valor2 = int(input("\nDigite o valor de b: "))
                    valor3 = int(input("\nDigite o valor de x: "))
                    print(
                        f"O resultado dessa linear é: {linear(valor3, valor1,valor2)}")

                    plot_linear(valor1, valor2)
                    break

                elif funcao == 4:
                    n = int(input("Escolha o número do fatorial: "))
                    print(f"O resultado da fatorial {n}! é: {fatorial(n)}")
                    plot_fatorial(n)
                    break

                elif funcao == 5:
                    print_funcoes()

        elif escolha == 3:
            break
        print_calculator()

        escolha = int(input("\nEscolha uma opção para iniciar: "))


init()
