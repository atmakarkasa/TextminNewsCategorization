from getDataText import getText
from Preprocessing import preProcessing

a= getText(path='/Users/hafi/PycharmProjects/TextminNewsCategorization/trainset')
b= preProcessing(a)
print b