import string

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
        print(self.original)


    def conv_audio(self, inDir):
        pass

    def comp_string(self):
        pass

if __name__ == '__main__':
    s = Speech()
    s.read_original("How Speech Recognition Works.txt")

