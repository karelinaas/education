# Задание 4. match ... case VS. if ... else ... elif
#
# Допустим, ты проектируешь робота, который принимает команды в виде
# последовательностей слов и чисел, например `ЗВУК 440 3`. Разбив команду на
# части и разобрав числа, мы должны получить сообщение вида ['BEEPER', 440, 3].
# а затем обработать его, вызвав соответствующий метод.
#
# Много других примеров и очень интересный разбор возможностей match есть
# в книге Л. Рамальо "Python – к вершинам мастерства" (со стр. 65 и далее)


class Led:
    brightness: float | int = 0
    color: str = '#000000'

    def set_brightness(self, ident: int, brightness: float | int):
        self.brightness = brightness
        print(f'Яркость светодиода {ident} выставлена на {self.brightness}.')

    def set_color(
        self,
        ident: int,
        red: float | int,
        green: float | int,
        blue: float | int,
    ):
        self.color = f'#{red:02X}{green:02X}{blue:02X}'
        print(f'Цвет светодиода {ident} выставлен на {self.color}.')


class Robot:
    leds: list[Led] = []

    def __init__(self):
        self.leds = [Led(), Led(), Led()]

    def beep(self, times: int, frequency: float | int):
        for i in range(times):
            print(f"{i}. Издаю звук с частотой {frequency:.2f}")

    def rotate_neck(self, angle: float | int):
        print(f"Поворачиваю голову на {angle} градусов")

    def handle_command(self, command: str):
        message = []
        # TODO тут опционально: или переписать на match, или просто сделать более адеватную, удобочитаемую проверку
        # или оставить как есть))
        for part in command.split():
            if part.isdigit() and part.replace('.', '').isdigit():
                message.append(int(part))
            elif not part.isdigit() and part.replace('.', '').isdigit():
                message.append(float(part))
            else:
                message.append(part)

        # TODO переписать на match. Как видишь, код совсем не удобочитаемый + возможна куча IndexError.
        match message[0]:
            case 'ЗВУК':
                self.beep(message[2], message[1])
            case 'ПОВЕРНИ_ГОЛОВУ':
                self.rotate_neck(message[1])
            case 'ДИОД':
                if len(message) == 5:
                    self.leds[message[1]].set_color(*message[1:])
                else:
                    self.leds[message[1]].set_brightness(message[1], message[2])
            case _:
                raise InvalidCommand(command)



class InvalidCommand(Exception):
    def __init__(self, custom_message: str | None = None):
        message = "!!! Неизвестная команда. "
        if custom_message:
            message += custom_message
        super().__init__(message)


commands = [
    'ПОВЕРНИ_ГОЛОВУ -45',
    'ДИОД 1 120',
    'СЛОМАЙСЯ',
    'ДИОД 2 100',
    'ДИОД 1 177 52 235',
    'ЗВУК 696.9 3',
    'ПОВЕРНИ_ГОЛОВУ 30',
]

robot = Robot()

for command in commands:
    try:
        robot.handle_command(command)
    except InvalidCommand as e:
        print(e)

# Вывод должен быть таким:

# Поворачиваю голову на -45 градусов
# Яркость светодиода 1 выставлена на 120.
# !!! Неизвестная команда. СЛОМАЙСЯ
# Яркость светодиода 2 выставлена на 100.
# Цвет светодиода 1 выставлен на #B134EB.
# 0. Издаю звук с частотой 696.90
# 1. Издаю звук с частотой 696.90
# 2. Издаю звук с частотой 696.90
# Поворачиваю голову на 30 градусов
