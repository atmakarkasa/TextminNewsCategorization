from GetDataText import getText
from Preprocessing import preProcessing
from Training import likelihoodProbability

a= getText(path='/Users/hafi/PycharmProjects/TextminNewsCategorization/trainset')
b= preProcessing(a)
c= likelihoodProbability(b)
