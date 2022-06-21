import os
import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd
import librosa
import pandas as pd
import scipy
from scipy.io.wavfile import write

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

def songLength(sampleRate, songData):
    return len(songData)/sampleRate
    
def creatingSongArray(wav, sample, wav2, sample2):
    sampleMaxLength = 0
    if len(wav) < len(wav2):
        sampleMaxLength = len(wav2)
    else:
        sampleMaxLength = len(wav)
    print(sampleMaxLength)

    magicNumber = (songLength(sample, wav))/(songLength(sample2, wav2))
    if magicNumber < 1:
        magicNumber = (songLength(sample2, wav2))/(songLength(sample, wav))

    if sample != sample2:
        if sample > sample2:
            #wav2 = scipy.signal.resample(wav2, len(wav), t=None, axis=0, window=None)
            wav2 = scipy.signal.resample(wav2, int(sampleMaxLength*magicNumber), t=None, axis=0, window=None,)
            sample2 = sample
        else:
            #wav = scipy.signal.resample(wav, len(wav2), t=None, axis=0, window=None)
            wav = scipy.signal.resample(wav, int(sampleMaxLength*magicNumber), t=None, axis=0, window=None,)
            sample = sample2

    maxLength = 0
    if len(wav) < len(wav2):
        maxLength = len(wav)
    else:
        maxLength = len(wav2)
    print(maxLength)

    workingWav = [0.0] * maxLength
    i = 0
    while i < maxLength:
        workingWav[i] = ((wav[i] + wav2[i])/2.0)
        i += 1

    # for i in workingWav:
        # workingWav[i] = ((wav[i] + wav2[i])/2.0)
        

    print(wav[44000])
    print(wav2[44000])
    print((wav[44000] + wav2[44000])/2.0)
    print(workingWav[44000])
    #print(wav[4045312])
    #print(wav2[4045312])
    #print((wav[4045312] + wav2[4045312])/2.0)
    #print(workingWav[4045312])
    newWav = np.array(workingWav, dtype=np.float32)
    print(len(newWav))
    scipy.io.wavfile.write("WrittenFile.wav", 44100, newWav)

    # tempx, tempFs = librosa.load(templist, sr=None)
    print_plot_play(x=newWav, Fs=sample, text='WAV file 3: ')
    

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

creatingSongArray(wav=x, sample=Fs, wav2=x2, sample2=Fs2)

# Read mp3
# path = '/Users/pasca/Desktop/AudioPython/Songs'
# /Users/Bashir/Python/tutorials
# 'C:\Users\pasca\Desktop\AudioPython\Songs'
# fn_mp3 = os.path.join('..', 'data', 'B', 'FMP_B_Note-C4_Piano.mp3')
# x, Fs = librosa.load(fn_mp3, sr=None)
# print_plot_play(x=x, Fs=Fs, text='MP3 file: ')