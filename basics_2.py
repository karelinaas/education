# Задание 2. Ошибки и исключения

# Напиши собственный класс исключения, которое должно выбрасываться, если
# получена слишком длинная строка. Используй его в функции, которая принимает на
# вход строку answer и максимальную длину max_len, и если длина answer больше
# max_len, вызывает твое исключение с сообщением "Введён слишком длиный ответ
# (n симв. при максимальной длине m симв.). Повторите ввод.".
# Если же длина в рамках допустимого, возвращается True.


# Тут, видимо, не совсем понятно было задание)) Саму логику исключения можно и нужно писать в его классе,
# это и подразумевалось. Вот как это реализовала я:
class AnswerIsTooLong(Exception):
    def __init__(
        self,
        *,
        message: str | None = None,
        extra_info: tuple[int, int] | None = None,
    ):
        if not message:
            answer_info = ""
            if len(extra_info) >= 2:
                answer_info = (
                    f' ({extra_info[0]} симв. при максимальной длине '
                    f'{extra_info[1]} симв.)'
                )
            # У исключения всего 1 цель, поэтому можно зашить сообщение об ошибке и прямо в него.
            message = (
                "Введён слишком длиный ответ{answer_info}. Повторите ввод."
                .format(answer_info=answer_info)
            )
        super().__init__(message)


def validate_answer(answer: str, max_len: int) -> bool | None:
    len_answer = len(answer)
    if len_answer > max_len:
        raise AnswerIsTooLong(extra_info=(len_answer, max_len))
    return True

datasets = [
    [
        'Напиши собственный класс исключения, которое должно выбрасываться',
        100,
    ],
    [
        'Применено дискретное распределение',
        10,
    ],
    ['abcdef', 20],
    ['abcdef', 2],
]

for dataset in datasets:
    try:
        is_valid = validate_answer(*dataset)
        is_valid_str = '' if is_valid else ' не'
        print(f'Ответ "{dataset[0]}"{is_valid_str} валиден.')
    except AnswerIsTooLong as e:
        print(e)

# Вывод должен быть таким:

# Ответ "Напиши собственный класс исключения, которое должно выбрасываться" валиден.
# Введён слишком длиный ответ (34 симв. при максимальной длине 10 симв.). Повторите ввод.
# Ответ "abcdef" валиден.
# Введён слишком длиный ответ (6 симв. при максимальной длине 2 симв.). Повторите ввод.
