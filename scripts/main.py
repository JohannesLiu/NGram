import nltk

nltk.download('punkt')

training_text = "I enjoy playing soccer with my friends."

tokens = nltk.word_tokenize(training_text)

print(tokens)



