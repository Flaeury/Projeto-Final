from tkinter import *  # Importa todos os símbolos (funções, classes, etc.) do módulo tkinter

import itertools  # Importa o módulo itertools, que fornece funções para criar iteradores

import math  # Importa o módulo math, que fornece funções matemáticas

class Calculadora():  # Define a classe Calculadora
    def __init__(self, raiz):  # Define o método de inicialização da classe
        # Inicializa o valor de entrada da calculadora como "0"
        self.input_ = "0" 
        # Cria uma instância da classe Celula e a atribui ao atributo "soma" da classe Calculadora
        self.soma = Celula()
        # Cria uma instância da classe Texto, passando a raiz (janela principal) e o valor de entrada como parâmetros, e atribui a essa instância ao atributo "caixa_texto" da classe Calculadora
        self.caixa_texto = Texto(raiz, self.input_) 

        # Define uma função local chamada "novo_botao" para criar novos botões na interface gráfica
        def novo_botao(text, row, column, function):
            return Botao(raiz, text, row, column, function)

        # Define uma função local chamada "input_numero" que retorna uma função lambda que chama o método "Numero" com o número especificado como argumento
        def input_numero(numero):
            return lambda : self.Numero(numero)
        
        # Cria um dicionário vazio chamado "buttons" para armazenar os botões da calculadora
        buttons = {}

        # Cria uma lista de tuplas contendo todas as combinações de posições para os botões numéricos na interface gráfica
        numbers_positions = list(itertools.product([3, 4, 5], [2, 3, 4]))
        
        # Itera sobre os números de 1 a 9
        for numero in range(1, 10):
            # Adiciona uma entrada ao dicionário "buttons" para cada número, mapeando-o para a posição correspondente e a função associada
            buttons.update({str(numero) : (*numbers_positions[numero-1], input_numero(numero))})
        
        # Adiciona a posição e a função associada para o botão "0" ao dicionário "buttons"
        buttons.update({"0": (5, 5, input_numero(0))})

        # Adiciona as funções trigonométricas, matemáticas e de limpeza ao dicionário "buttons", mapeando-as para as posições específicas na interface gráfica
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
        
        # Itera sobre as entradas do dicionário "buttons"
        for button in buttons.keys():
            # Chama a função "novo_botao" para criar um novo botão na interface gráfica com base nos dados do dicionário "buttons"
            novo_botao(button, *buttons[button])

    # Define o método "clear_" para limpar o valor de entrada da calculadora
    def clear_(self):
        self.input_ = "0"
        self.caixa_texto.atualizar(self.input_)        

    # Define o método "Raiz_Quadrada" para calcular a raiz quadrada do valor de entrada
    def Raiz_Quadrada(self):
        temporario = math.sqrt(float(self.input_))
        self.input_ = str(temporario)
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Seno" para calcular o seno do valor de entrada (em radianos)
    def Seno(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.sin(temporario)
        self.caixa_texto.atualizar(self.input_)
        
    # Define o método "Cosseno" para calcular o cosseno do valor de entrada (em radianos)
    def Cosseno(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.cos(temporario)
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Tangente" para calcular a tangente do valor de entrada (em radianos)
    def Tangente(self):
        temporario = ((int(self.input_))*2*math.pi)/(360)
        self.input_ = math.tan(temporario)
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Log10" para calcular o logaritmo na base 10 do valor de entrada
    def Log10(self):
        temporario = math.log10(int(self.input_))
        self.input_ = temporario
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Pi" para atribuir o valor de pi ao valor de entrada
    def Pi(self):
        self.input_ = math.pi
        self.caixa_texto.atualizar(self.input_)
        
    # Define o método "Pow" para elevar o valor de entrada ao quadrado
    def Pow(self):
        self.input_ = math.pow(float(self.input_), 2)
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Percentual" para calcular o percentual do valor de entrada
    def Percentual(self):
        self.input_ = (float(self.input_)/100)
        self.caixa_texto.atualizar(self.input_)

    # Define o método "Igual" para calcular o resultado da operação e atualizar o valor de entrada
    def Igual(self):
        self.soma._numero_B = self.input_
        soma = self.soma
        operacao = {"soma": soma.soma,
                    "subtracao": soma.subtracao,
                    "multiplicacao": soma.multiplicacao,
                    "divisao": soma.divisao}
        v = operacao()
        self.caixa_texto.atualizar(v)
        self.input_ = v

    def Soma(self):
        # Define o número A da célula como o valor de entrada atual da calculadora
        self.soma._numero_A = self.input_
        # Define o sinal da operação como "soma"
        self.soma._sinal = "soma"
        # Reinicia o valor de entrada da calculadora para "0"
        self.input_ = "0"

    def Multiplicacao(self):
        # Define o número A da célula como o valor de entrada atual da calculadora
        self.soma._numero_A = self.input_
        # Define o sinal da operação como "multiplicacao"
        self.soma._sinal = "multiplicacao"
        # Reinicia o valor de entrada da calculadora para "0"

    def Divisao(self):
        # Define o número A da célula como o valor de entrada atual da calculadora
        self.soma._numero_A = self.input_
        # Define o sinal da operação como "divisao"
        self.soma._sinal = "divisao"
        # Reinicia o valor de entrada da calculadora para "0"

    def Subtracao(self):
        # Define o número A da célula como o valor de entrada atual da calculadora
        self.soma._numero_A = self.input_
        # Define o sinal da operação como "subtracao"
        self.soma._sinal = "subtracao"
        # Reinicia o valor de entrada da calculadora para "0"

    def Numero(self, numero):
        # Adiciona o número ao final do valor de entrada da calculadora
        self.input_ += str(numero)
        # Atualiza o texto na interface gráfica com o novo valor de entrada

class Botao():
    def __init__(self, frame, text_botao, linha, coluna, comando):
        # Cria um botão na interface gráfica com o texto especificado e o comando associado
        self.button = Button(frame, text = text_botao, fg="black", bg="grey", command = comando, font = ("Arial", "20", "bold"))
        # Define a largura do botão
        self.button["width"] = 5
        # Define a altura do botão
        self.button["height"] = 1
        # Posiciona o botão na grade da interface gráfica
        self.button.grid(row = linha, column = coluna)

class Celula():
    def __init__(self):
        # Inicializa os atributos do número A, número B e sinal como nulos
        self._numero_A = None
        self._numero_B = None
        self._sinal = None

    def soma(self):
        # Retorna a soma dos números A e B
        return float(self._numero_A) + float(self._numero_B)

    def subtracao(self):
        # Retorna a subtração dos números A e B
        return float(self._numero_A) - float(self._numero_B)

    def multiplicacao(self):
        # Retorna a multiplicação dos números A e B
        return float(self._numero_A) * float(self._numero_B)
    
    def divisao(self):
        # Retorna a divisão dos números A e B
        return float(self._numero_A) / float(self._numero_B)

class Texto():
    def __init__(self, raiz, texto):
        # Cria um rótulo na interface gráfica com o texto especificado
        self.texto = Label(raiz, text =round (float(texto), 5), font = ("Arial", "72", "bold"))
        # Define a altura do rótulo
        self.texto["height"] = 2 
        # Define a largura do rótulo
        self.texto["width"] = 2
        # Posiciona o rótulo na grade da interface gráfica
        self.texto.grid(row=1, column=1, columnspan=6,sticky=W+E+N+S)

    def atualizar(self, novo_texto):
        # Atualiza o texto do rótulo com o novo texto especificado
        self.texto.config(text=round(float(novo_texto), 5))

def init():
    # Inicializa a janela principal
    raiz = Tk()
    # Define o título da janela
    raiz.title("Calculadora")
    # Define as dimensões da janela
    raiz.geometry("570x452")
    # Cria uma instância da calculadora na janela principal
    m = Calculadora(raiz)
    # Inicia o loop principal de eventos da interface gráfica
    raiz.mainloop()

init()