import math

# Square Root
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

# Power (Exponentiation)
def power(a, b):
    return math.pow(a, b)

# Trigonometric Functions (in radians)
def sine(a):
    return math.sin(a)

def cosine(a):
    return math.cos(a)

def tangent(a):
    return math.tan(a)

# Inverse Trigonometric Functions (returns in radians)
def arcsine(a):
    if a < -1 or a > 1:
        raise ValueError("Input for arcsin must be between -1 and 1")
    return math.asin(a)

def arccosine(a):
    if a < -1 or a > 1:
        raise ValueError("Input for arccos must be between -1 and 1")
    return math.acos(a)

def arctangent(a):
    return math.atan(a)

# Logarithms
def log_base_10(a):
    if a <= 0:
        raise ValueError("Logarithm input must be greater than zero")
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        raise ValueError("Logarithm input must be greater than zero")
    return math.log(a)

# Factorial
def factorial(a):
    if a < 0:
        raise ValueError("Factorial input must be non-negative")
    return math.factorial(a)
