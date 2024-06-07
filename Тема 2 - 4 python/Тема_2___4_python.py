
import sympy as sp
import numpy as np

# Коэффициенты уравнения гиперболы
a, b = 3, 2

# Заданная точка
x0, y0, z0 = 1, 0, 0

# Проверка принадлежности точки гиперболе
def is_point_on_hyperbola(a, b, x0, y0):
    return (x0**2 / a**2 - y0**2 / b**2) == 1

is_on_hyperbola = is_point_on_hyperbola(a, b, x0, y0)
print(f"Точка ({x0}, {y0}) {'принадлежит' if is_on_hyperbola else 'не принадлежит'} гиперболе.")

# Проверка пересечения плоскости с гиперболой
def does_plane_intersect_hyperbola(a, b, A, B, C, D):
    # Уравнение плоскости: Ax + By + Cz + D = 0
    # Подставляем x и y из гиперболы в уравнение плоскости и проверяем, существует ли решение для z
    x, y, z = sp.symbols('x y z')
    hyperbola_eq = x**2 / a**2 - y**2 / b**2 - 1
    plane_eq = A*x + B*y + C*z + D
    solutions = sp.solve((hyperbola_eq, plane_eq), (x, y, z))
    return len(solutions) > 0

# Коэффициенты плоскости (пример)
A, B, C, D = 1, -2, 1, -3
does_intersect = does_plane_intersect_hyperbola(a, b, A, B, C, D)
print(f"Плоскость {'пересекает' if does_intersect else 'не пересекает'} гиперболу.")

# Проверка пересечения прямой с гиперболой
def does_line_intersect_hyperbola(a, b, x_eq, y_eq, z_eq):
    # Уравнение прямой: x = x_eq, y = y_eq, z = z_eq (параметрически)
    # Подставляем x и y из прямой в уравнение гиперболы и проверяем, существует ли решение для параметра t
    t = sp.symbols('t')
    x = x_eq.subs(sp.symbols('t'), t)
    y = y_eq.subs(sp.symbols('t'), t)
    hyperbola_eq = x**2 / a**2 - y**2 / b**2 - 1
    solutions = sp.solve(hyperbola_eq, t)
    return len(solutions) > 0

# Уравнения прямой (пример)
x_eq = sp.sympify('1 + 2*t')
y_eq = sp.sympify('3 + t')
z_eq = sp.sympify('2 - t')
does_line_intersect = does_line_intersect_hyperbola(a, b, x_eq, y_eq, z_eq)
print(f"Прямая {'пересекает' if does_line_intersect else 'не пересекает'} гиперболу.")
