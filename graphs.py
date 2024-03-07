import matplotlib.pyplot as plt
import numpy as np

def mostrarFuncaoCosseno(pontoX):
    valorAbsolutoX = abs(pontoX)
    xInicio = valorAbsolutoX + (-1 * 2 * np.pi)
    xFim = valorAbsolutoX + (2 * np.pi)

    if (pontoX < 0):
        xInicio, xFim = -1 * xFim, -1 * xInicio
    
    x = np.linspace(xInicio, xFim, 100)
    y = np.cos(x)
    plt.axvline(x=pontoX, color='r', linestyle='--')
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoSeno(pontoX):
    valorAbsolutoX = abs(pontoX)
    xInicio = valorAbsolutoX + (-1 * 2 * np.pi)
    xFim = valorAbsolutoX + (2 * np.pi)

    if (pontoX < 0):
        xInicio, xFim = -1 * xFim, -1 * xInicio
    
    x = np.linspace(xInicio, xFim, 100)
    y = np.sin(x)
    plt.axvline(x=pontoX, color='r', linestyle='--')
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoQuadratica(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a * (x ** 2) + b * x + c
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoLinear(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoExponencial(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * (b ** x)
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoLogaritmica(a, b):
    x = np.linspace(0.1, 10, 100)
    y = a * np.log(x) / np.log(b)
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoFatorial():
    x = np.arange(1, 11)
    y = np.cumprod(x)
    plt.plot(x, y)
    plt.show()

def mostrarFuncaoRadical(a, b):
    x = np.linspace(0, 10, 100)
    y = a * (x ** (1 / b))
    plt.plot(x, y)
    plt.show()
