"""
A program that accepts the lengths of three sides of a triangle as inputs.
 The program should output whether or not the triangle is a right triangle
  (Recall from the Pythagorean
   Theorem that in a right triangle, the square of one side equals the sum of
    the squares of the other two sides). Implement using functions.
"""


def is_right_triangle():
    side_1 = int(input("enter the length of side 1: "))
    side_2 = int(input("enter the length of side 2: "))
    side_3 = int(input("enter the length of side 3: "))
    sides=[side_1,side_2,side_3]
    sides.sort()
    return sides[2] **2==sides[0]**2+sides[1]**2
if is_right_triangle():
    print("the triangle is a right triangle.")
else:
    print("the triangle is not right triangle. ")
