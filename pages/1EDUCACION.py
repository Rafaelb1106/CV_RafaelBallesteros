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
    texto = "EDUCACIÓN"  
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)

    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Bootcamp de Data Science, </p> <p style='font-size: 25px; display: inline;'>2023</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Hack a Boss – España.</p>", unsafe_allow_html=True)

    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Especialización en Gerencia Ambiental, </p> <p style='font-size: 25px; display: inline;'>2020</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Corporación Universitaria Remington. - Colombia.</p>", unsafe_allow_html=True)

    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Ingeniero de Sistemas, </p> <p style='font-size: 25px; display: inline;'>2009</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Universidad de Pamplona - Pamplona, Norte de Santander, Colombia.</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Declaración de equivalencia España, Exp: 1030-1111270, 2023.</p>", unsafe_allow_html=True)

    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Bachiller, </p> <p style='font-size: 25px; display: inline;'>2000</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Colegio la Enseñanza - Arauca, Colombia.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()