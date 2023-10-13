from GramKit.Corpus.StatInfo import CorpusStatInfo, SimpleCorpusStatInfo
from collections import Counter
import math

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
            tokens = [x.lower() for x in seg.split()]
            ngrams = list(zip(*[tokens[i:] for i in range(self.n)]))
            prefix = list(zip(*[tokens[i:] for i in range(self.n-1)]))
            ngramsList += ngrams
            prefixList += prefix
        self.ngramsCounter = Counter(ngramsList)
        self.prefixCounter = Counter(prefixList)



if __name__ == "__main__":
    sc = SimpleCorpusStatInfo()
    ngramModel = NGramModel(3, sc)
    ngramModel.printSummarization()
