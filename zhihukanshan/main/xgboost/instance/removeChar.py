

# remove the character 'w' in word_embedding.txt

import numpy as np


def main():
    # dataMat_label = []
    dataMat_wordVectorSet =[]
    dataDirectory = 'D:/PycharmProjects/ZhiHuKanShan/zhihukanshan/data'
    # file_r = open(dataDirectory+'/dataOri/word_embedding.txt','r')
    file_r = open(dataDirectory+'/part_word_embedding_less.txt','r')
    output = open(dataDirectory+'/rem_part_word_embedding_less.txt','wb')
    line_1 = file_r.readline()
    line_2 = file_r.readline()

    output.write(line_1)
    output.write(line_2)
    for line in file_r.readlines():
        line_trim = line[1:]
        # curLine_label = curLine[:1]
        # curLine_label = curLine_label[0][1:]
        # dataMat_label.append(curLine_label)
        # # print dataMat_label
        # print line_trim
        output.write(line_trim)

    file_r.close
    output.close
    return
main()