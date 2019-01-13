# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

N = int(input('введите количество элементов массива: '))
min_el = int(input('введите нижнюю границу массива: '))
max_el = int(input('введите верхнюю границу массива: '))

arr = [randint(min_el, max_el) for _ in range(N)]

print(arr, end=' ')

mn = 0
mx = 0

for i in range(N):

    if arr[i] < arr[mn]:
        mn = i

    elif arr[i] > arr[mx]:
        mx = i

print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))

b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

print(arr, end=' ')

