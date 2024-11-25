import streamlit as st
import re

def evaluar_contrasena(contrasena):
    # Expresiones regulares para cada criterio
    mayuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[¡¿$@#$%^&?%!]')

    # Inicializar variables de conteo
    conteo_mayusculas = len(mayuscula.findall(contrasena))
    conteo_minusculas = len(minuscula.findall(contrasena))
    conteo_numeros = len(numero.findall(contrasena))
    conteo_especiales = len(especial.findall(contrasena))

    # Evaluar la fortaleza
    if len(contrasena) >= 8 and conteo_mayusculas > 0 and conteo_minusculas > 0 and conteo_numeros > 0 and conteo_especiales > 0:
        return "La contraseña es muy segura."
    else:
        sugerencias = []
        if len(contrasena) < 8:
            sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
        if conteo_mayusculas == 0:
            sugerencias.append("Incluye al menos una letra mayúscula.")
        if conteo_minusculas == 0:
            sugerencias.append("Incluye al menos una letra minúscula.")
        if conteo_numeros == 0:
            sugerencias.append("Incluye al menos un número.")
        if conteo_especiales == 0:
            sugerencias.append("Incluye al menos un carácter especial (!, $, %, etc.).")
        return sugerencias

# Interfaz de usuario con Streamlit
st.title("Evaluador de Contraseñas")
st.write("Pagina desarrollada por: Juan Pablo Zuluaga Mesa")
contrasena = st.text_input("Ingrese su contraseña:")

if contrasena:
    resultado = evaluar_contrasena(contrasena)
    if isinstance(resultado, str):
        st.success(resultado)
    else:
        st.warning("La contraseña no es lo suficientemente segura. Sugerencias:")
        for sugerencia in resultado:
            st.write("- " + sugerencia)
