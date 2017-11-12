import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *

# Preprocessing all clean data text on array paragraph from function getDataText
def preProcessing(paragraph):

    letters_lowered = [] # Store all lowered letters
    letters_regexed = [] # Store all regexed letters
    letters_splited = [] # Store all splited letters
    stopword = [line.rstrip('\n\r') for line in open('stopwords_en.txt')]
    filteredWords    = [] # Store all filtered words according to stopwords_en.txt
    wordLemma = WordNetLemmatizer()
    stemmer = PorterStemmer()
    words_lemmatized = []

    for i in range(len(paragraph)):
        lowered = paragraph[i].lower() # Lowering all capital letters to lowered letters
        letters_lowered.append(lowered) # Inserting to array letters_lowered
        regexed = re.sub(r'[^a-z]', ' ', letters_lowered[i]) # Removing all numbers, punctuations, and symbols
        letters_regexed.append(regexed) # Inserting to array letters_regexed
        splited = letters_regexed[i].split() # Splitting every sentences into words
        letters_splited.append(splited) # Inserting to array letters_splited

    for j in range(len(letters_splited)):
        for k in range(len(letters_splited[j])):
            if letters_splited[j][k] not in stopword:
                filteredWords.append(letters_splited[j][k])

    for l in range(len(filteredWords)):
        words_stemmed = stemmer.stem(filteredWords[l])
        words_lemmatized.append(wordLemma.lemmatize(words_stemmed))

    return words_lemmatized


