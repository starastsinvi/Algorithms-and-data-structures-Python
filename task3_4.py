# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

N = int(input('введите количество элементов массива: '))
min_el = int(input('введите нижнюю границу массива: '))
max_el = int(input('введите верхнюю границу массива: '))

arr = [randint(min_el, max_el) for _ in range(N)]
print(arr)

num = arr[0]
max_frq = 1

for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')