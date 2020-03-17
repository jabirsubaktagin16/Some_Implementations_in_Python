from typing import Union
from math import  pi,pow

def cube(side_length: Union[int,float]) -> float:
    return pow(side_length,3)

def cuboid(width: float, height: float, length: float) -> float:
    return float(width*height*length)

def cone(area_of_base: float, height: float) -> float:
    return (area_of_base*height)/3.0

def right_circ_cone(radius: float, height: float) -> float:
    return pi * pow(radius, 2) * height/3.0

def prism(area_of_base: float, height: float) -> float:
    return float(area_of_base*height)

def pyramid(area_of_base: float, height: float) -> float:
    return area_of_base*height/3.0

def sphere(radius: float) -> float:
    return 4/3 * pi * pow(radius, 3)

def circular_cylinder(radius: float, height: float) -> float:
    return pi * pow(radius, 2) * height

if __name__ == '__main__':
    print("Volumes: ")
    print("Cube: "+str(cube(2)))
    print("Cuboid: "+str(cuboid(2, 2, 2)))
    print("Cone: "+str(cone(2, 2)))
    print("Right Circular Cone: "+str(right_circ_cone(2, 2)))
    print("Prism: "+str(prism(2, 2)))
    print("Pyramid: "+str(pyramid(2, 2)))
    print("Sphere: "+str(sphere(2)))
    print("Circular Cylinder: "+str(circular_cylinder(2, 2)))