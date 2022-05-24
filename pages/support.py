import streamlit as st
from PIL import Image

def app():
    image = Image.open('assets/bass_logo.png')
    meme = Image.open('assets/meme.jpg')
    st.image(image)
    st.subheader('You can help this project!')
    st.markdown("""You can support my project by donating some money. This donations will go to maintain the server.
        Don't forget to leave a coment in transaction with your name or nickname. I wiil put it to the list of people, who supported my project
        on the web-page of application""")
    st.markdown("**Sberbank:** 4274 3200 7261 1406")
    st.markdown("**Tinkoff:** 4377 7237 7782 1079")
    st.markdown("""Also you can support project by upgrading code of the project on GitHub: https://github.com/Dron-Adron/basstranscriber""")
    st.image(meme)