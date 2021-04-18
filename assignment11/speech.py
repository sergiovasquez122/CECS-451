import string
import os
import speech_recognition as sr

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
                self.original[idx].append(word)
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
                self.recognized[idx].append(word)
            self.recognized.append([])

    def comp_string(self):
        pass

if __name__ == '__main__':
    s = Speech()
    s.read_original("How Speech Recognition Works.txt")

