#Gráficas en png
import matplotlib.pyplot as plt

#Análisis 1
# Datos de ejemplo
x1 = [2, 4, 6, 8, 10]
y1 = [1, 2, 3, 5, 12]
# Crear un gráfico de línea
plt.plot(x1, y1)
plt.title('Gráfico de Línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
# Guardar el gráfico en un sitio específico
plt.savefig('gráficas/grafica1.png')
plt.close()  # Cerrar la figura actual

#Análisis 2
# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [0, 7, 1, 9, 5]
plt.bar(categorias, valores)
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')
# Guardar el gráfico en un sitio específico
plt.savefig('gráficas/grafica2.png')
plt.close()  # Cerrar la figura actual

#Análisis 3
# Datos de ejemplo
x = [3,2,1,2,3]
y = [5,4,6,7,8]
# Crear un gráfico de línea
plt.plot(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
# Guardar el gráfico en un sitio específico
plt.savefig('gráficas/grafica3.png')
plt.close()  # Cerrar la figura actual