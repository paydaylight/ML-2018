from scipy.optimize import minimize
import numpy
import math
import matplotlib.pyplot as plt

def F(x): #наша функция
    return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

x = numpy.arange(1, 30, .1) #точки графика
mini = minimize(F, 2, method='BFGS') #подсчитываем по методу BFGS для 2
print(round(float(mini.fun, 2)) #первый ответ
mini = minimize(F, 30, method='BFGS')
print(round(float(mini.fun, 2)) #второй ответ

plt.plot(x, list(map(F, x)))#рисуем график
