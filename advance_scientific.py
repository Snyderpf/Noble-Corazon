import math

def arcsine(a):
    if a < -1 or a > 1:
        raise ValueError("Input must be between -1 and 1 for arcsin.")
    return math.asin(a)

def arccosine(a):
    if a < -1 or a > 1:
        raise ValueError("Input must be between -1 and 1 for arccos.")
    return math.acos(a)

def arctangent(a):
    return math.atan(a)

# Exponential and Logarithmic Functions
def exp(a):
    return math.exp(a)  # e^a

def natural_log(a):
    if a <= 0:
        raise ValueError("Input must be greater than zero for natural log.")
    return math.log(a)

def log_base_10(a):
    if a <= 0:
        raise ValueError("Input must be greater than zero for log base 10.")
    return math.log10(a)

# Factorial Function
def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(a)
