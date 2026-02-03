import math


def square(a):
    return math.ceil(a * a)


user_input = input('Введите сторону квадрата: ').replace(',', '.')
num_a = float(user_input)

print(f"Площадь равна: {square(num_a)}")
