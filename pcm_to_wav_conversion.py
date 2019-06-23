import wave
import os
import re
import librosa

for dirpath, dirnames, files in os.walk(path_dir):
    for file_name in files:
        if file_name.endswith('.pcm'):
            fname = dirpath + '/' + file_name
            with open(fname, 'rb') as pcmfile:
                pcmdata = pcmfile.read()
            print(pcmdata)
            with wave.open(fname[:-4]+'.wav', 'wb') as wavfile:
                wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
                wavfile.writeframes(pcmdata)
