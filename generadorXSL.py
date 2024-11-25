import streamlit as st
import pandas as pd
import re
import os

# Función para extraer la información mediante expresiones regulares
def extract_data(text):
    # Regex para Número de serie del producto
    serial_number = re.search(r"\b\d{4,6}\b", text)  # ejemplo de un número de serie con 4 a 6 dígitos
    serial_number = serial_number.group(0) if serial_number else "Desconocido"

    # Regex para Nombre del producto (simple ejemplo)
    product_name = re.search(r"([A-Za-z0-9\s]+(?:\s[A-Za-z0-9\s]+)*)", text)
    product_name = product_name.group(0).strip() if product_name else "Desconocido"

    # Regex para Valor (Ejemplo de precios en formato $123.45)
    price = re.search(r"\$\d+(?:,\d{1,2})?", text)
    price = price.group(0) if price else "Desconocido"

    # Regex para Fecha de compra (Ejemplo: DD/MM/YY)
    purchase_date = re.search(r"\b(\d{2}/\d{2}/\d{2})\b", text)
    purchase_date = purchase_date.group(0) if purchase_date else "Desconocida"

    # Regex para extraer Información de contacto de clientes (Nombres, emails, teléfono)
    name_email_phone = re.findall(r"([A-Za-z]+(?:\s[A-Za-z]+)*)\s*([\w\.-]+@[\w\.-]+)\s*(\+?\d{1,4}?\s?\(?\d{1,3}\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4})", text)
    contact_info = []
    for match in name_email_phone:
        contact_info.append(f"{match[0]}, {match[1]}, {match[2]}")

    return serial_number, product_name, price, purchase_date, contact_info


# Función principal para cargar archivo y procesar los datos
def process_file(file):
    # Leer el archivo CSV
    df = pd.read_csv(file)
    
    # Lista para almacenar los datos procesados
    data = []

    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        text = row[0]  # Asumimos que el texto está en la primera columna
        serial_number, product_name, price, purchase_date, contact_info = extract_data(text)

        # Añadir los resultados a la lista
        for contact in contact_info:
            contact_details = contact.split(", ")
            data.append([serial_number, product_name, price, purchase_date] + contact_details)

    # Convertir la lista de datos en un DataFrame
    processed_df = pd.DataFrame(data, columns=["Número de serie del producto", "Nombre del producto", "Valor", "Fecha de compra", "Nombre del cliente", "Correo electrónico", "Teléfono"])

    # Guardar el DataFrame en un archivo Excel
    output_file = "productos_procesados.xlsx"
    processed_df.to_excel(output_file, index=False)

    return output_file


# Interfaz de usuario con Streamlit
def main():
    st.title("Procesador de Productos con Regex")
    
    st.write("""
    Esta aplicación procesa un archivo CSV de productos utilizando expresiones regulares.
    Extrae información relevante y genera un archivo Excel con los datos procesados.
    """)

    # Subir archivo CSV
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Procesar el archivo y obtener el archivo Excel
        output_file = process_file(uploaded_file)
        
        # Mostrar mensaje de éxito
        st.success(f"Archivo procesado con éxito. Puedes descargarlo aquí:")
        
        # Enlace de descarga para el archivo generado
        st.download_button(
            label="Descargar archivo Excel",
            data=open(output_file, "rb").read(),
            file_name=output_file,
            mime="application/vnd.ms-excel"
        )

if __name__ == "__main__":
    main()
