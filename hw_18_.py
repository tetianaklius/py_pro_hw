# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності,
#  закон якої задається за допомогою функції користувача.
#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів,
#  що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.

def func_g(func, x: int = 1, n: int = 3):
    """
    :param func: user`s function
    :param x: first element of sequence
    :param n: number of elements of sequence
    :return: next element of sequence
    """
    i = 0
    while i < n:
        yield x
        x = func(x)
        i += 1


def user_func_1(x: int):
    return x * 2


def user_func_2(x: int):
    return x ** 3


g = func_g(user_func_1, 1, 10)
p = func_g(user_func_2, 10, 3)

c = []
for item in g:
    if len(c) > 10:
        g.close()
        break
    print(item)
    c.append(item)

for item in p:
    print(item)


# 2. Використовуючи замикання, реалізуйте такий прийом програмування як мемоїзація.
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n-го члена ряду Фібоначчі.
# Порівняйте швидкість виконання із просто рекурсивним підходом.
import timeit

stmt_1 = """
def fib():
    fib_seq = [0, 1]
    
    def get_next(n):
        if n < len(fib_seq):
            return fib_seq[n]
            
        curr, next = fib_seq[-2], fib_seq[-1]
        i = len(fib_seq)

        while i <= n:
            curr, next = next, curr + next
            fib_seq.append(next)
            i += 1

        return next

    return get_next
f = fib()
f(25)
"""

stmt_2 = """
def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)
recur_fib(25)
"""

stmt_3 = """
import functools
@functools.lru_cache
def recur_fib_tools(n):
    if n <= 1:
        return n
    else:
        return recur_fib_tools(n - 1) + recur_fib_tools(n - 2)  
recur_fib_tools(25)
"""



print(timeit.timeit(stmt_1, number=10)) #2
print(timeit.timeit(stmt_2, number=10)) #3
print(timeit.timeit(stmt_3, number=10)) #1


# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача
# і поверне суми елементів отриманого списку.

def x_sum(x_func, x_list):
    c = x_func(x_list)
    return sum(c)


def x_func(x_list):
    b = [i ** 2 for i in x_list]
    return b


s = [1, 2, 3, 4, 5]
print(x_sum(x_func, s))
