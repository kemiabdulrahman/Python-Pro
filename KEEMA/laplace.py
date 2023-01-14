from sympy import symbols, exp, laplace_transform, inverse_laplace_transform

t = symbols('t')
f = exp(-2*t)

# Find the Laplace Transform of the function
F = laplace_transform(f, t, s)
print("Laplace Transform: ",F)

# Find the Inverse Laplace Transform of the function
f_inv = inverse_laplace_transform(F, s, t)
print("Inverse Laplace Transform: ",f_inv)

