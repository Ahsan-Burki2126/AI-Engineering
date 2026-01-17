import math 

def calculate_circumference(radius):
    """
    This fuction takes radius of the circle and calculates its circumference.
    """
    return 2 * math.pi * radius

def calculate_area_of_circle(radius):
    """
    This function calculates area of circlre
    """
    return math.pi * radius ** 2

def calculate_diameter_of_circle(radius):
    """
    This function calculates diameter of a circle 
    
    :param radius: radius of the circle
    """
    return radius * 2

def calculate_circle(area):
    """
    Docstring for calculate_circle
    
    :param area: Area of the circle
    """
    radius = math.sqrt(area/math.pi)
    return radius
