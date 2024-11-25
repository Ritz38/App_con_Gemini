import streamlit as st
import pandas as pd
import requests
import re
from openpyxl import Workbook

def procesar_csv(url):
    # Descargar el CSV
    response = requests.get(url)
    open('regex_productos.csv', 'wb').write(response.content)

    # Leer el CSV
    df = pd.read_csv('regex_productos.csv')

    # Definir expresiones regulares (ajustar según el formato del CSV)
    regex_numero_serie = r'\d+'
    regex_nombre_producto = r'[A-Za-z\s]+'
    regex_valor = r'\$\d+\.\d+'
    regex_fecha = r'\d{2}/\d{2}/\d{2}'
    regex_contacto = r'[^,\n]+'  # Ajustar según el formato de la columna de contacto

    # Crear un nuevo DataFrame para almacenar los datos formateados
    data = {'Número de serie': [],
            'Nombre del producto': [],
            'Valor': [],
            'Fecha de compra': [],
            'Información de contacto': []}

    # Iterar sobre cada fila y extraer la información
    for index, row in df.iterrows():
        data['Número de serie'].append(re.search(regex_numero_serie, str(row['columna_numero_serie'])).group())
        # ... (similarmente para otras columnas)
        data['Información de contacto'].append(re.findall(regex_contacto, str(row['columna_contacto'])))

    # Crear un DataFrame a partir del diccionario
    df_nuevo = pd.DataFrame(data)

    # Crear un archivo Excel
    workbook = Workbook()
    sheet = workbook.active
    for row in df_nuevo.itertuples(index=False):
        sheet.append(row)

    # Guardar el archivo Excel
    workbook.save('resultado.xlsx')

# Interfaz de usuario de Streamlit
st.title("Procesador de CSV con Regex")

url = "https://raw.githubusercontent.com/gabrielawad/programacion-para-ingenieria/refs/heads/main/archivos-datos/regex/regex_productos.csv"
if st.button("Procesar CSV"):
    procesar_csv(url)
    st.success("¡Archivo Excel generado exitosamente!")
