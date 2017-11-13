from __future__ import division
import os
import xml.etree.ElementTree as ET
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *
from collections import Counter
import sklearn

import re


# Declaring path of xml texts
path = '/Users/hafi/PycharmProjects/TextminNewsCategorization/trainset'

# Get clean text in <p> in xml file

paragraph = [] # Store all sentences inside xml's code <p> until </p>
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    for text in root.iter('text'):
        for p in text.iter('p'):
            paragraph.append(p.text)


# Preprocessing all clean data text on array paragraph from function getDataText
letters_lowered = [] # Store all lowered letters
letters_regexed = [] # Store all regexed letters
letters_splited = [] # Store all splited letters
stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
filteredWords   = [] # Store all filtered words according to stopwords_en.txt
wordLemma       = WordNetLemmatizer()
stemmer         = PorterStemmer()
words_lemmatized= []
Bag_of_Words = words_lemmatized

for i in range(len(paragraph)):
    lowered = paragraph[i].lower()  # Lowering all capital letters to lowered letters
    letters_lowered.append(lowered)  # Inserting to array letters_lowered
    regexed = re.sub(r'[^a-z]', ' ', letters_lowered[i])  # Removing all numbers, punctuations, and symbols
    letters_regexed.append(regexed)
    splited = letters_regexed[i].split()
    letters_splited.append(splited)

for j in range(len(letters_splited)):
    for k in range(len(letters_splited[j])):
        if letters_splited[j][k] not in stopword:
            filteredWords.append(letters_splited[j][k])

for l in range(len(filteredWords)):
    words_stemmed = stemmer.stem(filteredWords[l])
    words_lemmatized.append(wordLemma.lemmatize(words_stemmed))

# print filteredWords

# import nltk
# from nltk.collocations import *
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(filteredWords)
# y= finder.nbest(bigram_measures.pmi, 20)
# finder1 = BigramCollocationFinder.from_words(Bag_of_Words)
# yu= finder1.nbest(bigram_measures.pmi, 20)
#
# print y
# print ''
# print yu


# from collections import Counter
# list1=['apple','egg','apple','banana','egg','apple']
# counts = Counter(list1)
# freq=[]
#
# a= sum(counts.values())
# # print a
#
# for i in counts:
#     print i, counts[i]
#     print i
#     print counts[i]
#     freq.append(counts[i] / sum(counts.values()))
#     print freq
#
# x= type(counts[i])
# y= type(a)
# print x
# print y

from nltk import bigrams
import collections
import math


countedWords= collections.Counter(words_lemmatized) #a2
bigramsCountedWords= collections.Counter(bigrams(countedWords)) #a3
a4=sum([countedWords[x]for x in countedWords])
a5=sum([bigramsCountedWords[x]for x in bigramsCountedWords])
a6={x:float(countedWords[x])/a4 for x in countedWords} # word probabilities(w1 and w2)
a7={x:float(bigramsCountedWords[x])/a5 for x in bigramsCountedWords} # joint probabilites (w1&w2)
u = {}
v = {}
for x in a6:
  k={x:round(math.log((a7[b]/(a6[x] * a6[y])),2),4) for b in a7 for y in a6 if x and y in b}
  u[x] = k[x]
  k={x:round(math.log((a7[b]/(a6[x] * a6[y])),2),4) for b in a7 for y in a6 if x in b and y in b}
  v[x] = k[x]
print u