# Задание 6. functools - частичное применение функции

# Напиши функцию, которая принимает на вход имя, приветствие и знак препинания, а
# возвращает строку вида "{приветствие}, {имя}{знак препинания}".
# Затем используй functools.partial, чтобы создать две новые функции:
# 1) всегда использует приветствие "Здравствуй" и знак "!".
# 2) всегда использует приветствие "Привет" и знак ".".

# В качестве доп. задания также можешь добавить аргумент "эмоция" (например,
# "весело", "грустно") и модифицировать partial, чтобы одна из функций добавляла
# его в приветствие.

from functools import partial

def send_greeting(greeting: str, name: str, separator: str, emotion: str | None = None) -> str:
    if emotion:
        return f"{emotion} {greeting}, {name}{separator}"
    else:
        return f"{greeting}, {name}{separator}"

# Частичное применение (тут пока без указания эмоции)
say_hello = partial(send_greeting, greeting="Здравствуй!", separator="!")
say_hi = partial(send_greeting, greeting="Привет!", separator=".")

# С эмоцией
say_sad_hello = partial(send_greeting, greeting="Привет!", separator=".", emotion="*грустно*")

print(say_hello(name = "Алиса"))  # Здравствуй, Алиса!
print(say_hi(name = "Боб"))       # Привет, Боб.
print(say_sad_hello(name = "Ваня"))  # *грустно* Здравствуй, Ваня!
