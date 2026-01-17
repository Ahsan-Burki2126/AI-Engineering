def calculate_perimeter_of_rectangle(length, width):
    """
    This function calculates the perimeter of a rectangle.
    """
    return 2 * (length + width)


def calculate_area_of_rectangle(length, width):
    """
    This function calculates area of a rectangle.
    """
    return length * width


def calculate_rectangle_from_area(area, width):
    """
    Calculates length of rectangle from area and width.

    :param area: Area of the rectangle
    :param width: Width of the rectangle
    """
    length = area / width
    return length
