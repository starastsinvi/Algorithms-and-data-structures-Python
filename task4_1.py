# Найти сумму n элементов следующего ряда чисел: 1 - 0.5 0.25 - 0.125...
# Количество элементов(n) вводится с клавиатуры.

# python -m timeit -n 100 -s "import task4_1" "task4_1.summ_first()"

import cProfile

#n = int(input("введите количество элементов (n): "))

def summ_first(n):
    if n < 2:
        return 1
    return summ_first(n-1) + (-0.5)**(n-1)
#print("сумма (первый) = ", summ_first(n))

# 100 loops, best of 3: 2.43 usec per loop (10)
# 100 loops, best of 3: 3.69 usec per loop (15)
# 100 loops, best of 3: 5.06 usec per loop (20)
# 100 loops, best of 3: 6.26 usec per loop (25)

#cProfile.run('summ_first()')
# 10/1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_first) (10)
# 15/1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_first) (15)
# 20/1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_first) (20)
# 25/1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_first) (25)

def summ_loop(n):
    if n < 2:
        return 1
    b = -0.5
    summ = 1
    k = 1
    for _ in range(2, n+1):
        k = k*b
        summ = summ + k
    return summ
#print("сумма (второй) = ", summ_loop(n))

# 100 loops, best of 3: 1.1 usec per loop (10)
# 100 loops, best of 3: 1.41 usec per loop (15)
# 100 loops, best of 3: 1.73 usec per loop (20)
# 100 loops, best of 3: 2.12 usec per loop (25)

#cProfile.run('summ_loop()')
# 1    0.000    0.000    0.000    0.000 task4_1.py:27(summ_loop) (10)
# 1    0.000    0.000    0.000    0.000 task4_1.py:27(summ_loop) (15)
# 1    0.000    0.000    0.000    0.000 task4_1.py:27(summ_loop) (20)
# 1    0.000    0.000    0.000    0.000 task4_1.py:27(summ_loop) (25)

def summ_eq(n):
    return(1*(1-((-0.5)**n))/(1-(-0.5)))
#print("сумма (третий) = ", summ_eq(n))

# 100 loops, best of 3: 0.791 usec per loop (10)
# 100 loops, best of 3: 0.699 usec per loop (100)
# 100 loops, best of 3: 0.732 usec per loop (1000)
# 100 loops, best of 3: 0.703 usec per loop (10000)

#cProfile.run('summ(n)')

# 1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_eq) (10)
# 1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_eq) (100)
# 1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_eq) (1000)
# 1    0.000    0.000    0.000    0.000 task4_1.py:11(summ_eq) (10000)

# итог, первый вариант - что-то на подобии рекурсии, что и следовало ожижать - самый слабый алгоритм,
# как с точки зрения времени, так и с точки зрения памяти.
# второй алгоритм - цикл, тут уже и время получще и память не забиваем.
# третий - самый быстрый, готовая формула поиска суммы геом прогрессии (самое быстрое и самое нетребовательное)




