# Lab 1

# 1.1 Part A

f_string = input("Enter the temperature in Fahrenheit: ")
f = float(f_string)

celsius = (f - 32) / 1.8

print("The temperature in Celsius: ", celsius)

# 1.2 Part B

h_string = input("Enter the height of the trapezoid: ")
h = float(h_string)

lb_string = input("Enter the length of the bottom base: ")
lb = float(lb_string)

lt_string = input("Enter the length of the top base: ")
lt = float(lt_string)

print("The area is: ", 1/2 * (lb + lt) * h)

# 1.3 Part C

pi = 3.14

r_string = input("Enter the radius of the cone: ")
r = float(r_string)

h_string = input("Enter the height of the cone: ")
h = float(h_string)

print("The volume is: ", (pi * (r ** 2) * h) / 3)
