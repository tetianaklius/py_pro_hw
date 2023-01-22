# 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
#  Генератор повинен зупинити свою роботу або після досягнення зазначеного елементу, або при передачі команди на завершення.

def func_1(n: int, x: int = 1):
    """
    :param n: multiplier
    :param x: the initial element of the progression
    :return: /yield/ element of the progression
    """
    while True:
        yield x
        x *= n


g = func_1(3, 1)
for item in g:
    if item > 1_500:
        g.close()
        break
    print(item)


# 2. Реалізуйте свій аналог генераторної функції range().

def my_range(*args):
    start, stop, step = 0, None, 1
    if len(args) == 1:
        stop = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError()

    if not isinstance(start, int):
        raise TypeError()
    if not isinstance(stop, int):
        raise TypeError()
    if not isinstance(step, int):
        raise TypeError()

    if not step:
        raise ValueError()
    if step < 0 and stop > start:
        return
    if step > 0 and stop < start:
        return

    while abs(start) <= abs(stop):
        yield start
        start += step


print(*my_range(-20, 20, 2))


# 3. Напишіть функцію-генератор, яка повертатиме прості числа.
# Верхня межа діапазону повинна бути задана параметром цієї функції.

def simple_gen(m: int):
    """
    :param m: The upper limit of the range
    :return: prime numbers of the range
    """
    for i in range(2, m + 1):
        for y in range(2, i):
            if not i % y:
                break
        else:
            yield i


x = simple_gen(100)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for i in x:
    print(i)


# 4. Напишіть генераторний вираз для заповнення списку.
# Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.

m = 15
x = (n ** 3 for n in range(2, m))
print(*x)
