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
    texto = "EXPERIENCIA LABORAL"   
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True) 

    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>INSOFT. Ingeniero Desarrollador. </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Mayo 2021 – Nov 2022. (Teletrabajo) Bogotá, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Soporte, desarrollo y mantenimiento a aplicativos de la empresa en Java Script Básico, Delphi y SQL FireBird.  Implementación e integración de proyectos de la empresa. Software principal (<a href="https://www.contapyme.com/" target="_blank">www.contapyme.com </a>), cabe destacar que fui el que implemento el calculo de la nomina y en el ultimo proyecto hacia desarrollos y soporte al sistema de ticket interno de la empresa desarrollado en su totalidad en Delphi .</p>', unsafe_allow_html=True)
    
    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Food Club. Administrador. </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Junio 2017 – diciembre 2021. Arauca, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Administrador de restaurante de comidas rápidas. Supervisión de la limpieza y orden de las instalaciones y de su adecuado abastecimiento, realización de las tareas administrativas correspondientes al negocio y de trámites ante entidades públicas.  Atención personalizada al cliente y seguimiento de consultas y reclamos. Coordinación de actividades, delegación de tareas y supervisión de los empleados. </p>', unsafe_allow_html=True)
    
    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Secretaría de Movilidad Distrital. Ingeniero de Sistemas. </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Mayo 2016 – febrero 2017. Bogotá, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Desarrollo de requerimientos para los módulos del ERP SICAPITAL en los lenguajes Oracle Forms y Report 10g y 11g, Soporte al ERP Empresarial de la entidad especialmente el módulo de contratación de la entidad y demás funciones asignadas por jefe inmediato.</p>', unsafe_allow_html=True)
    
    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Secretaria de Educación del Distrito de Bogotá, Ingeniero de Sistemas. </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Junio 2013 – enero 2015. Bogotá, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">desarrollo de requerimientos para los módulos del ERP SICAPITAL (SICO) en los lenguajes Oracle Forms y Report, Mantenimiento al sistema de matrículas online del Distrito.</p>', unsafe_allow_html=True)
    
    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Cobiscorp (Desarrollo Bancario). </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Marzo 2012 – agosto 2012. Bogotá, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">desarrollo de requerimientos para los módulos cobis (software bancario) en los lenguajes Visual Basic 6 y Visual Basic .NET (front end).</p>', unsafe_allow_html=True)
    
    st.write("<p style='font-weight: bold;font-size: 25px; display: inline;'>Universidad Cooperativa de Colombia. Docente. </p> ", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px; display: inline;'>Julio 2009 – septiembre 2010. Arauca, Colombia.</p>", unsafe_allow_html=True)
    st.markdown(f'<p style="font-size: 20px; display: inline;text-align: justify;">Docente tiempo completo a cargo de las cátedras de bases de datos (PostgreSQL, mysql), Programación (java básico), matemáticas y Algebra lineal.  </p>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
