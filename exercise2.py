import math
import numpy
import matplotlib.pyplot as plt

def F(x): #наша функция
    return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

def solveMatrix(arr): #функция для решения матрицы
    matrixCoef = numpy.zeros(shape=(len(arr), len(arr))) #матрица коэфицентов
    matrixAnsw = [] #матрица ответов
    for i in range(len(arr)): #в зависимости от размера матрицы заполняем коэффиценты
        matrixAnsw.append(F(arr[i])) #добавляем в матрицу ответов решения
        for j in range(len(arr)):
            matrixCoef[i][j] = arr[i]**j #подсчитываем коэффиценты
    return numpy.linalg.solve(matrixCoef, matrixAnsw) #возвращяем решения

in1 = [1, 15]
in2 = [1, 8, 15]
in3 = [1, 4, 10, 15]
#вызываем функцию от инпутов
y1 = solveMatrix(in1)
y2 = solveMatrix(in2)
y3 = solveMatrix(in3)

print(y1)
print(y2)
print(y3)
#рисуем график
plt.plot(in1, y1)
plt.plot(in2, y2)
plt.plot(in3, y3)
