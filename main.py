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
def main_tree():
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

def main_branch():
    up()
    goto(0,-100)
    left(90)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))


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
#print(koch(2,100))

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


def freeze_fract(n, a):
    down()
    if n == 0:
        forward(a)
    else:
        freeze_fract(n-1,a/2)
        left(90)
        freeze_fract(n - 1, a / 4)
        freeze_fract(n - 1, -a / 4)
        right(90)
        freeze_fract(n - 1, a / 2)
        up()
'''
def dragon_reverse(n,a):
    down()
    if n == 0:
        backward(a)
        return
    left(90)
    dragon_reverse(n - 1, a)
    right(90)
    dragon_reverse(n - 1,a)
    left(90)
def dragon(n,a):
    down()
    if n == 0:
        forward(a)
        return
    dragon(n - 1, a)
    right(90)
    dragon_reverse(n - 1,a)
    left(90)
'''
def dragon_reverse(n,a):
    down()
    if n == 0:
        forward(a)
        return
    dragon(n-1, a)
    right(90)
    dragon_reverse(n - 1, a)

def dragon(n,a):
    down()
    if n == 0:
        forward(a)
        return
    dragon(n-1, a)
    left(90)
    dragon_reverse(n - 1, a)

#print(dragon_reverse(1,60))
#exitonclick()




def numbers(x):
    if x // 10 == 0:
        return x
    print(x%10)
    return numbers(x//10)

def destobin(x):
    if x < 2:
        return str(x)
    return destobin(x // 2) + str(x % 2)


def deston(x,n):
    if x < n:
        return str(x)
    return deston(x // n, n) + str(x % n)

def function1(x):
    d = 2
    while True:
        if x == d:
            return 1
        elif x % d ==0:
            return 0
        d += 1


def pifagor_tree(a,n):
    if n == 0:
        return quad(a)
    quad(a)
    up()
    left(90)
    forward(a)
    right(45)
    down()
    pifagor_tree((a**2/2)**0.5, n-1)
    home()
    pifagor_tree((a**2/2)**0.5, n - 1)

def quad(a):
    for i in range(0,4):
        forward(a)
        left(90)



exitonclick()
