# coding: utf-8

#!/usr/bin/python

from __future__ import division

import numpy as np
import xgboost as xgb

# label need to be 0 to num_class -1
data = np.loadtxt('./dermatology.data', delimiter=',',
        converters={33: lambda x: int(x == '?'), 34: lambda x: int(x)-1})
sz = data.shape

#以sz[0] * 0.7 为分界点，划分训练集和测试集
train = data[:int(sz[0] * 0.7), :]
test = data[int(sz[0] * 0.7):, :]

train_X = train[:, :33]
train_Y = train[:, 34]

test_X = test[:, :33]
test_Y = test[:, 34]

xg_train = xgb.DMatrix(train_X, label=train_Y)
xg_test = xgb.DMatrix(test_X, label=test_Y)

# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 6

watchlist = [(xg_train, 'instance'), (xg_test, 'test')]
num_round = 5  # Number of boosting iterations.
bst = xgb.train(param, xg_train, num_round, watchlist)  # watchlist: (parameter: eval) List of items to be evaluated during training, this allows user to watch performance on the validation set.
# get prediction
pred = bst.predict(xg_test)
error_rate = np.sum(pred != test_Y) / test_Y.shape[0]
print('Test error using softmax = {}'.format(error_rate))

# do the same thing again, but output probabilities
#采用softprob再计算一遍。softprob给出的结果是：一共六种皮肤病，测试集中每一个sample，属于任一种皮肤病的概率
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist)
# Note: this convention has been changed since xgboost-unity
# get prediction, this is in 1D array, need reshape to (ndata, nclass)
#pred_prob是一个被reshape为ndata*nclass的矩阵，给出的是每一个sample属于任一种皮肤病的概率
pred_prob = bst.predict(xg_test).reshape(test_Y.shape[0], 6)
pred_label = np.argmax(pred_prob, axis=1)
error_rate = np.sum(pred != test_Y) / test_Y.shape[0]
print('Test error using softprob = {}'.format(error_rate))
