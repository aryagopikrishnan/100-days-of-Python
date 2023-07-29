# Functions with outputs
# Number of days in a month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


#----------------------------------------------------------------------

# Calculator

# Create a function for each operation

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2


def multiply(n1,n2):
  return n1 * n2


def divide(n1,n2):
  return n1 / n2

# Creating a dictionary to save the operations

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
for symbol in operations:
  print(symbol)

operation_chosen = input("Pick an operation to perform: ")

if operation_chosen == "+":
  answer = add(num1,num2)
elif operation_chosen == "-":
  answer = subtract(num1,num2)
elif operation_chosen == "*":
  answer = multiply(num1,num2)
else:
  answer = divide(num1,num2)

print(f"{num1} {operation_chosen} {num2} = {answer}")

#--------------------------------------------------------------------

# Recursion:

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2


def multiply(n1,n2):
  return n1 * n2


def divide(n1,n2):
  return n1 / n2

# Creating a dictionary to save the operations

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = int(input("What is the first number?: "))
  num2 = int(input("What is the second number?: "))
  for symbol in operations:
    print(symbol)
    should_countinue = True
  while should_countinue:
      
    operation_chosen = input("Pick an operation to perform: ")

    if operation_chosen == "+":
        answer = add(num1,num2)
    elif operation_chosen == "-":
        answer = subtract(num1,num2)
    elif operation_chosen == "*":
        answer = multiply(num1,num2)
    else:
        answer = divide(num1,num2)

    print(f"{num1} {operation_chosen} {num2} = {answer}")

    if input(f"Type y to continue with the same number and n to start new: ") == "y":
      num1 = answer
    else:
      should_countinue = False
      calculator()
  


