__author__ = "Huangxuanyu Gong"

from gensim.models import word2vec
import os

keywords = ['Obama', 'Trump', 'GOP', 'Democrats', 'wall', 'Mexico', 'abortion', 'gun', 'TPP', 'Paris']

for keyword in keywords:
    for model in os.listdir('./tokenizedmodels'):
        newsModel = word2vec.Word2Vec.load('./tokenizedmodels/' + model)
        print('The result of ' + model[:-10] + ' for ' + keyword + ' is the following:')
        print(newsModel.most_similar(positive = keyword))
        print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


