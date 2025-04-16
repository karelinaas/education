# Задание 3. match ... case VS. if ... else ... elif
#
# Где именно "match ... case" подходит намного лучше, чем "if ... else ... elif"
# ?
#
# Во-первых, "match ... case" доступен только с версии Python 3.10+ )) То есть,
# если версия ниже, нам остаётся использовать только "if ... else ... elif".
#
# В случае с Python 3.10+:
# Если у нас много вариантов выбора (напр., используется какая-то структура
# данных, список, словарь) и при этом проверка не требует сложных логических
# вычислений, можно использовать match.
#
# Если вариантов 2-3, ЛИБО условие сложное - используем if.
#
# Но вообще, смотрим уместность по ситуации, насколько более читаемым стал код.
#
# В качестве примера предлагаю тебе (в этой задаче и в следующей) переписать
# неудобные конструкции с "if ... else ... elif" на "match ... case" и оценить,
# насколько читаемее стал код.
#
# И вот еще отличная статья по теме: https://habr.com/ru/articles/585216/

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    VIOLET = 4
    ORANGE = 5
    WHITE = 6
    BLACK = 7
    PINK = 8
    TRANSPARENT = 3


def handle_color_if(color: int) -> str:
    if color == Color.RED:
        return "Это роза."
    elif color == Color.BLUE:
        return "Это колокольчик."
    elif color == Color.VIOLET:
        return "Это фиалка."
    elif color == Color.ORANGE:
        return "Это бархатец."
    elif color == Color.WHITE:
        return "Это ландыш."
    elif color == Color.PINK:
        return "Это пион."
    elif color in (Color.GREEN, Color.BLACK, Color.TRANSPARENT):
        return "Это, скорее всего, не цветок."

    return "Ошибка обработки."

def handle_color_match(color: int) -> str:
    match color:
        case Color.RED:
            return "Это роза."
        case Color.BLUE:
            return "Это колокольчик"
        case Color.VIOLET:
            return "Это фиалка"
        case Color.ORANGE:
            return "Это бархатец"
        case Color.WHITE:
            return "Это ландыш"
        case Color.PINK:
            return "Это пион"
        case Color.TRANSPARENT | Color.GREEN | Color.BLACK:
            return "Не цветок"
        # В этом задании вообще всё отлично!
        # Единственное, можно учесть, что в метод могут передать что-то вообще не из енама Color.
        case _:
            return "Ошибка обработки."


for color in Color:
    print(color)
    print("handle_color_if", handle_color_if(color))
    print("handle_color_match", handle_color_match(color))
    print("--------------------")
