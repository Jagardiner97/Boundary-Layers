import sympy as sp

alpha = 2.2e-4
k = 2.4
h = 15
q = 7500

# Define symbols
s, x, t = sp.symbols('s x t')

# Define the function in Laplace domain
f_s = q * sp.exp(-sp.sqrt(s/alpha) * x) / (s*(k*sp.sqrt(s/alpha) - h))

# Perform inverse Laplace transform
f_t = sp.inverse_laplace_transform(f_s, s, t)

# Print the result
print("Inverse Laplace Transform of the given function:")
sp.pprint(f_t)
