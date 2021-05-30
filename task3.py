import pickle


class UnigramMorphAnalyzer:

    def __init__(self):
        self.statistics = {}

    def train(self):
        with open('train.txt', encoding='utf8') as train:
            for line in train:
                line = line.split()
                word, pos = line[0], line[1]
                if len(word) < 4:
                    len_word = len(word) + 1
                else:
                    len_word = 5
                for i in range(1, len_word):
                    if word[-i:] in self.statistics:
                        if pos in self.statistics[word[-i:]]:
                            self.statistics[word[-i:]][pos] += 1
                        else:
                            self.statistics[word[-i:]][pos] = 1
                    else:
                        self.statistics[word[-i:]] = {pos: 1}

    def predict(self, token):
        for i in self.statistics:
            if i == token[-4:]:
                print(self.statistics[i])
            elif i == token[-3:]:
                print(self.statistics[i])
            elif i == token[-2:]:
                print(self.statistics[i])
            elif i == token[-1:]:
                print(self.statistics[i])

    def save(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.statistics, f, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open('data.pickle', 'rb') as f:
            self.statistics = pickle.load(f)
           



