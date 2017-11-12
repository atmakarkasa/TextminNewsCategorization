from __future__ import division
from collections import Counter

def likelihoodProbability(words_lemmatized):
    frequencies = []
    counted_Words = Counter(words_lemmatized)
    total_Words = sum(counted_Words.values())

    for i in counted_Words:
        x = counted_Words[i] / total_Words
        frequencies.append(x)
    return frequencies



