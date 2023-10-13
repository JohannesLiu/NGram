from GramKit.Corpus.Segments import NGram, Segment
import numpy as np

class NaturalnessModel(object):
    def __init__(self, n, probaOfUnkown = 1e-6):
        self.n = n
        self.probaOfUnkown = probaOfUnkown
        self.ngramModel2ngramSuccessorModel = dict()
    def crossEntroopy(self, segment):

        if len(segment) == 0 or segment == None:
            return self.probaOfUnkown
        probabilitySum = 0
        # words = [x.lower() for x in segment.strip().split(" ")]
        tokens = Segment(segment).data
        for i in range(len(tokens)):
            currentToken = tokens[i]
            currentNGram = NGram(tokens[max(0, i-self.n): i])
            modelProba = self.probability(currentNGram, currentToken)
            if modelProba == 0:
                proba = self.probaOfUnkown
            else:
                proba = modelProba * ( 1 - self.probaOfUnkown)
            probabilitySum = probabilitySum + np.log(proba)/np.log(2)
        return - (probabilitySum / len(tokens))

    def probability(self, ngram, token):
        if self.ngramModel2ngramSuccessorModel.get(ngram) is None or NGram is None:
            return 0
        return self.ngramModel2ngramSuccessorModel[ngram].probability(token)

    def forward(self, segment):
        tokens = Segment(segment)
        for i in range(len(tokens.data)):
            ngram = tokens.buildNGram(i, self.n)
            if self.ngramModel2ngramSuccessorModel.get(ngram) is None:
                self.ngramModel2ngramSuccessorModel[ngram] = NGramSuccessorModel()
            ngramSuccessorModel = self.ngramModel2ngramSuccessorModel[ngram]
            ngramSuccessorModel.forward(tokens.data[i])

class NGramSuccessorModel():
    def __init__(self):
        self.word2Count = dict()
        self.totalWordCount = 0

    def probability(self, token):
        if self.word2Count.get(token) is None:
            return 0
        return self.word2Count[token] / self.totalWordCount

    def forward(self, token):
        self.totalWordCount += 1
        if self.word2Count.get(token) == None:
            self.word2Count[token] = 1
        else:
            self.word2Count[token] += 1

