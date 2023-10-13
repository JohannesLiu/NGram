from collections import Counter
class CorpusStatInfo(object):
    def __init__(self, name):
        self.name = name
        self.segments = []
        self.wordSet = set()
        self.word2Count = dict()
        self.totalWordCount = 0
        self.totalUniqueWordCount = 0
        self.ngramsList = []
        self.prefixList = []

    def init(self):
        self.loadData()
        self.stats()

    def append(self, segment: str):
        self.segments.append(segment)

    def loadData(self):
        NotImplemented

    def stats(self):
        for seg in self.segments:
            tokens = [x.lower() for x in seg.strip().split(" ")]
            for token in tokens:
                self.wordSet.add(token)
                if token not in self.word2Count:
                    self.word2Count[token] = 1
                    self.totalUniqueWordCount +=1
                else:
                    self.word2Count[token] += 1
                self.totalWordCount += 1

    def printSummarization(self):
        print("totalWordCount ", self.totalWordCount)
        print("totalUniqueWordCount ", self.totalUniqueWordCount)
        print("Work Frequency: ")
        for token in self.wordSet:
            print(f"Word: {token} occurs {self.word2Count[token]} times.")

class SimpleCorpusStatInfo(CorpusStatInfo):
    def __init__(self):
        CorpusStatInfo.__init__(self, "simple")
        self.init()

    def loadData(self):
        self.append("The quick brown fox jumps over the lazy dog")
        self.append("I enjoy reading books on a rainy day")
        self.append("She danced gracefully to the rhythm of the music")
        self.append("The sunset painted the sky in shades of orange and pink.")
        self.append("He took a deep breadth and plunged into the icy water")
        self.append("The aroma of freshly brewed coffee filled the air")
        self.append("We hiked through the dense forest, surrounded by towering trees")
        self.append("The children giggled as they played in the sprinklers")
        self.append("The old man sat on the porch, rocking back and forth in his chair")
        self.append("The city lights shimmered in the distance, creating a mesmerizing view")

if __name__=="__main__":
    sc = SimpleCorpusStatInfo()
    sc.printSummarization()

