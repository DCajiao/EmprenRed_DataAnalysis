# EmprenRed_DataAnalysis
EmprenRed DataAnalysis es una aplicación de análisis de Datos. En este repositorio se encuentra su Frontend en html y css. Esta aplicaciónn ejecutará de forma local un script de pyspark que arrojará 3 gráficas en formato png en un directorio específico, en la página alojada en Apache, se mostrarán dichas imágenes en un presentación más amigable.

---
# v0:FrontBase
Contiene el desarrollo Fronted base para desplegar la aplicación en la máquina Ubuntu.
## ¿Cómo montarla en Ubuntu?
1. Ejecutar *git clone* en la ubicación */var/www/html/* dentro de la máquina virtual Ubuntu. 
2. Definir en el Script de PySpark que las gráficas de salida deben almacenarse en */var/www/html/gráficas* con los respectivos nombres (*grafica1.png*, *grafica2.png*, *grafica3.png*).
3. Una vez definidos los tipos de análisis a realizar, incluir en las páginas la interpretación de la gráfica que se está mostrando. (>En esta gráfica podemos ver que...<)
---
