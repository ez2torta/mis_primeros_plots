import numpy as np


# generates a function using ax^2 + bx + c
def cuadratic_form(a, b, c):
    return lambda x: a * x**2 + b * x - c


# generates a function using mx+n
def linear_form(m, n):
    return lambda x: m * x + n


# generates f(g(x)
def fog(f, g):
    return lambda x: f(g(x))


# generates g(f(x)
def gof(f, g):
    return lambda x: g(f(x))


# generates f(f(x)
def fof(f):
    return lambda x: f(f(x))


# generates g(g(x)
def gog(g):
    return lambda x: g(g(x))

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
