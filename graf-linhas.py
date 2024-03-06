import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotagem do gráfico de linhas
plt.plot(x, y)
plt.title('Gráfico de Linhas')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()
