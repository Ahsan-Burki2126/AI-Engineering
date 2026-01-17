import math

def calculate_perimeter_of_square(side):
    """
    This function calculates the perimeter of a square.
    """
    return 4 * side


def calculate_area_of_square(side):
    """
    This function calculates area of a square.
    """
    return side ** 2


def calculate_square_from_area(area):
    """
    Calculates side length of square from area.

    :param area: Area of the square
    """
    side = math.sqrt(area)
    return side
