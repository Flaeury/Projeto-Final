import numpy as np
import matplotlib.pyplot as plt

# Dados
np.random.seed(0)
data = np.random.randn(1000)

# Plotagem do histograma
plt.hist(data, bins=30, color='skyblue')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()
