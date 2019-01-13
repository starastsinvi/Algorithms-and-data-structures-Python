# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

N = int(input('введите количество элементов массива: '))
min_el = int(input('введите нижнюю границу массива: '))
max_el = int(input('введите верхнюю границу массива: '))

arr = [randint(min_el, max_el) for _ in range(N)]
print(arr)

min_id = 0
max_id = 0
for i in range(1, N):
    if arr[i] < arr[min_id]:
        min_id = i
    elif arr[i] > arr[max_id]:
        max_id = i
print(arr[min_id], arr[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id + 1, max_id):
    summa += arr[i]
print(summa)
