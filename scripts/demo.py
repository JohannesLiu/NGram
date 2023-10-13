
n = 3
# fn = ("../resources/"
#       "")
all_words = set()
ngrams_list = []
prefix_list = []


# with open(fn) as f:
#     for line in f:
#         sentence = line.split()
#         word_list = [x.lower() for x in sentence]


sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print([sentence[i:] for i in range(n)])
print(*[sentence[i:] for i in range(n)])


print(list(zip(*[sentence[i:] for i in range(n)])))


