from GramKit.Corpus.Segments import Segment, NGram
from GramKit.Corpus.StatInfo import CorpusStatInfo, SimpleCorpusStatInfo
from GramKit.Model.Naturalness import NaturalnessModel



def test_1():
    sc = SimpleCorpusStatInfo()
    model = NaturalnessModel(3, 0)

    segments = ["I like eating apple", "I hate eating orange", "She like having bread", "I do like drinking"]

    for seg in segments:
        model.forward((seg))
    seg2learn = segments
    seg2test = ""
    print(f"\nSeg2learn {seg2learn}")
    print(f"seg2test {seg2test}")
    result = model.crossEntroopy(segments[-1])
    print(f"Cross Entropy: {result}")

def test_2():
    seg2learn = ""
    seg2test = ""
    print(f"\nSeg2learn {seg2learn}")
    print(f"seg2test {seg2test}")
    model = NaturalnessModel(3, 0)
    result = model.crossEntroopy(seg2test)
    print(f"Cross Entropy: {result}")

def test_3():
    seg2learn = ""
    seg2test = "a b c d c"
    print(f"\nSeg2learn {seg2learn}")
    print(f"seg2test {seg2test}")
    model = NaturalnessModel(3, 0)

    result = model.crossEntroopy(seg2test)
    print(f"Cross Entropy: {result}")

def test_4():
    seg2learn = "a b c d e"
    seg2test = "a b c d c"
    print(f"\nSeg2learn {seg2learn}")
    print(f"seg2test {seg2test}")
    model = NaturalnessModel(3)
    model.forward(seg2learn)
    result = model.crossEntroopy(seg2test)
    print(f"Cross Entropy: {result}")


def test_5():
    seg2learn = "a b c d e"
    seg2test = "f f f f f f"
    print(f"\nSeg2learn {seg2learn}")
    print(f"seg2test {seg2test}")
    model = NaturalnessModel(3)
    model.forward(seg2learn)
    result = model.crossEntroopy(seg2test)
    print(f"Cross Entropy: {result}")
