def print_menu():
    print("\n")
    print("|==========================================|")
    print("|          CALCULADORA CIENTÍFICA          |")
    print("|==========================================|")
    print("|    [ON]    |    [OFF]    |     [Mais]    |")
    print("|==========================================|")
    print("|  [1] Soma           |     [2] Subtração  |")
    print("|  [3] Multiplicação  |     [4] Divisão    |")
    print("|  [5] Fatorial       |     [6] Sair       |")
    print("|==========================================|")
    print("\n")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y


def calculate_factorial(num):
    if num < 0:
        return "Erro: Fatorial de número negativo não está definido!"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial


def main():
    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == '6':
            print("Saindo da calculadora.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print("Resultado:", add(num1, num2))
            elif choice == '2':
                print("Resultado:", subtract(num1, num2))
            elif choice == '3':
                print("Resultado:", multiply(num1, num2))
            elif choice == '4':
                print("Resultado:", divide(num1, num2))
        elif choice == '5':
            num = int(input("Digite um número para calcular o fatorial: "))
            print("Resultado:", calculate_factorial(num))
        else:
            print("Opção inválida!")


main()
