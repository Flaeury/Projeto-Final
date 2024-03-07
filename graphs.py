import matplotlib.pyplot as plt
import numpy as np

def plotCosFunc(xPoint):
    xPointAbs = abs(xPoint)
    xStart = xPointAbs + (-1 * 2 * np.pi)
    xEnd = xPointAbs + (2 * np.pi)

    if (xPoint < 0):
        xStart, xEnd = -1 * xEnd, -1 * xStart

    x = np.linspace(xStart, xEnd, 100)
    y = np.cos(x)
    plt.axvline(x=xPoint, color='r', linestyle='--')
    plt.plot(x, y)
    plt.show()

def plotSinFunc(xPoint):
    xPointAbs = abs(xPoint)
    xStart = xPointAbs + (-1 * 2 * np.pi)
    xEnd = xPointAbs + (2 * np.pi)

    if (xPoint < 0):
        xStart, xEnd = -1 * xEnd, -1 * xStart

    x = np.linspace(xStart, xEnd, 100)
    y = np.sin(x)
    plt.axvline(x=xPoint, color='r', linestyle='--')
    plt.plot(x, y)
    plt.show()

def plotQuadraticFunc(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a * (x ** 2) + b * x + c
    plt.plot(x, y)
    plt.show()

def plotLinearFunc(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b
    plt.plot(x, y)
    plt.show()

def plotExponentialFunc(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * (b ** x)
    plt.plot(x, y)
    plt.show()

def plotLogarithmicFunc(a, b):
    x = np.linspace(0.1, 10, 100)
    y = a * np.log(x) / np.log(b)
    plt.plot(x, y)
    plt.show()

def plotFactorialFunc():
    x = np.arange(1, 11)
    y = np.cumprod(x)
    plt.plot(x, y)
    plt.show()

def plotRadicalFunc(a, b):
    x = np.linspace(0, 10, 100)
    y = a * (x ** (1 / b))
    plt.plot(x, y)
    plt.show()
