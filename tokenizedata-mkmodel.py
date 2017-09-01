__author__ = "Huangxuanyu Gong"

from gensim.models import word2vec
import os

for file in os.listdir('./tokenized'):
    data = word2vec.LineSentence('./tokenized/' + file)
    model = word2vec.Word2Vec(data, size = 100, window = 3, hs = 1, min_count = 1, sg = 1)
    model.save('./tokenizedmodels/' + file + '.model')
    print('Done with ' + str(file) + ' model.')

print('All Done')

