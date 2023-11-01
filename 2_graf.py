from math import pi
from sympy import *
from sympy.abc import f,x
from sympy.plotting import plot


f=(2+sin(x)**2)/(1+x**2)

print(f)
plot(f,(x, -2, 1.5))


#________________________________________________
from sympy.abc import z,x,y

y= 5 * sin(pi*x) - cos(3*pi*x)
z= cos(2 * pi * x)  - 2 * sin(pi * x)**3

print(y)
print(z)
plot(y,z,(x,-2,2))


#_______________________________________________
from sympy.plotting import plot3d
from sympy.abc import z,x,y

z = 5 * x**2 * cos(y)**2 - 2 * y**2 * exp(y)

print(z)
plot3d(z,(x,-1,1),(y,-1,1))


#______________________________________________
from sympy.plotting import plot3d_parametric_line
from sympy.abc import x,y,t

x = 2*sin(t)**3
y = 2*cos(t)**3

print(x)
print(y)
plot3d_parametric_line(x,y,t,(t,-2*pi, 2*pi))






