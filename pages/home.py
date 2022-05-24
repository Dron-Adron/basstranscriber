import streamlit as st
from PIL import Image

def app():
        image = Image.open('assets/bass_logo.png')
        step1 = Image.open('assets/step1.jpg')
        step2 = Image.open('assets/step2.jpg')
        step3 = Image.open('assets/step3.jpg')
        step4_1 = Image.open('assets/step4_1.jpg')
        step4_2 = Image.open('assets/step4_2.jpg')
        step5_1 = Image.open('assets/step5_1.jpg')
        step5_2 = Image.open('assets/step5_2.jpg')
        step6 = Image.open('assets/step6.jpg')
        step7 = Image.open('assets/step7.jpg')
        st.image(image)
        st.subheader('About the project')
        st.markdown("""Greetings to all who have visited this page! My name is Andrey and I 
                am the developer of basstranscriber.com. As the name suggests, this application 
                performs the ability to transcribe bass guitar songs into tablature format. 
                The algorithm works as follows: the audio track is divided into fragments and 
                each containing one note. Then FFT transforming each fragment. After that, function choose 
                frequency with the max magnitude and another function compare this frequencies with the dict, wich 
                contain patterns of notes and their frequencies. This function choosing the nearest note. This project was 
                created as part of the final qualifying work and will be improved in the future. If 
                you would like to support the project, please visit the "Support my project" section in 
                the sidebar of the web-page.""")
        st.subheader('How to start')
        st.markdown("""In order to start using the system, you need to go to the section "Transcriber".""")
        st.image(step1)
        st.markdown("""After going to the "Transcriber" section, enter the CAPTCHA verification code 
                so that the system makes sure that you are not a robot.""")
        st.image(step2)
        st.markdown("""After successfully passing the test, you will have the opportunity 
                to upload a bass guitar song for analysis. The file must have a ".wav" extension.""")
        st.image(step3)
        st.markdown("""When the file is loaded, a graph of the ratio of loudness to time 
                will appear. According to this graph, it will be necessary to cut the 
                melody into fragments of separately played notes. The vertical axis is the 
                dBFS division, and the horizontal axis is the millisecond division. You can 
                interact with the graph: you can zoom in, zoom out, and when you hover over 
                the mouse, you can see the value of a certain sound peak.""")
        st.image([step4_1, step4_2], use_column_width = True)
        st.markdown("""In the "Interval" field, you can choose the intensivity of time scale. The default value is 1. This 
                means that the graph is not compressed and is displayed in detail. If 
                you enter a value of 100, for example, then the graph will already be less detailed 
                and the millisecond axis values will be divided by 100. So if the standard 
                display of the division graph was “2000, 4000, 6000”, then when the division is 
                compressed, it will be “200, 400, 600” . This function is designed for convenience and 
                is recommended if the bass guitar song is quite long.""")
        st.image([step5_1, step5_2], use_column_width = True)
        st.markdown("""Next, you need to divide the melody into fragments using the "Minimum 
                silence length" and "Minimum silence threshold" sliders. The first parameter is 
                measured in dBFS. It will cut off all peaks below this value. The second 
                parameter is measured in milliseconds and its task is to divide the signal into 
                fragments. That is, all distances between peaks that are less than this parameter will 
                not be considered silence and, therefore, will be included in the fragment. The 
                settings for dividing a melody into fragments are best done based on the schedule""")
        st.image(step6)
        st.markdown("""Each time you change the division into fragments, the tablature will 
                be automatically updated until you get the best result.""")
        st.image(step7)