
# coding: utf-8

# In[ ]:


__author__ = 'Щедрин Андрей Викторович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
a = int(input('Введите целое беззнаковое число '))
b = list(str(a))
i = 0
c = []
while i < len(b):
    c.append(b[i])
    i += 1
k = 0
max = int(c[0])
while k < len(c):
    if int(c[k]) > max:
        max = int(c[k])
        k += 1
    else:
        max = max
        k += 1
print('Максимальная цифра в данном числе: ' + str(max))


# In[ ]:


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
a = input('Введите число a: ')
b = input('Введите число b: ')
a = [a]
a.append (b)
b = a[0]
a = a[1]
print ('Переменная а равна ' + a)
print ('Переменная b равна ' + b)


# In[ ]:


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = float(input('Введите значение переменной a '))
while True:
    if a == 0:
        a = float(input ('Значение a не может равняться 0. Введите значение a, отличное от 0: '))
    else:
        break
b = float(input('Введите значение переменной b '))
c = float(input('Введите значение переменной c '))
D = b**2 - 4 * a * c
if D < 0 :
    print ('У данного уравнения нет корней')
elif D == 0:
    x = (-b + math.sqrt(D)) / (2 * a)
    print ('У данного уравнения один корень х=' + str(x))
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print ('У данного уравнения два корня х1=' + str(x1) + ' и x2=' + str(x2))

