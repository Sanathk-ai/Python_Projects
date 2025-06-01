# bill_amount = float(input("What's the total amount? "))
# tip = float(input("How much percentage of tip would you like to give: 10, 12, 15, 20, 50, 100? "))
# members = float(input("How many members to split the bill with? "))
# bill_amount += bill_amount*(tip/100)
# total = (bill_amount)/members
# print(f"Each pay ${round(total, 2)}")

weight = float(input("What is your weight? "))
height = float(input("What is your height? "))

bmi = weight / (height ** 2)

if(bmi<18.5):
    print("Underweight")
elif(bmi>=18.5 and bmi<25):
    print("Normal weight")
else:
    print("Overweight")


import random

# rand_int = random.randint(0,1)
# if rand_int == 0:
#     print("Tails")
# else:
#     print("Heads")





