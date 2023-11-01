import sympy
from sympy import symbols, sin, cos, sqrt, diff

x, y, z = symbols('x y z')

f = sin(x)**2 * cos(y) + sqrt(z + y)
 
df_dx = diff(f, x)
df_dy = diff(f, y)
df_dz = diff(f, z)

x_values = [-1, 1, 2]
y_values = [3, 2, 1]
z_values = [1, 3, 5]

for x_val, y_val, z_val in zip(x_values, y_values, z_values):
    result_dx = df_dx.subs([(x, x_val), (y, y_val), (z, z_val)])
    result_dy = df_dy.subs([(x, x_val), (y, y_val), (z, z_val)])
    result_dz = df_dz.subs([(x, x_val), (y, y_val), (z, z_val)])

    print(f"Для x = {x_val}, y = {y_val}, z = {z_val}:")
    print(f"df/dx = {result_dx}")
    print(f"df/dy = {result_dy}")
    print(f"df/dz = {result_dz}")
    print()
