# Lab 6: This program determines the type of triangle based on the lengths of its sides.

# Input: lengths of the three sides of the triangle
first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))

# Determine the type of triangle using conditional statement combined with logical operators
if (first_side == second_side) and (second_side == third_side) and (first_side == third_side):
    print("The triangle is Equilateral.")
elif (first_side == second_side) or (second_side == third_side) or (first_side == third_side):
    print("The triangle is Isosceles.")
elif (first_side != second_side) and (second_side != third_side) and (first_side != third_side):
    print("The triangle is Scalene.")
else:
    print("Invalid input.")