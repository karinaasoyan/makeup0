import math


def calc_rectangle(a, b):
    rectangle_area = a * b
    return rectangle_area


def calc_triangle1(a, b, c):
    p_half = (a + b + c)/2
    triangle_area = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
    return triangle_area


def calc_triangle2(a, b, alpha):
    triangle_area2 = (a * b * (math.sin(alpha * math.pi/180))/2)
    return triangle_area2


def calc_circle(r):
    circle_area = math.pi * r ** 2
    return circle_area


def action_number():
    num = float(raw_input("""
Please choose an option
    1. Rectangle area (a, b)
    2. Triangle area 1 (a, b, c)
    3. Triangle area 2 (a, b, alpha)
    4. Circle area (r)
    5. Quit
"""))
    if num == 1:
        a = float(raw_input("Please enter side (a): "))
        b = float(raw_input("Please enter side (b): "))
        print calc_rectangle(a, b)
        action_number()
    elif num == 2:
        a = float(raw_input("Please enter side (a):  "))
        b = float(raw_input("Please enter side (b):  "))
        c = float(raw_input("Please enter side (c):  "))
        print calc_triangle1(a, b, c)
        action_number()
    elif num == 3:
        a = float(raw_input("Please enter side (a):  "))
        b = float(raw_input("Please enter side (b):  "))
        alpha = float(raw_input("Please enter angle (alpha):  "))
        print calc_triangle2(a, b, alpha)
        action_number()
    elif num == 4:
        r = float(raw_input("Give the radius (r): "))
        print calc_circle(r)
        action_number()
    elif num == 5:
        print("Bye!")

    else:
        print("Wrong input, please try again.")
        action_number()


action_number()