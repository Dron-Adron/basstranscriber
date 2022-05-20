import streamlit as st
from PIL import Image

def app():
    image = Image.open('assets/bass_logo.png')
    st.image(image)
    st.title('About project')