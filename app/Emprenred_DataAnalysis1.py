from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import requests
import json
##Spark
# Crear la sesión de Spark
spark = SparkSession.builder.appName("EmprenRed_DataAnalysis").getOrCreate()
# Especifica la ruta al archivo JSON
def guardar_respuesta_como_json(url, nombre_archivo):
    # Realizar la solicitud GET
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos_json = respuesta.json()

        # Guardar los datos en un archivo JSON
        with open(nombre_archivo, 'w') as archivo_json:
            json.dump(datos_json, archivo_json, indent=4)
        
        print(f"Datos guardados exitosamente en '{nombre_archivo}'.")
    else:
        print(f"Error al realizar la solicitud. Código de estado: {respuesta.status_code}")

# Ejemplo de uso
url = 'http://emprenred.eastus.cloudapp.azure.com:3009/solicitud'  
json_data = 'respuesta.json'  

guardar_respuesta_como_json(url, json_data)

# Cargar el JSON en un DataFrame de pandas
df1 = pd.read_json(json_data)

# Especifica la ruta donde quieres guardar el archivo CSV
ruta_csv = 'dataset/resultado.csv'

# Guardar el DataFrame como un archivo CSV
df1.to_csv(ruta_csv, index=False)

df = spark.read.csv("dataset/resultado.csv", header=True, inferSchema=True)

# Mostrar el DataFrame
df.show()
# Ajusta la intensidad de los rojos
intensity_factor = 2  # Puedes ajustar este valor según tus preferencias
#Análisis
# Calcula los 5 campos de negocio más comunes y su número
campos_negocio_mas_comunes = df.groupBy("campoNegocio").count().orderBy(col("count").desc()).limit(5)
print("Los 5 campos de negocio más comunes son:")
campos_negocio_mas_comunes.show(truncate=False)
df_pandas1 = campos_negocio_mas_comunes.toPandas()

# Crea el gráfico de barras
plt.bar(df_pandas1["campoNegocio"], df_pandas1["count"],color=plt.cm.Reds(intensity_factor * df_pandas1["count"] / max(df_pandas1["count"])))

# Añade los valores exactos encima de cada barra
for i, valor in enumerate(df_pandas1["count"]):
    plt.text(i, valor, str(valor), ha='center', va='bottom')
plt.title('Top 5 Campos de Negocio Más Comunes')
plt.xlabel('Campo de Negocio')
plt.ylabel('Número de Ocurrencias')

# Muestra el gráfico
plt.savefig('gráficas/grafica1.png')
plt.close()

# Calcula los 5 cargos más comunes y su número
cargos_mas_comunes = df.groupBy("cargoExperto").count().orderBy(col("count").desc()).limit(5)
print("Los 5 cargos más comunes son:")
cargos_mas_comunes.show(truncate=False)
df_pandas2 = cargos_mas_comunes.toPandas()
# Crea el gráfico de barras
plt.bar(df_pandas2["cargoExperto"], df_pandas2["count"],color=plt.cm.Reds(intensity_factor * df_pandas2["count"] / max(df_pandas2["count"])))
# Añade los valores exactos encima de cada barra
for i, valor in enumerate(df_pandas2["count"]):
    plt.text(i, valor, str(valor), ha='center', va='bottom')
plt.title('Top 5 Cargos de Expertos Más Comunes')
plt.xlabel('Cargo del Experto')
plt.xticks(fontsize=9)  # Ajusta el tamaño de la fuente
plt.xticks(rotation=30, ha="center")  # Ajusta el ángulo de rotación
plt.ylabel('Número de Ocurrencias')

# Ajustar el diseño para evitar que se recorte el texto
plt.tight_layout()

# Muestra el gráfico
plt.savefig('gráficas/grafica2.png')
plt.close()

# Calcula los 5 nombres de las empresas que más se le solicitan vacantes
negocios_mas_comunes = df.groupBy("nombreNegocio").count().orderBy(col("count").desc()).limit(5)
print("Los 5 negocios a los que cuales se le solicitan más vacantes son:")
negocios_mas_comunes.show(truncate=False)
df_pandas3 = negocios_mas_comunes.toPandas() 
plt.bar(df_pandas3["nombreNegocio"], df_pandas3["count"],color=plt.cm.Reds(intensity_factor * df_pandas1["count"] / max(df_pandas1["count"])))
# Añade los valores exactos encima de cada barra
for i, valor in enumerate(df_pandas3["count"]):
    plt.text(i, valor, str(valor), ha='center', va='bottom')
plt.title('Top 5 Negocios que les solicitan más vacantes')
plt.xlabel('Nombre del Negocio')
plt.xticks(fontsize=9)  # Ajusta el tamaño de la fuente
plt.xticks(rotation=30, ha="center")  # Ajusta el ángulo de rotación
plt.ylabel('Número de Ocurrencias')

# Ajustar el diseño para evitar que se recorte el texto
plt.tight_layout()

# Muestra el gráfico
plt.savefig('gráficas/grafica3.png')
plt.close()


