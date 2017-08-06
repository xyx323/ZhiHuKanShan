from numpy import *
import pickle
import kMeans
import pandas as pd


def main():

    dataDirectory = 'D:/PycharmProjects/ZhiHuKanShan/zhihukanshan/data'

    list_DataMat_wordVectorSet = kMeans.loadDataSet(dataDirectory+'/rem_word_embedding.txt')
    # matDataMat_Label = mat(listDataMat_label)
    # matDataMat_wordVectorSet = mat(list_DataMat_wordVectorSet)
    matDataMat_wordVectorSet = pd.DataFrame(list_DataMat_wordVectorSet)

    # store the matDataMat_Label into word_label.pkl
    # output_1 = open('word_wordVectorSet.pkl', 'wb')
    # Pickle dictionary using protocol 0.
    # pickle.dump(matDataMat_wordVectorSet, output_1)
    # output_1.close

    matDataMat_wordVectorSet.to_hdf('rem_word_embedding.h5','df')
    # matDataMat_wordVectorSet.to_csv('rem_word_embedding.csv')
    # print matDataMat_wordVectorSet
    # print matDataMat_wordVectorSet[0,5]

    # # store the matDataMat_vectorSet into word_vectorSet.pkl
    # output_2 = open('word_vectorSet.pkl', 'wb')
    # # Pickle dictionary using protocol 0.
    # pickle.dump(matDataMat_vectorSet, output_2)
    # output_2.close
    #
    # print matDataMat_vectorSet


main()
