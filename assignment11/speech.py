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
        audio_files_to_text = [[] for _ in range(25)]
        r = sr.Recognizer()
        # convert to string
        for file in os.listdir(inDir):
            tens_digit = 0
            if file[-2].isnumeric():
                tens_digit = (ord(file[-2]) - 48) * 10
            ones_digit = ord(file[-1]) - 48
            message = r.recognize_google(file)
            audio_files_to_text[tens_digit + ones_digit].append(message)
        # parse
        for idx,  line in enumerate(audio_files_to_text):
            punct = string.punctuation
            punct += '’'
            for c in punct:
                line = line.replace(c, '')
            for word in line.split():
                self.recognized[idx].append(word.lower())
            self.recognized.append([])

    def comp_string(self):
        for s1, s2 in zip(self.original, self.recognized):
            score = distance.levenshtein(s1, s2) / max(len(s1), len(s2))
            self.distances.append(score)


if __name__ == '__main__':
    sp = Speech()
    sp.read_original("How Speech Recognition Works.txt")
    sp.conv_audio("audio_files")
    sp.comp_string()
    x = ['Sent{i}'.format(i = i) for i in range(25)]
    ax = sns.boxplot(x, sp.distances)
    plt.show()
