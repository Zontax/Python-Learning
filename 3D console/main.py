# pip install windows-curses, colorama
import curses, locale
from math import pi, cos, sin
from colorama import init, Fore

init()
POS_X, POS_Y, POS_A = 2, 2, 0  # Положение и поворот игрока на карте (начальные)
FOV = pi / 2  # Ширина угла обзор в радинах
RESOLUTION = 0.1  # разрешение шага луча
DEPTH = 15  # Максимальная глубина прорисовки
SPEED = 0.4  # Скорость игрока вперед назад за одно нажатие
ROTATION_SPEED = 0.15  # скорость повотора игрока в радианах

# Карта
MAP = """
################
#...#..........#
#...#..........#
#...#####......#
#.......#......#
#####...#......#
#.......#......#
#..............#
#..........#...#
#............#.#
#..........#...#
#............#.#
#..........#...#
###..........#.#
###........#...#
################
"""


def make_map(string_map):
    """
    Форматирует карту в одну строку без переносов для лучшего поиска
    :param string_map: MAP
    :return: форматированная карта, ширина, высота в блоках
    """
    rows = string_map.strip().split('\n')
    h = len(rows)
    w = len(rows[0])
    return string_map.replace('\n', ''), w, h


def main_3dwalk(screen):
    # для корректного отображение юникода
    locale.setlocale(locale.LC_ALL, '')

    curses.noecho()  # кнопки не печатаются на экране
    curses.curs_set(0)  # курсор убран
    curses.start_color()  # цветной режим
    curses.use_default_colors()  # стандартная палитра

    # форматируем карту и получаем ее размеры
    level_map, map_width, map_height = make_map(MAP)

    def get_block(x, y):
        """
        По координатам  на карте возращает символ блока
        # - это стена, все остальное свободное пространство
        :param x: колонка
        :param y: строка
        :return: сивмвол блока
        """
        x, y = int(x), int(y)
        if 0 <= x < map_width and 0 <= y < map_height:
            return level_map[y * map_width + x]
        else:
            return '#'

    # текущие положение и угол
    pos_x, pos_y, pos_a = POS_X, POS_Y, POS_A

    exit_flag = False  # флаг выхода
    while not exit_flag:
        # полачем размер экрана в каждом кадре, чтобы не глючить, если юзер изменил размер терминала
        screen_height, screen_width = screen.getmaxyx()

        # по колонкам "пикселей на экране"
        for col in range(screen_width):
            # 1. определим направление луча
            # угол сканирует от pos_a - FOV / 2 до pos_a + FOV / 2
            ray_angle = (pos_a - FOV / 2) + (col / screen_width) * FOV

            # вектор, куда смотрит луч на карте
            eye_x, eye_y = sin(ray_angle), cos(ray_angle)

            # 2. Ищем ближайшую стену и дистанцию до нее
            distance = 0.0
            # пока не достигли стены и дистанция менее предельной
            while distance < DEPTH:
                # луч делает шаг вперед
                distance += RESOLUTION
                # "текущее" положение на луче
                test_x = int(pos_x + eye_x * distance)
                test_y = int(pos_y + eye_y * distance)
                # смотрим карту, есть ли там стена или край
                if get_block(test_x, test_y) == '#':
                    break  # стена. расстояние в distance

            # 3. Высота пола и потолка
            # Чем дальше стена, тем меньше она вертикально занимает на экране, а ниже и вышее ее - потолок и пол
            ceiling = int(screen_height / 2 -
                          screen_height / distance)  # высота потолка
            floor = int(screen_height - ceiling)  # высота пола

            # рисуем вертикальную линию
            for row in range(screen_height):
                if row <= ceiling:  # Ряд выше или равен границе потолка
                    shade = '`'
                elif floor >= row > ceiling:  # Кусок стены
                    if distance <= DEPTH / 4:  # совсем близко
                        shade = "█"
                    elif distance <= DEPTH / 3:  # ближе
                        shade = "▓"
                    elif distance <= DEPTH / 2:  # дальше
                        shade = "▒"
                    elif distance <= DEPTH:  # еще дальше
                        shade = "░"
                    else:
                        shade = "░"  # совсем далеко
                else:
                    # Оттенок пола, чем ближе к низу экрана, тем гуще заливка
                    b = 1 - (row - screen_height / 2) / (screen_height / 2)
                    if b < 0.25:
                        shade = '#'
                    elif b < 0.5:
                        shade = "x"
                    elif b < 0.75:
                        shade = "."
                    else:
                        shade = ' '
                # заменяем символ в row/col на shade с цветом color
                screen.insstr(row, col, shade)

        # информационная строка положения и поворота
        screen.addstr(screen_height - 1, 0,
                      f" x = {pos_x:.2f}, y = {pos_y:.2f}, a = {pos_a:.2f} ")

        screen.refresh()  # отрисуем все

        key_code = screen.getch()  # ждем клавишу и обрабатываем
        key = chr(key_code) if 0 < key_code < 256 else 0
        if key in ('w', 's'):
            # шаг вперед или назад
            dx, dy = sin(pos_a) * SPEED, cos(pos_a) * SPEED
            if key == 's':  # назад - обратим вектор
                dx, dy = -dx, -dy

            # сдвинем игрока в направлении
            pos_x += dx
            pos_y += dy
            if get_block(pos_x, pos_y) == '#':  # усп, мы в стене
                # отменим движение
                pos_x -= dx
                pos_y -= dy
        elif key == 'a':  # поворот налево
            pos_a -= ROTATION_SPEED
        elif key == 'd':  # поворот направо
            pos_a += ROTATION_SPEED
        elif key == chr(27):  # esc
            break

    # завершение работы, восстановление настроек
    curses.endwin()


curses.wrapper(main_3dwalk)
