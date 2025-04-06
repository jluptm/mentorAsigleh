import streamlit as st
import pandas as pd

#from deta import Deta
from PIL import Image

imagen1 = Image.open('pres01/01.jpg')
imagen2 = Image.open('pres01/02.jpg')
imagen3 = Image.open('pres01/03.jpg')
imagen4 = Image.open('pres01/04.jpg')
imagen5 = Image.open('pres01/05.jpg')
imagen6 = Image.open('pres01/01.jpg')

st.image(imagen1)
st.image(imagen2)
st.image(imagen3)
st.image(imagen4)
st.image(imagen5)
st.image(imagen6)