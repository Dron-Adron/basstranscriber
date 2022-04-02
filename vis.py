import tempfile

import streamlit as st
import matplotlib.pyplot as plt

from pydub import AudioSegment, silence
from calibrating import NOTES
from formating import formating_array_to_tab

from main import plot_song, get_note_freq, detect_peak, recognize_note




uploaded_file = st.file_uploader("Choose a file", type='wav')
if uploaded_file is not None:
     # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    with tempfile.NamedTemporaryFile(suffix='.wav') as f:
        f.write(bytes_data)
        f.seek(0)
        
        song = AudioSegment.from_file(f.name)


    
    st.audio(bytes_data)



    fig, ax = plt.subplots()
    ax.plot(plot_song(song, 100))
    ax.minorticks_on()
    # Customize the major grid
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    # Customize the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.xlabel('Milliseconds')
    plt.ylabel('dBFS') 
    st.pyplot(fig)

    

    min_silence_len = st.slider('Min silence length', min_value=1, max_value=1000, value=100)

    silence_thresh = st.slider('Min silence threshold', min_value=-100, max_value=-1, value=-50)

    

    def len_n_thresh(len, thresh):
        notes = silence.split_on_silence(song, min_silence_len = len, silence_thresh = thresh)
        return notes
    
    notes = len_n_thresh(min_silence_len, silence_thresh)



    def create_note_array():
        note_list = []
        for item in notes:
            freq = detect_peak(*get_note_freq(item))
            note_list.append(recognize_note(freq))
        return note_list

    note_array = create_note_array()

    g_line = 'G|'
    d_line = 'D|'
    a_line = 'A|'
    e_line = 'E|'
    
    for note in note_array:        
        g_note,d_note,a_note,e_note = formating_array_to_tab(note)
        g_line += g_note
        d_line += d_note
        a_line += a_note
        e_line += e_note


    st.text(g_line + '\n' + d_line + '\n' + a_line + '\n' + e_line + '\n')