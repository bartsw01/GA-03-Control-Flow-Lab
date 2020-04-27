# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print("Enter the lengths of three sides of a triangle: ")
t_side_1 = input("Side 1: ")
t_side_2 = input("Side 2: ")
t_side_3 = input("Side 3: ")

if t_side_1 == t_side_2 == t_side_3:
  print(f"A triangle with sides of {t_side_1}, {t_side_2}, and {t_side_3} is an equilateral triangle.")
elif  t_side_1 != t_side_2 and t_side_1 != t_side_3 and t_side_3 != t_side_2:
  print(f"A triangle with sides of {t_side_1}, {t_side_2}, and {t_side_3} is a scalene triangle.")
else:  
  print(f"A triangle with sides of {t_side_1}, {t_side_2}, and {t_side_3} is an isosceles triangle.")