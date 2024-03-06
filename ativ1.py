import matplotlib.pyplot as plt


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


def plot_or_solve():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    choice = input(
        "Deseja plotar o gráfico (P) ou encontrar as raízes da função (R)? ")

    if choice == 'P' or choice == 'p':
        x_values = np.linspace(-30, 30, 10)
        y_values = funcao_quadratica(x_values, a, b, c)

        plt.plot(x_values, y_values, label=f'{a}x² + {b}x + {c}')
        plt.title('Gráfico de uma Função Quadrática')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.show()
    elif choice in ('R', 'r'):
        raizes = calcular_raizes(a, b, c)
        print(f"Raízes da função quadrática: {raizes}")
    else:
        print("Opção inválida. Escolha 'P' para plotar o gráfico ou 'R' para resolver a função quadrática.")


plot_or_solve()
