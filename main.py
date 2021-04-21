"""
Case-study 8: recursive functions (fractals)
Developers:
Кривошапова Д. Е.:20%
Кузнецов А. Д.:
Лапочкин Д. А.: 25%
"""
from turtle import *


def main():
    speed(10)
    fractal = input('''Введите цифру, соответсвующую одному из перечисленных ниже фракталов:
    1   "Убегающий" квадрат
    2   Двоичное дерево
    3   Фрактал "Ветка"
    4   Кривая Коха
    5   Снежинка Коха
    6   Кривая Минковского
    7   "Ледяной" фрактал (первый вариант)
    8   "Ледяной" фрактал (второй вариант)
    9   Кривая Леви
    10  Фрактал Дракон Хартера-Хейтуэя
''')
    if fractal == '1':
        square(int(input('Изначальная длина стороны квадрата: ')))
    elif fractal == '2':
        main_tree()
    elif fractal == '3':
        main_branch()
    elif fractal == '4':
        main_koch()
    elif fractal == '5':
        main_star_koch()
    elif fractal == '6':
        main_minkovskiy()
    elif fractal == '7':
        main_freeze_fract()
    elif fractal == '8':
        main_freeze_fract_second()
    elif fractal == '9':
        main_levi()
    elif fractal == '10':
        dragon(int(input('Глубина рекурсии: ')), int(input('Длина стороны: ')))
    done()


def main_tree():
    up()
    goto(0, -100)
    left(90)
    down()
    tree(int(input('Глубина рекурсии: ')), int(input('Угол отклонения ветки: ')))


def main_branch():
    up()
    goto(0, -100)
    left(90)
    down()
    branch(int(input('Глубина рекурсии: ')), int(input('Длина стороны: ')))


def main_koch():
    order = int(input('Глубина рекурсии: '))
    size = int(input('Длина стороны: '))
    up()
    goto(-size/2, 0)
    down()
    koch(order, size)


def main_star_koch():
    order = int(input('Глубина рекурсии: '))
    size = int(input('Длина стороны: '))
    up()
    goto(-size/2, size/4)
    down()
    for i in range(3):
        koch(order, size)
        right(120)


def main_minkovskiy():
    up()
    goto(-300, 0)
    down()
    minkovskiy(int(input('Глубина рекурсии: ')), int(input('Длина стороны: ')))


def main_freeze_fract():
    order = int(input('Глубина рекурсии: '))
    size = int(input('Длина стороны: '))
    up()
    goto(-size/2, 0)
    down()
    freeze_fract(order, size)


def main_freeze_fract_second():
    order = int(input('Глубина рекурсии: '))
    size = int(input('Длина стороны: '))
    up()
    goto(-400, 0)
    down()
    freeze_fract_second(order, size)


def main_levi():
    up()
    goto(-100, 0)
    down()
    levi(int(input('Глубина рекурсии: ')), int(input('Длина стороны: ')))


def square(a):
    if a < 0:
        return
    for i in range(4):
        forward(a)
        left(90)
    left(10)
    penup()
    forward(int(a / 10))
    pendown()
    square(a - 5)


def tree(n, angle):
    if n == 0:
        return
    forward(50)
    left(angle)
    tree(n-1,angle)
    forward(20)
    forward(-20)
    right(2*angle)
    tree(n-1, angle)
    forward(20)
    forward(-20)
    left(angle)
    forward(-50)


def branch(n, size):
    if n == 0:
        left(180)
        return
    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)
    forward(x)
    left(180)
    forward(size)


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)


def minkovskiy(n, a):
    if n == 0:
        forward(a)
    if n < 0:
        return
    minkovskiy(n-1,a)
    left(90)
    minkovskiy(n-1,a)
    right(90)
    minkovskiy(n-1,a)
    right(90)
    minkovskiy(n-1, a)
    minkovskiy(n-1, a)
    left(90)
    minkovskiy(n-1, a)
    left(90)
    minkovskiy(n-1, a)
    right(90)
    minkovskiy(n-1, a)


def freeze_fract(n, a):
    down()
    if n == 0:
        forward(a)
    else:
        freeze_fract(n-1, a/2)
        left(90)
        freeze_fract(n-1, a/4)
        freeze_fract(n-1, -a/4)
        right(90)
        freeze_fract(n-1, a/2)
        up()


def freeze_fract_second(order, size):
    if order == 0:
        forward(size)
    else:
        freeze_fract_second(order - 1, size)
        left(120)
        freeze_fract_second(order - 1, size/2)
        left(180)
        freeze_fract_second(order - 1, size/2)
        left(120)
        freeze_fract_second(order - 1, size/2)
        left(180)
        freeze_fract_second(order - 1, size/2)
        left(120)
        freeze_fract_second(order - 1, size)


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order-1, size/(2**0.5))
        right(90)
        levi(order-1, size/(2**0.5))
        left(45)


def dragon(n,a):
    down()
    if n == 0:
        forward(a)
        return
    dragon(n-1, a)
    left(90)
    dragon_reverse(n-1, a)


def dragon_reverse(n,a):
    down()
    if n == 0:
        forward(a)
        return
    dragon(n-1, a)
    right(90)
    dragon_reverse(n-1, a)


main()
