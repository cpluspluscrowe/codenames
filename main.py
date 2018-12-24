#!/usr/bin/env python
import gensim.downloader as api
from gensim import corpora, models, similarities
word_vectors = api.load("glove-wiki-gigaword-100")


words = ['spike','staff','spider','code','dance','racket','snow','root','tap','torch','germany','africa','note','piano','worm','bed','bond','square','sock','pyramid','robot','back','wall','chest','bolt']

blue = ['spike']
red = ['spider','racket','snow','germany','bolt', 'torch']
white = ['staff','dance','tap','torch','africa','pyramid','robot','chest']



#chum, booger, spanky, rido,mammary,ingleside,genomic,leukemic,kwazulu,ips

#ring
# shoebox
# median, insurgency, feed, density, malaria, pigs, infected, functional
result = word_vectors.most_similar(positive=blue,negative = red, topn=20,restrict_vocab=5000)
# density, #commune
# surge
# datafile 3

d = {}
for word1 in blue:
    for word2 in blue:
        if word1 != word2:
            similarity = word_vectors.similarity(word1, word2)
            d[word1 + " " + word2] = similarity


import operator

sorted_x = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

for x in sorted_x:
    print(x)



#print(word_vectors.doesnt_match("breakfast cereal dinner lunch".split()))


#input = ""
#most_similar = 0
#most_similar_word = ""
#d = {}
#for word in words:
#    similarity = word_vectors.similarity(word,'cheese')
#    d[word] = similarity



#pigs for 3


