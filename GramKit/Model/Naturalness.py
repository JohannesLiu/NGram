from GramKit.Corpus.Segments import NGram
from NGram import NGramModel, NGramSuccessorModel
import math
class Naturalness(object):
    def __init__(self, n, probaOfUnkown):
        self.n = n
        self.probaOfUnkown = probaOfUnkown
        self.ngramModel2ngramSuccessorModel = dict()
    def crossEntroopy(self, segments):
        probabilitySum = 0
        tokens = [x.lower() for x in segments]
        for i in range(len(tokens)):
            currentToken = tokens[i]
            currentNGram = tokens[max(0, i-self.n), i]
            modelProba = self.probability(currentNGram, currentToken)
            if modelProba == 0:
                proba = self.probaOfUnkown
            else:
                proba = modelProba * ( 1 - self.probaOfUnkown)
            probabilitySum = probabilitySum + math.log(proba)/math.log(2)

    def probability(self, ngram, token):
        return self.ngramModel2ngramSuccessorModel[ngram].probability(token)

    def forward(self, segment):
        tokens = [x.lower() for x in segment.strip().split(" ")]
        for i in range(len(tokens)):
            ngram = NGram(i, self.n)
            if self.ngramModel2ngramSuccessorModel.get(ngram) is None:
                self.ngramModel2ngramSuccessorModel(ngram, NGramSuccessorModel())
            ngramSuccessorModel = self.ngramModel2ngramSuccessorModel(ngram)
            ngramSuccessorModel.forward(tokens[i])

