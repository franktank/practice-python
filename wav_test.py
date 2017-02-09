
# from audiolab import wavread
# from pylab import *
# http://stackoverflow.com/questions/36893767/plotting-audio-spectrogram-in-python
# http://dsp.stackexchange.com/questions/10152/spectrogram-of-wav-file
# signal, fs, enc = wavread('Humpback.wav')
# specgram(signal) <---?????
# pip install --no-index -f http://dist.plone.org/thirdparty/ -U PIL
# http://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file
# subplot from pylab??
# http://coreygoldberg.blogspot.com/2013/06/generating-audio-spectrograms-in-python.html


# ---- Useful Maybe for converting wav to spectrogram -----
# https://github.com/YerevaNN/Spoken-language-identification/blob/6a470b8b7e8472eb516ec6f0a92ca0747a8dba67/augment_data.py

# WAV FILES!! http://www.wavsource.com/

import matplotlib
matplotlib.use('Agg')
import argparse
import os
import sys
import matplotlib.pyplot as plt
from scipy.io import wavfile
from PIL import Image


def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    nfft = 256  # Length of the windowing segments
    fs = 256    # Sampling frequency
    pxx, freqs, bins, im = plt.specgram(data, nfft,fs)
    plt.axis('off')
    plt.savefig('dog_wav.png',
                dpi=100, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0) # Spectrogram saved as a .png

def retrieve_pixels():
    i = Image.open("dog_wav.png")

    pixels = i.load() # this is not a list, nor is it list()'able
    width, height = i.size

    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    write_template = open("pixels.txt", 'a')
    # print write_template
    for line in all_pixels:
        #print line
        write_template.write(" ".join(str(elem) for elem in line) + "\n")
    write_template.close()
    print all_pixels

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    print data
    return rate, data

if __name__ == '__main__': # Main function
    wav_file = 'dog_growl3.wav' # Filename of the wav file
    graph_spectrogram(wav_file)
    retrieve_pixels()
# End of code