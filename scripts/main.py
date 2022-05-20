import array

from pydub.utils import get_array_type
from pydub import silence

import numpy as np
import scipy.fft
import scipy.signal

from scripts.calibrating import NOTES
from scripts.formating import formating_array_to_tab

def plot_song(song, interval):
    volume = [segment.dBFS for segment in song[::interval]]
    return volume

def get_note_freq(sample, max_frequency = 315):
    bit_depth = sample.sample_width * 8
    array_type = get_array_type(bit_depth)
    raw_audio_data = array.array(array_type, sample._data)
    n = len(raw_audio_data)

    freq_array = np.arange(n) * (float(sample.frame_rate) / n) 
    freq_array = freq_array[:(n // 2)] 
    raw_audio_data = raw_audio_data - np.average(raw_audio_data)

    freq_magnitude = scipy.fft.fft(raw_audio_data) 
    freq_magnitude = freq_magnitude[:(n // 2)] 

    if max_frequency:
        max_index = int(max_frequency * n / sample.frame_rate) + 1
        freq_array = freq_array[:max_index]
        freq_magnitude = freq_magnitude[:max_index]

        freq_magnitude = abs(freq_magnitude)
        freq_magnitude = freq_magnitude / np.sum(freq_magnitude)
    return freq_magnitude, freq_array

def detect_peak(freq_magnitude, freq_array):
    peak_indicies, props = scipy.signal.find_peaks(freq_magnitude, height=0.015)
    max_magnitude = 0
    max_freq = 0
    for i, peak in enumerate(peak_indicies):
        freq = freq_array[peak]
        magnitude = props["peak_heights"][i]
        if max_magnitude < magnitude:
            max_magnitude = magnitude
            max_freq = freq
    return max_freq

def recognize_note(freq):
    distance = 1e19
    for key in NOTES:
        if abs(NOTES[key] - freq) < distance:
            distance = abs(NOTES[key] - freq)
            best_note = key
    return best_note


def process(song, len, thresh):
    notes = silence.split_on_silence(song, min_silence_len = len, silence_thresh = thresh)
    note_list = []
    for item in notes:
        freq = detect_peak(*get_note_freq(item))
        note_list.append(recognize_note(freq))
    return note_list

def postprocess(note_array):
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
    return g_line + '\n' + d_line + '\n' + a_line + '\n' + e_line + '\n'