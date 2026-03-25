# This is a demo script to test the functionality of the demo_module.
import demo_module
demo_module.greet("Yuvraj")
result = demo_module.add(5, 3)
print(f"The result of addition is: {result}")

# Now let's test some functions from the math module.
import math

print(f"The addition of 5 and 3 is: {math.fsum([5, 3])}")

print(f"The square root of 16 is: {math.sqrt(16)}")

print(f"the factorial of 5 is: {math.factorial(5)}")

# find distance of line between points (2, 3) and (5, 6)(use math module)
distance = math.dist((2, 3), (5, 6))
print(f"The distance of the line is: {distance}")

# find Area of circle with radius 5 (use math module)
radius = 5
area = math.pi * radius ** 2
print(f"The area of the circle is: {area}")

# find EMI for a loan per month with principal amount of 5,000,000, interest rate of 10% and loan tenure of 12 months (use math module)
P = 5000000  # Principal amount
R = 0.10 / 12  # monthly interest rate in percentage
N = 12  # Loan tenure in months
EMI = (P * R * math.pow(1 + R, N)) / (math.pow(1 + R, N) - 1)
print(f"The EMI for the loan is: {EMI}")

#date and time module
from datetime import datetime, date

# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Get the current date
today = date.today()
print(f"Current date: {today}")

# Format the current date and time in a specific format
strftime = now.strftime(" %d-%m-%Y %H:%M:%S ")
print(f"Formatted date and time: {strftime}")

#Calculate Age from date of birth(user input)
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print(f"Your age is: {age}")





