# Code 1: Average of student heights

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_count = n+1
sum_heights = 0
x= 0
for x in range(0,n+1):
    sum_heights = sum_heights + student_heights[x]
    x=x+1
    
    
average = sum_heights/total_count
print(round(average))

#----------------------------------------------------------------------

# Code 2: High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high = 0
for x in range(0,n+1):
    if student_scores[x] >= high:
        high = student_scores[x]
        x=x+1
print(high)
        
#----------------------------------------------------------------------

# Code 3: Even numbers sum using range

even_sum = 0
for numbers in range(2,101,2):
    even_sum = even_sum+numbers
print(even_sum)

#----------------------------------------------------------------------

# Code 4: FizzBuzz

for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)

#--------------------------------------------------------------------

# Code 5: Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for char in range(1,nr_letters+1):
  random_char = random.choice(letters)
  password = password + random_char
  print(password)
for symbol in range(1,nr_symbols+1):
  random_symbol = random.choice(symbols)
  password = password + random_symbol
  print(password)
for num in range(1,nr_numbers+1):
  random_num = random.choice(numbers)
  password = password + random_num
  print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for char in range(1,nr_letters+1):
  random_char = random.choice(letters)
  password.append(random_char)
  # print(password)
for symbol in range(1,nr_symbols+1):
  random_symbol = random.choice(symbols)
  password.append(random_symbol)
  # print(password)
for num in range(1,nr_numbers+1):
  random_number = random.choice(numbers)
  password.append(random_number)
  # print(password)

#causes repetition
# final_password = ""
# for digit in range(1,len(password)+1):
#   random_digit = random.choice(password)
#   final_password = final_password + random_digit 
#   print(final_password)

final_password = ""
random.shuffle(password)
# print(password)
for digit in range(0,len(password)):
  final_password = final_password + password[digit]
print(final_password)