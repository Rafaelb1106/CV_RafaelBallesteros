import streamlit as st
import numpy as np
import pandas as pd
import requests
import smtplib
from PIL import Image
from page_config_dict import PAGE_CONFIG
from page_config_dict import encabezado
st.set_page_config(**PAGE_CONFIG)
encabezado()

def main():
    texto = "PROYECTOS"   
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True) 

    texto = "1.	Currículum Vitae Interactivo con Streamlit y Python."   
    st.markdown(f'<p style="font-size: 20px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)     
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">La pagina actual fue una idea para plasmar mi Currículum de una manera interactiva y exponer algo de los conocimientos que he adquirido a lo largo de mi trayectoria profesional y educativa. Esta pagina es hecha con las tecnologías de Streamlit y Python. Donde Streamlit es una herramienta de código abierto que nos permite compartir aplicaciones web de datos personalizadas, la cual es elegante, intuitiva y funciona perfectamente con Python que por su parte es un lenguaje de programación extremadamente versátil y amigable para los usuarios con una sintaxis simple y legible lo cual lo ha convertido en un lenguaje muy popular y nos permite hacer múltiples cosas como script para analizar datos, construir sitios web, automatizar tareas y mucho más. </p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    texto = "2.	Proyecto Final Bootcamp Data Science."   
    st.markdown(f'<p style="font-size: 20px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)     
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">En el siguiente proyecto se puso en practica algunas de las cosas aprendidas en el bootcamp de data science de HackaBoss. </p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">En el proyecto podremos ver web scraping con las limitaciones que supone montarlo en streamlit, el cual no nos permite a nivel de la nube utilizar una librería de automatización muy popular como es Selenium la cual toma el control de un navegador y nos permite automatizar para hacer diferentes cosas como la extracción de información, en consecuencia utilizaremos otra librería muy popular como es Beatifulsoup, la cual nos permite analizar el HTML y extraer información de las webs.  </p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">Para el Recomendador se utiliza una técnica aprendida en el bootcamp, este sistema utiliza técnicas de aprendizaje automático para analizar las preferencias y generar recomendaciones que se alinean con los gustos individuales de usuario. </p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">El detector de objetos es una aplicación web dinámica e interactiva de ciencia de datos que utiliza algoritmos de aprendizaje automático profundo para identificar y clasificar imágenes introducidas por los usuarios. </p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">URL: <a href="https://proyectofinalhackabossrafaelbm.streamlit.app/" target="_blank" style="text-decoration: none;font-size: 17px; color: #000000;">https://proyectofinalhackabossrafaelbm.streamlit.app/</a></p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    texto = "3.	Análisis Detallado de la Encuesta Fair's Affairs: Dashboard en Power BI."   
    st.markdown(f'<p style="font-size: 20px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)     
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;">Presentamos nuestro avanzado dashboard en Power BI, construido a partir de los datos de la encuesta Fairs Affairs. Este recurso proporciona una visualización profunda y detallada de las respuestas, transformando datos cuantitativos en insights claros y accionables. </p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 17px; display: inline;text-align: justify;"><a href="https://projectpowerbi-encuesta-infidelidad.streamlit.app/" target="_blank" style="text-decoration: none;font-size: 20px; color: #000000;">Para más detalles dar clic aquí.</a></p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()