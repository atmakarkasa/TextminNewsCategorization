import os
import xml.etree.ElementTree as ET
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *
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

print words_lemmatized


