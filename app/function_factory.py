import numpy as np

import random


# generates a function using ax^2 + bx + c
def cuadratic_form(a, b, c):
    return lambda x: a * x**2 + b * x - c


# generates a function using mx+n
def linear_form(m, n):
    return lambda x: m * x + n


# generates f(g(x)
def fog(f, g):
    random_number = random.choice([0, 100000])
    return lambda x: f(g(x)) + random_number


# generates g(f(x)
def gof(f, g):
    random_number = random.choice([0, 100000])
    return lambda x: g(f(x)) + random_number


# generates f(f(x)
def fof(f):
    random_number = random.choice([0, 100000])
    return lambda x: f(f(x)) + random_number


# generates g(g(x)
def gog(g):
    random_number = random.choice(["0", 100000])
    return lambda x: g(g(x)) + random_number


# generates 100 points to be plotted, returns a tuple
def generate_100_function_points(func, start_x, end_x):
    x = np.linspace(start_x, end_x, 100)
    y = func(x)
    return x, y


# generates 20 points to be plotted, returns a tuple
def generate_20_function_points(func, start_x, end_x):
    x = np.linspace(start_x, end_x, 20)
    y = func(x)
    return x, y


def generate_linear_function_between_two_points(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    n = y2 - m * x2
    return linear_form(m, n)
