#Code 1: 
two_digit_number = input("Type a two digit number: ")


dig1 = int(two_digit_number[0])
dig2 = int(two_digit_number[1])

#print(type(dig1))

dig_sum = dig1+dig2
print(str(dig1)+ " + "+str(dig2)+" = "+str(dig_sum))
print(dig_sum)

#----------------------------------------------------------------

#Code 2:

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#print(type(height))

bmi = float(weight)/(float(height)**2)
print(int(bmi))

#---------------------------------------------------------------

#Code 3:

age = input("What is your current age? ")

years_remaining = 90 - int(age)


days = 365*years_remaining
weeks = 52*years_remaining
months = 12*years_remaining


print(f"You have {days} days, {weeks} weeks, and {months} months left.")



#Day 2 Project - Tip Calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))

tip_percentage = int(input("What percentage tip would you like to give? "))
num_people = int(input("How many people to split the bill? "))


tip = (tip_percentage/100) * total_bill
total_amount = tip + total_bill
bill_per_person = total_amount/num_people
bill_per_person = round(bill_per_person,2)

print(f"Each person should pay: ${bill_per_person}")
