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
    texto = "En construcción "   
    st.markdown(f'<p style="font-size: 45px; color: maroon;font-weight: bold;">{texto}</p>', unsafe_allow_html=True) 
    

if __name__ == "__main__":
    main()