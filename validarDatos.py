import streamlit as st
import re

def validar_nombre(nombre):
    patron = r'^[A-Z][a-zA-Z]+$'
    return re.fullmatch(patron, nombre)

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(patron, email)

def validar_telefono(telefono):
    # Adapta el patrón según el formato de teléfono deseado (ej: +5491112345678)
    patron = r'^\+\d{10}$'
    return re.fullmatch(patron, telefono)

def validar_fecha(fecha):
    # Adapta el patrón según el formato de fecha deseado (ej: DD/MM/AAAA)
    patron = r'^\d{2}/\d{2}/\d{4}$'
    return re.fullmatch(patron, fecha)

# Interfaz de usuario
st.title("Formulario de Validación")
st.write("Pagina desarrollada por: Juan Pablo Zuluaga Mesa")

nombre = st.text_input("Ingrese su primer nombre:")
email = st.text_input("Ingrese su dirección de correo electrónico:")
telefono = st.text_input("Ingrese su número de teléfono:")
fecha = st.text_input("Ingrese una fecha (DD/MM/AAAA):")

if st.button("Validar"):
    if not validar_nombre(nombre):
        st.error("El nombre debe comenzar con mayúscula y solo contener letras.")
    if not validar_email(email):
        st.error("La dirección de correo electrónico no es válida.")
    if not validar_telefono(telefono):
        st.error("El número de teléfono no es válido.")
    if not validar_fecha(fecha):
        st.error("El formato de fecha no es válido.")
    else:
        st.success("¡Todos los datos son válidos!")
