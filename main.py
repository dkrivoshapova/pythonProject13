from turtle import *


def square(a):
    if a<0:
        return
    for i in range(4):
        forward(a)
        left(90)
    left(10)
    penup()
    forward(int(a / 10))
    pendown()
    square(a - 5)

#square(100)

def tree(n,angle):
    if n==0:
        return
    forward(50)
    left(angle)
    tree(n-1,angle)
    forward(20)
    forward(-20)
    right(2*angle)
    tree(n - 1, angle)
    forward(20)
    forward(-20)
    left(angle)
    forward(-50)
def main_tree()
    up()
    goto(0,-100)
    left(90)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Угол отклонения ветки:'))
    branch(n,a)

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

def main_branch()
    up()
    goto(0,-100)
    left(90)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    branch(n,a)

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

def koch_main():
    up()
    goto(-100,0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)

def star_koch():
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    for i in range(3):
        koch(n, a)
        right(120)
