import string
import os
import speech_recognition as sr
import distance
import seaborn as sns
import matplotlib.pyplot as plt

class Speech:
    def __init__(self):
        self.original = []
        self.recognized = []
        self.distances = []

    def read_original(self, inFile):
        f = open(inFile, 'r')
        idx = 0
        self.original.append([])
        punct = string.punctuation
        punct += '’'
        for line in f:
            for c in punct:
                line = line.replace(c, '')
            for word in line.split():
                self.original[idx].append(word.lower())
            self.original.append([])
            idx += 1


    def conv_audio(self, inDir):
        audio_files_to_text = ['' for _ in range(25)]
        r = sr.Recognizer()
        # convert to string
        for file in os.listdir(inDir):
            tens_digit = 0
            idx = file.find('.')
            file_base = file[:idx]
            if file_base[-2].isnumeric():
                tens_digit = (ord(file_base[-2]) - 48) * 10
            ones_digit = ord(file_base[-1]) - 48
            file_joined = os.path.join(inDir, file)
            message = ""
            with sr.WavFile(file_joined) as source:
                audio = r.record(source)
                message = r.recognize_google(audio)
            position = (tens_digit + ones_digit) - 1
            audio_files_to_text[position] = message
        # parse
        for idx,  line in enumerate(audio_files_to_text):
            punct = string.punctuation
            punct += '’'
            self.recognized.append([])
            for c in punct:
                line = line.replace(c, '')
            for word in line.split():
                self.recognized[idx].append(word.lower())

    def comp_string(self):
        for s1, s2 in zip(self.original, self.recognized):
            score = distance.levenshtein(s1, s2) / max(len(s1), len(s2))
            self.distances.append(score)

def read_in_all_audio_submissions(inFile, inDir):
    result = [[] for _ in range(25)]
    for the_dir in os.listdir(inDir):
        sp = Speech()
        sp.read_original(inFile)
        sp.conv_audio(os.path.join(inDir, the_dir))
        sp.comp_string()
        for idx, value in enumerate(sp.distances):
            result[idx].append(value)
    return result


if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(20,10))
    x = ['Sent{i}'.format(i = i + 1) for i in range(25)]
    results = read_in_all_audio_submissions("How Speech Recognition Works.txt", "audio_files")
    sns.boxplot(x, results, ax = ax)
    plt.show()
