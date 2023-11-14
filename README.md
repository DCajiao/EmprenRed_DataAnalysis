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
---
# v1:FrontBase + ScriptPySpark + Matplotlib_borrador
Se añadieron los siguientes items:
1. Contiene la primera versión del Script de PySpark
2. Contiene los datos almacenados en un JSON en la carpeta dataset/resultado.JSON (Esto es provisional mientras se desarrolla el despliegue de la app principal en la nube de Azure)
3. Contiene instruccionnes en el Script EmprenRed_DataAnalysys.py de los aspectos que se deben implementar.
4. El front ya se encuentra sincronizado con el output del Script pruebasgraficas.py para mostrar las imagenes en la página
---