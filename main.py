# Estas são as importações de bibliotecas necessárias para o funcionamento do código. A biblioteca itertools é usada para criar iteradores eficientes para loops, enquanto math fornece funções matemáticas básicas e constantes.
import itertools
import math

# Aqui definimos a classe Calculadora, que representa a calculadora em si. O método __init__ é um método especial que é executado automaticamente sempre que um objeto da classe é instanciado. Ele inicializa os atributos da calculadora.

class Calculadora():
    def __init__(self):

# Nestas linhas, inicializamos os atributos da calculadora. self.input_ armazena o valor atual inserido na calculadora, self.soma é uma instância da classe Celula, que será usada para realizar operações matemáticas, e self.caixa_texto é uma instância da classe Texto, que será usada para exibir o texto na calculadora.

        self.input_ = "0" 
        self.soma = Celula()
        self.caixa_texto = Texto(self.input_) 

# Aqui definimos uma função interna novo_botao que cria um novo botão. Ela recebe um texto para exibir no botão, a linha e a coluna onde o botão deve ser colocado e a função a ser executada quando o botão é pressionado.
 
        def novo_botao(text, row, column, function):
            return Botao(text, row, column, function)

# Essa função interna input_numero retorna uma função lambda que chama o método Numero da calculadora com o número passado como argumento.

        def input_numero(numero):
            return lambda : self.Numero(numero)


        buttons = {}
        
# Nestas linhas, criamos um dicionário chamado buttons que mapeia os números de 1 a 9 para suas respectivas posições na interface da calculadora. Usamos a função itertools.product para criar todas as combinações possíveis de linhas e colunas onde os botões podem ser colocados.

        numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
        for numero in range(1, 10):
            buttons.update({str(numero) : (*numbers_positions[numero-1], input_numero(numero))})

# Esta linha adiciona o botão "0" à posição (5, 5) na interface da calculadora.

        buttons.update({"0": (5, 5, input_numero(0))})

# Estas linhas adicionam os botões de funções especiais (como pi, seno, cosseno, etc.) à interface da calculadora.

        buttons.update({
            "pi()": (2, 1, self.Pi),
            "x²": (2, 2, self.Pow),
            "log10()": (2, 3, self.Log10),
            "%": (2, 4, self.Percentual),
            "raiz()": (2, 5, self.Raiz_Quadrada),
            "clear": (2, 6, self.clear_),
            "sen()": (3, 1, self.Seno),
            "cos()": (4, 1, self.Cosseno),
            "tg()": (5, 1, self.Tangente)
        })

# Este loop cria todos os botões definidos no dicionário buttons e os coloca na interface da calculadora.

        for button in buttons.keys():
            novo_botao(button, *buttons[button])

# Este método limpa o valor atual na calculadora e atualiza o texto exibido.

    def clear_(self):
        self.input_ = "0"
        self.caixa_texto.atualizar(self.input_)        

# Este método calcula a raiz quadrada do número atual na calculadora e atualiza o texto exibido.

    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.input_))
        self.input_ = str(temporario)
        self.caixa_texto.atualizar(self.input_)

# Este método calcula o seno do número atual na calculadora e atualiza o texto exibido.

    def Seno(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.sin(temporario)
        self.caixa_texto.atualizar(self.input_)

# Este método prepara a calculadora para uma operação de soma.

    def Soma(self):
        self.soma._numero_A = self.input_
        self.soma._sinal = "soma"
        self.input_ = "0"

# Este método adiciona o número pressionado à calculadora e atualiza o texto exibido.

    def Numero(self, numero):
        self.input_ += str(numero)
        self.caixa_texto.atualizar(self.input_)

# Aqui definimos a classe Botao, que representa um botão na interface da calculadora. Ele armazena o texto a ser exibido no botão e a função a ser executada quando o botão é pressionado.

class Botao():
    def __init__(self, text_botao, linha, coluna, comando):
        print(f"Botão {text_botao} na linha {linha}, coluna {coluna}")
        self.texto = text_botao
        self.comando = comando

# Aqui definimos a classe Celula, que representa uma célula de cálculo na calculadora. Ela possui métodos para realizar operações matemáticas básicas.

class Celula():
    def __init__(self):
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        return float(self._numero_A) * float(self._numero_B)
    
    def divisao(self):
        return float(self._numero_A) / float(self._numero_B)

# Aqui definimos a classe Texto, que representa o texto exibido na calculadora. Ela possui um método para atualizar o texto exibido com um novo texto.

class Texto():
    def __init__(self, texto):
        self.texto = texto

    def atualizar(self, novo_texto):
        self.texto = round(float(novo_texto), 5)

# Inicialização
m = Calculadora()

# Impressão inicial
print("====================================")
print("|      CALCULADORA CIENTÍFICA      |")
print("|==================================|")
print("|   [ON]   |   [OFF]   |   [Mais]  |")
print("|==================================|")
print("|  [7]  |  [8]  |  | [9]   |  [/]  |")
print("|  [4]  |  [5]  |  | [6]   |  [*]  |")
print("|  [1]  |  [2]  |  | [3]   |  [-]  |")
print("|  [0]  |  [.]  |  | [=]   |  [+]  |")
print("====================================")
# Finalmente, instanciamos um objeto da classe Calculadora para iniciar a calculadora e imprimimos a interface inicial da calculadora