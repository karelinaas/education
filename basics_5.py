# Задание 5. functools - кэширование результатов функции
import time
# Напиши функцию, которая вычисляет факториал числа n. Используй
# functools.lru_cache, чтобы кэшировать результаты вычислений и избегать
# повторяющихся расчетов для одних и тех же аргументов.

# В качестве доп. задания еще можешь замерить время выполнения функции с
# кэшированием и без него для n = 400 (с помощью time.time()).

import functools

@functools.cache
def calculate_factorial(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n - 1)

# Без кэша
def factorial_no_cache(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n - 1)

# Замер времени
start = time.time()
calculate_factorial(400)
end = time.time()
print("Cached:", end - start)
start = time.time()
factorial_no_cache(400)
end = time.time()
print("No cache:", end - start)
