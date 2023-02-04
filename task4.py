# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

n = int(input('Введите число N: '))
from random import randint
def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list
numbers = list(n)
print(numbers)
import random
random.shuffle(numbers)
print(numbers)