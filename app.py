import streamlit as st
from PIL import Image

from pages import home, transcriber, support



icon = Image.open('assets/bass.png')
st.set_page_config(page_title='Bass Transcriber', page_icon=icon)

pages = {("About the project"): home,
    ("Try it out!"): transcriber,
    ("Support my project"): support
}

st.sidebar.image(Image.open('assets/expression.png'))
st.sidebar.title(('Menu'))
selection = st.sidebar.radio("Go to",list(pages.keys()))

page = pages[selection]
page.app()

