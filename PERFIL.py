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
    texto = "Perfil"   
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True)
    
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Soy un apasionado Ingeniero de Sistemas graduado de la prestigiosa Universidad de Pamplona, con una sólida formación en el campo de la ingeniería. Mi enfoque principal se centra en las ciencias de la computación, programación, bases de datos y ciencias fundamentales. Cuento con un amplio conocimiento en programación avanzada y dominio en bases de datos SQL.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Mi constante búsqueda de crecimiento personal y desarrollo profesional me ha dotado de una inquebrantable capacidad de aprendizaje y adaptación para enfrentar desafíos. Poseo una pasión innata por encontrar soluciones efectivas y oportunas para satisfacer las necesidades de cualquier empresa o entidad.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Además, me enorgullece destacar que no solo soy un profesional altamente competente, sino también una persona íntegra y de valores arraigados. La honestidad, el respeto y la tolerancia son principios fundamentales en mi vida. Soy crítico en la búsqueda de la excelencia, autodidacta en mi constante desarrollo y orientado al logro de resultados sobresalientes. Mi empatía y compromiso me permiten establecer conexiones significativas con los demás y trabajar en equipo de manera efectiva.</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Siendo criado en un hogar que valora y cultiva principios sólidos, llevo en mí un espíritu de integridad y ética que se refleja en todas mis acciones. Estoy listo para asumir nuevos retos y contribuir con mi conocimiento y habilidades.</p>', unsafe_allow_html=True)
    
    


if __name__ == "__main__":
    main()