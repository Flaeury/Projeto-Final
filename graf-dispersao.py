import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plotagem do gráfico de dispersão
plt.scatter(x, y, color='red')
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()
