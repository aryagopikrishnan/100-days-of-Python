# Day 8: Functions with inputs

def paint_calc(height,width,cover):
    num_of_cans = (height*width)/(cover)
    print(round(num_of_cans))


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#-------------------------------------------------------------------------

# Prime number check using function with input

def prime_checker(number):
    i=0
    for dividend in range(1,number+1):
        if number % dividend == 0:
            i+=1
    if i > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


#----------------------------------------------------------------------

# Caeser - cipher encription code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(t,s):
  cipher_text = ""
  for letter in t:
    position = alphabet.index(letter)
    new_position = position + s
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded test is {cipher_text}")
    
def decrypt(t,s):
  cipher_text = ""
  for letter in t:
    position = alphabet.index(letter)
    new_position = position - s
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The decoded test is {cipher_text}")

if direction == "encode":
  encrypt(t=text,s=shift)
else:
  decrypt(t=text,s=shift)

#-------------------------------------------------------------------------
# Caeser - cipher encription code with only one function

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text1,s,cipher_direction):
    text2 = ""
    if cipher_direction == "decode":
        s *= -1
    for letter in text1:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+s
            text2 += alphabet[new_position]
        else:
            text2 += letter
    print(f"The {cipher_direction}d text is {text2}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift%26
    caesar(text,shift,direction)
    result = input("Type yes to go again, otherwise type no: ").lower()
    if result == "no":
       should_continue = False
       print("Goodbye!")


      
   