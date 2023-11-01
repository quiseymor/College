import sympy
from sympy import symbols, sin, cos, sqrt
a, b, x = sympy.symbols('a b x')
f = 1 /(sqrt(2 * x** 2 - 1.3))

integral = sympy.integrate(f, (x, a, b))

integral = integral.subs([(a, 1), (b, 2)])

print("Значение интеграла:", integral)


#_____________________________________
import sympy
from sympy import symbols, sin, cos, sqrt
a, b, x = sympy.symbols('a b x')
f = sin(x + 1.4)/(0.8 + cos(2 * x**2 + 0.5))

integral = sympy.integrate(f, (x, a, b))

integral = integral.subs([(a, 3), (b, 2.2)])

print("Integral value:", integral)


#___________________________________
import sympy
from sympy import symbols, sin, cos, sqrt
a, b, x = sympy.symbols('a b x')
f = sqrt(0.8 * x**2 + 1)/(x + sqrt (1.5 * x**2 - 2))

integral = sympy.integrate(f, (x, a, b))

integral = integral.subs([(a, 1.9), (b, 1.5)])

print("Integral value:", integral)


#__________________________________
import sympy
from sympy import symbols, sin, cos, sqrt, tan
a, b, x = sympy.symbols('a b x')
f = tan(x)**2/(x**2 + 1)

integral = sympy.integrate(f, (x, a, b))

integral = integral.subs([(a, 1), (b, 0.2)])

print("Integral value:", integral)
