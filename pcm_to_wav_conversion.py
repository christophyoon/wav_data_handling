import wave
import os
import re
import librosa

# [7시]/[일곱시] 와 같은 문장 변환시켜주는 함수
def convertToKorean(matchObj):
    korean = matchObj.group(2)
    return korean


# Data root 경로
path_dir = r'C:\Users\vision\Desktop\Git\github_yeongtae_tacotron2\output\no_prosody'
dirs = os.listdir(path_dir)

# Directory명 -> Speaker label
dir2idx = {code:str(idx) for idx, code in enumerate(dirs)}

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



with open(path_dir + '\\transcript.txt', 'wt') as tranfile:
    for dir in dirs:
        if os.path.isdir(path_dir + '\\' + dir):
            for file in os.listdir(path_dir + '\\' + dir):
                if file.endswith('.txt'):
                    with open(path_dir + '\\' + dir + '\\' + file) as f:
                        txt = f.readline()[:-1].strip()
                        txt = re.sub(pattern=r'\[(.*?)\]/\[(.*?)\]',
                                     repl=convertToKorean,
                                     string=txt)

                    path = dir + '\\' + file
                    path = path.replace('.txt', '.wav')
                    speaker = dir2idx[dir]
                    line = path + '|' + txt + '|' + speaker + '\n'
                    tranfile.write(line)

with open('transcript_train.txt', 'r+') as tranfile: