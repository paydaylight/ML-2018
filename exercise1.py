import re
import numpy
import math
numpy.set_printoptions(threshold=numpy.nan)
    
def cosineDistance(a, b):
    dotProd = 0.0
    sqvA = 0.0
    sqvB = 0.0
    for i in range(len(a)):
        dotProd += a[i] * b[i]
        sqvA += a[i] * a[i]
        sqvB += b[i] * b[i]
    return 1 - (dotProd/(math.sqrt(sqvA) * math.sqrt(sqvB)))

def elemUnique(list):
    ret = []
    for i in list:
        if i not in ret:
            ret.append(i)
    return ret

t = open('C:/Users/User/Desktop/sentences.txt').read().lower()

tokens = re.split('[^a-z]', t)
tokens = ' '.join(tokens).split() #лист всех слов текста

tokenSet = elemUnique(tokens) #сет уникальных элементов
d = dict(enumerate(tokenSet)) #словарик уникальных слов

arr = []
cnt = 0
sent = t.split('.\n') #каждая строка отдельно
while cnt < len(sent):
    arr.append(sent[cnt]) #лист предложений текста
    cnt += 1

matrixA = numpy.zeros((len(sent), len(tokenSet)))
for i in range(len(sent)):
    token = re.split('[^a-z]', arr[i])
    token = ' '.join(token).split()
    for j in token:
        if j in token:
            matrixA[i][tokenSet.index(j)] += 1
            
matrixB = []
for i in range(len(sent)):
    matrixB.append(cosineDistance(matrixA[0], matrixA[i]))
    
print(matrixB)
