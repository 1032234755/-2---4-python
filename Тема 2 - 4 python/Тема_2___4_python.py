
import sympy as sp
import numpy as np

# ������������ ��������� ���������
a, b = 3, 2

# �������� �����
x0, y0, z0 = 1, 0, 0

# �������� �������������� ����� ���������
def is_point_on_hyperbola(a, b, x0, y0):
    return (x0**2 / a**2 - y0**2 / b**2) == 1

is_on_hyperbola = is_point_on_hyperbola(a, b, x0, y0)
print(f"����� ({x0}, {y0}) {'�����������' if is_on_hyperbola else '�� �����������'} ���������.")

# �������� ����������� ��������� � ����������
def does_plane_intersect_hyperbola(a, b, A, B, C, D):
    # ��������� ���������: Ax + By + Cz + D = 0
    # ����������� x � y �� ��������� � ��������� ��������� � ���������, ���������� �� ������� ��� z
    x, y, z = sp.symbols('x y z')
    hyperbola_eq = x**2 / a**2 - y**2 / b**2 - 1
    plane_eq = A*x + B*y + C*z + D
    solutions = sp.solve((hyperbola_eq, plane_eq), (x, y, z))
    return len(solutions) > 0

# ������������ ��������� (������)
A, B, C, D = 1, -2, 1, -3
does_intersect = does_plane_intersect_hyperbola(a, b, A, B, C, D)
print(f"��������� {'����������' if does_intersect else '�� ����������'} ���������.")

# �������� ����������� ������ � ����������
def does_line_intersect_hyperbola(a, b, x_eq, y_eq, z_eq):
    # ��������� ������: x = x_eq, y = y_eq, z = z_eq (��������������)
    # ����������� x � y �� ������ � ��������� ��������� � ���������, ���������� �� ������� ��� ��������� t
    t = sp.symbols('t')
    x = x_eq.subs(sp.symbols('t'), t)
    y = y_eq.subs(sp.symbols('t'), t)
    hyperbola_eq = x**2 / a**2 - y**2 / b**2 - 1
    solutions = sp.solve(hyperbola_eq, t)
    return len(solutions) > 0

# ��������� ������ (������)
x_eq = sp.sympify('1 + 2*t')
y_eq = sp.sympify('3 + t')
z_eq = sp.sympify('2 - t')
does_line_intersect = does_line_intersect_hyperbola(a, b, x_eq, y_eq, z_eq)
print(f"������ {'����������' if does_line_intersect else '�� ����������'} ���������.")
