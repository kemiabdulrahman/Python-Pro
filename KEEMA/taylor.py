import math

def taylor_series(function, x, n):
    """
    Calculates the Taylor series of a given function at a given point x.
    function : function to calculate the Taylor series of
    x : point to evaluate the Taylor series at
    n : number of terms in the Taylor series
    """
    series = 0
    for i in range(n):
        series += (function(x, i) * (x ** i)) / math.factorial(i)
    return series

def function(x, i):
    """
    Example function to calculate the Taylor series of
    """
    if i == 0:
        return 1
    elif i == 1:
        return math.sin(x)
    else:
        return math.sin(x) + (math.cos(x) * i)

x = math.pi/4
n = 10
print("Taylor series for function sin(x) at x = {0} is {1}".format(x,taylor_series(function, x, n)))

