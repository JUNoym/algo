# 関数に関数を渡す
def func1(func, param):
    return func(param)


print(func1(len, 'adsjfpoasjdfpo'))

# 関数を返す関数
# 関数定義の中で定義する関数のことを「ローカル関数」と呼ぶ

print('--------------------------------')


def make_adder(x):
    def adder(y):
        return x + y
    return adder


print('--------------------------------')

# Closure


def outer(a, b):

    def inner():
        return a + b
    return inner


print(outer(1, 4))
f = outer(1, 4)
r = f()
print(r)

print('--------------------------------')


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area


cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.14159265)

print(cal1(10))
print(cal2(10))
