__author__ = "Huangxuanyu Gong"

#Walk through the data directory and print out a list of sentence
import os
import nltk

for filename in os.listdir('./data'):
    file = open('./data/' + filename, 'r', encoding = 'utf-8')
    txtfile = file.read()
    file.close()
    tokenizedstring = ""
    sent_text = nltk.sent_tokenize(txtfile)
    for sentence in sent_text:
        tokenized_text = nltk.word_tokenize(sentence)
        for word in tokenized_text:
            tokenizedstring += (word + ' ')
        tokenizedstring += '\n'
    tokenizedfile = open('./tokenized/' + filename, 'w')
    tokenizedfile.write(tokenizedstring)
    tokenizedfile.close()

