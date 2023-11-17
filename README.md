# EmprenRed_DataAnalysis

EmprenRed DataAnalysis es una aplicación de análisis de datos. Este repositorio contiene el frontend en HTML y CSS. La aplicación ejecutará localmente un script de PySpark que generará 3 gráficos en formato PNG en un directorio específico. En la página alojada en Apache, se mostrarán estas imágenes de manera más amigable.

### ¿Cómo implementar en Ubuntu?
1. Ejecuta git clone en la ubicación /var/www/html/ dentro de la máquina virtual Ubuntu.
2. Especifica en el script de PySpark que los gráficos de salida deben almacenarse en /var/www/html/gráficas con los nombres respectivos.
3. Antes de ejecutar, se debe ejecutar:
    '''pip install apache2 python3'''