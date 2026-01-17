import math

def calculate_perimeter_of_triangle(a, b, c):
    """
    This function calculates the perimeter of a triangle.
    """
    return a + b + c


def calculate_area_of_triangle(base, height):
    """
    This function calculates area of a triangle.
    """
    return 0.5 * base * height


def calculate_triangle_from_area(area, height):
    """
    Calculates base of triangle from area and height.

    :param area: Area of the triangle
    :param height: Height of the triangle
    """
    base = (2 * area) / height
    return base
