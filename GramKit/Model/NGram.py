from GramKit.Corpus.StatInfo import Corpus, SimpleCorpus
from collections import Counter
import math


class NGramModel():
    def __init__(self, n: int):
        self.n = n
        self.wordSet = set()
        self.word2Count = dict()
        self.ngramsCounter = Counter()
        self.prefixCounter = Counter()
        self.probaOfUnkown = 1e-6

    def init(self):
        NotImplemented

    def printSummarization(self):
        # print(self.word2count.values())
        print("totalWordCount ", sum(self.word2Count.values()))
        print("totalUniqueWordCount ", len(self.wordSet))
        print("Work Frequency: ")
        for token in self.wordSet:
            print(f"Word: {token} occurs {self.word2Count[token]} times.")

    def forward(self, segments):
        for seg in segments:
            tokens = [x.lower for x in seg.split()]
            for word in tokens:
                if word not in self.word2Count:
                    self.word2Count[word] = 0
                else:
                    self.word2Count

    def forward_infer(self, preSentence, postSentence):
        potentialWord2score = dict()
        for word in self.word2count.keys():
            test_sentence = preSentence[-(self.n - 1)] + [word] + postSentence[:(self.n - 1)]
            potentialWord2score[word] = self.probability(test_sentence)
        return max(potentialWord2score.keys(), key=(lambda k: potentialWord2score[k]))

    def probability(self, segment):
        prob = 1
        ngrams = list(zip(*[segment[i:] for i in range(self.n)]))
        for ngram in ngrams:
            # prob *= (1 + self.ngramsCounter[ngram])/(len(self.prefixCounter) + self.prefixCounter[(ngram[i] for i in range(self.depth))])
            prob *= (1 + self.ngramsCounter[ngram]) / (len(self.prefixCounter))
        return prob

class NGramModel():
    def __init__(self, n, Corpus):
        self.n = n
        self.wordSet = Corpus.wordSet
        self.word2Count = Corpus.word2Count
        self.init(Corpus)

    def init(self, Corpus):
        ngramsList = []
        prefixList = []
        for seg in Corpus.segments:
            tokens = ['<BOS'] + [x.lower for x in seg.split()] + ['<EOS']
            ngrams = list(zip(*[tokens[i:] for i in range(self.n)]))
            prefix = list(zip(*[tokens[i:] for i in range(self.n-1)]))
            ngramsList += ngrams
            prefixList += prefix
        self.ngramsCounter = Counter(ngramsList)
        self.prefixCounter = Counter(prefixList)

class NGramSuccessorModel():
    def __init__(self):
        self.word2Count = dict()
        self.totalWordCount = 0

    def probability(self, token):
        return self.word2Count[token] / self.totalWordCount

    def forward(self, token):
        self.totalWordCount += 1
        if self.word2Count.get(token) == None:
            self.word2Count[token] = 1
        else:
            self.word2Count[token] += 1



class NGramSuccessorModel():
    def __init__(self):
        NotImplemented


if __name__ == "__main__":
    sc = SimpleCorpus()
    ngramModel = NGramModel(3, sc)
    ngramModel.printSummarization()
