# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint

N = int(input('введите количество элементов массива: '))
min_el = int(input('введите нижнюю границу массива: '))
max_el = int(input('введите верхнюю границу массива: '))

arr = [randint(min_el, max_el) for _ in range(N)]
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])
