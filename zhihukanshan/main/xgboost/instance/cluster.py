
from numpy import *
import pandas as pd
import kMeans

def main():
    word_embedding_df = pd.read_hdf('rem_word_embedding.h5','df')
    word_embedding = mat(word_embedding_df.values) # .values is an array
    print 'word_embedding is loaded'
    m = word_embedding.shape[0]
    n = word_embedding.shape[1]
    print m;print n
    word_embedding_label = word_embedding[:,0]
    word_embedding_vector = word_embedding[:,1:]
    # print word_embedding_label
    # print word_embedding_vector
    myCentriods, clustAssing = kMeans.kMeans(word_embedding_vector,2700)
    print 'clustAssing:'
    print clustAssing

main()