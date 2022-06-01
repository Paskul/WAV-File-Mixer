import os
import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd
import librosa
import pandas as pd
import scipy
from scipy.io.wavfile import write
from vscode_audio import Audio


def print_plot_play(x, Fs, text=''):
    """1. Prints information about an audio singal, 2. plots the waveform, and 3. Creates player
    
    Notebook: C1/B_PythonAudio.ipynb
    
    Args: 
        x: Input signal
        Fs: Sampling rate of x    
        text: Text to print
    """
    print('%s Fs = %d, x.shape = %s, x.dtype = %s' % (text, Fs, x.shape, x.dtype))
    plt.figure(figsize=(8, 2))
    plt.plot(x, color='gray')
    plt.xlim([0, x.shape[0]])
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    # ipd.display(ipd.Audio(data=x, rate=Fs))

def beep(songNumber):
    if songNumber == 1:
        ipd.display(ipd.Audio(fn_wav, autoplay=True))
    if songNumber == 2:
        ipd.display(ipd.Audio(fn_wav2, autoplay=True))
    
def creatingSongArray(wav, wav2):
    maxLength = 0
    if len(wav) > len(wav2):
        maxLength = len(wav)
    else:
        maxLength = len(wav2)
    workingWav = [0] * maxLength
    for i in workingWav:
        workingWav[i] = ((wav[i] + wav2[i])/2.0)
    #newWav = np.array(workingWav, dtype=np.int16)
    newWav = np.array(workingWav, dtype=np.float32)
    # scipy.io.wavfile.write("WrittenFile.wav", 44100, workingWav)

    # tempx, tempFs = librosa.load(templist, sr=None)
    print_plot_play(x=newWav, Fs=44100, text='WAV file 3: ')
    

# Read wav1
path = '/Users/pasca/Desktop/AudioPython/Songs'
fn_wav = os.path.join(path, 'Nirvana - Breed (Audio).wav')
x, Fs = librosa.load(fn_wav, sr=None)
print_plot_play(x=x, Fs=Fs, text='WAV file 1: ')
# beep(1);
# Audio(fn_wav, sr=None)

# Read wav2
path2 = '/Users/pasca/Desktop/AudioPython/Songs'
fn_wav2 = os.path.join(path2, 'Nirvana - Territorial Pissings (Audio).wav')
x2, Fs2 = librosa.load(fn_wav2, sr=None)
print_plot_play(x=x2, Fs=Fs2, text='WAV file 2: ')
# beep(2);
# Audio(fn_wav2, sr=None)

creatingSongArray(wav=x, wav2=x2)

# Read mp3
# path = '/Users/pasca/Desktop/AudioPython/Songs'
# /Users/Bashir/Python/tutorials
# 'C:\Users\pasca\Desktop\AudioPython\Songs'
# fn_mp3 = os.path.join('..', 'data', 'B', 'FMP_B_Note-C4_Piano.mp3')
# x, Fs = librosa.load(fn_mp3, sr=None)
# print_plot_play(x=x, Fs=Fs, text='MP3 file: ')