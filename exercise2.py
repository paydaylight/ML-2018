# coding: utf-8

# In[46]:


import math
import numpy
import matplotlib.pyplot as plt

def F(x): #наша функция
    return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

def matrix(arr): #создаем матрицу размерности nxn
    matrixCoef = numpy.zeros(shape=(len(arr), len(arr)))
    for i in range(len(arr)):
        for j in range(len(arr)):
            matrixCoef[i][j] = arr[i]**j
    return matrixCoef

def sumOfEle(arr, x): #подсчитываем сумму прогрессии нужной нам размерности
    out = numpy.zeros(shape=(len(x)))
    for i in range(len(x)):
        for j in range(len(arr)):
            out[i] += arr[j] * (x[i]**j)
    return out

x = numpy.arange(1, 15, .1) #наш набор точек от 1 до 15
in1 = [1, 15]
in2 = [1, 8, 15]
in3 = [1, 4, 10, 15]

m1 = matrix(in1)
m2 = matrix(in2)
m3 = matrix(in3)
#лист решений функции F(x)
l1 = list(map(F, in1)) 
l2 = list(map(F, in2))
l3 = list(map(F, in3))

answ1 = numpy.linalg.solve(m1, l1)
answ2 = numpy.linalg.solve(m2, l2)
answ3 = numpy.linalg.solve(m3, l3)
#подсчитываем Y
y = list(map(F, x))
y1 = sumOfEle(answ1, x)
y2 = sumOfEle(answ2, x)
y3 = sumOfEle(answ3, x)
#рисуем графики
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
