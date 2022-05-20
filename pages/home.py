import streamlit as st
from PIL import Image

def app():
    image = Image.open('assets/bass_logo.png')
    st.image(image)
    st.title('About project')
    st.subheader('Test')
    st.markdown("""Test""")
    st.subheader('Test2')
    st.markdown("""Test2""")
    st.subheader('Test3')
    st.markdown("""Test3""")