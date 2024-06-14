import numpy as np
import matplotlib.pyplot as plt

# Definimos la función x^2 + 3x - 4 para x = [0, 10]
def f(x):
    return x**2 + 3*x - 4

# Generamos un rango de valores para x y    evaluamos la función en ese rango
x = np.linspace(0, 10, 400)
y = f(x)

# Creamos el gráfico
plt.plot(x, y, label='f(x) = x^2 + 3x - 4')

# Agregamos título y etiquetas de eje
plt.title('Gráfico de la función f(x) = x^2 + 3x - 4')
plt.xlabel('x')
plt.ylabel('y')

# Mostramos el gráfico y guardamos en un archivo PNG
plt.savefig('funcion_x2_3x_4.png', bbox_inches='tight')
plt.show()
