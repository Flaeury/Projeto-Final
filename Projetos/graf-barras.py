import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 45, 56, 78, 90]

# Plotagem do gráfico de barras
plt.bar(categorias, valores, color='green')
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.grid(axis='y')
plt.show()
