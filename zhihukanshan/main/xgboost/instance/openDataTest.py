import pickle
import pandas as pd

# file_1 = open('word_wordVectorSet.pkl', 'rb')
# wordVectorSet = pickle.load(file_1)
# file_1.close()
# print wordVectorSet

# file_2 = open('word_vectorSet.pkl', 'rb')
# vectorSet = pickle.load(file_2)
# file_2.close()
# print vectorSet

word_wordVectorSet = pd.read_csv('word_embedding.csv')
print word_wordVectorSet