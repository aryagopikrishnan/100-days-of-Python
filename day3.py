# Code 1: Odd or Even

number = int(input("Which number do you want to check? "))

if number % 2 ==0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#--------------------------------------------------------------------------

# Code 2:  BMI 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = int(weight/(height**2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


#-------------------------------------------------------------------------

#Code 3: Leap Year

year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


#-------------------------------------------------------------------

#Code 4: Pizza Delivery Code

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

#print(type(size))

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
else:
    print(f"Your final bill is: ${bill}")

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3
if extra_cheese == "Y":
    bill = bill + 1

print(f"Your final bill is: ${bill}")

#-----------------------------------------------------------------

# Code 5: Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
t_count = 0
r_count = 0
u_count = 0
e_count = 0
l_count = 0
o_count = 0
v_count = 0
love = 0
true = 0


combined_name = name1+name2

#print(combined_name)

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")

true = t_count+r_count+u_count+e_count

l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")
e_count = combined_name.count("e")

love = l_count+ o_count+v_count+e_count

score = int(str(true)+str(love))

if (score <10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >=40) and (score<= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


#------------------------------------------------------------------------------------

