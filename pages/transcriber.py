import tempfile

import streamlit as st
import plotly.express as px
from PIL import Image
from pydub import AudioSegment

from scripts.main import plot_song, postprocess, process
from scripts.captcha import generate_captcha

captcha_image, captcha_text = generate_captcha()

def app():
    image = Image.open('assets/bass_logo.png')
    st.image(image)
    
    st.image(captcha_image, use_column_width=True)
    captcha_user_input = st.text_input('Enter the CAPTCHA')

    if captcha_text == captcha_user_input:
        uploaded_file = st.file_uploader("Choose a .wav file", type='wav')
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            with tempfile.NamedTemporaryFile(suffix='.wav') as f:
                f.write(bytes_data)
                f.seek(0)
                
                song = AudioSegment.from_file(f.name)
            
            st.audio(bytes_data)
            
            interval = st.number_input('Current interval of chart', value = 1)
            df = plot_song(song, interval)
            fig = px.line(df, markers=True)
            fig.update_layout(title='Cut your audio on min silence length and min silence threshold', 
                                xaxis_title='milliseconds/'+str(interval), 
                                yaxis_title='dBFS', 
                                hovermode="x")
            st.plotly_chart(fig, use_container_width=True)


            min_silence_len = st.slider('Min silence length', min_value=1, max_value=1000, value=100)

            silence_thresh = st.slider('Min silence threshold', min_value=-100, max_value=-1, value=-50)

            st.text(postprocess(process(song,min_silence_len,silence_thresh)))