# Constants
HRA_P = 0.10
TA_P = 0.05
# Get basic pay from the user
basic_pay = float(input("Enter the basic pay: "))
# Calculate HRA and TA
hra = HRA_P * basic_pay
ta = TA_P * basic_pay
# Calculate total salary
salary = basic_pay + hra + ta
# Print the salary
print("The total salary is:", salary)