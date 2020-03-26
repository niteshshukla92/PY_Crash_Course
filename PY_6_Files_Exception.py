# Files and Exceptions
# Reading from a File
# Reading an Entire File
with open('C:/Users/niteshshukla/.PyCharmCE2019.3/config/scratches/pi_digits.txt') as file_object:
    contents=file_object.read()
    print(contents.rstrip())
# print(contents)
filename='C:/Users/niteshshukla/.PyCharmCE2019.3/config/scratches/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


filename='C:/Users/niteshshukla/.PyCharmCE2019.3/config/scratches/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string=''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(f"{pi_string[:52]}...")
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# read mode('r'), write mode('w'), append mode('a'), or a read and write ('r+')
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# *******************Exceptions*******************
try:
    print(9/0)
except ZeroDivisionError:
    print("You can't divide by zero")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number=input("\n First number: ")
    if first_number=='q':
        break
    second_number=input("\n Second number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)


# Handling the FileNotFoundError Exception

filename='C:/Users/niteshshukla/.PyCharmCE2019.3/config/scratches/pi_digits.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words=contents.split()
    num_words=len(words)
    print(f"the line pi_digits has about {num_words} words.")

# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
# count_words(filename)

# Storing Data
# using json.dump() and json.load()

import json
numbers = [2,3,4,5,6,7]
filename='C:/Users/niteshshukla/.PyCharmCE2019.3/config/scratches/numbers.json'
with open (filename,'w') as f:
    json.dump(numbers,f)
with open(filename,'r') as f:
    numbers=json.load(f)
print(numbers)

# creating user database
# import json
username=input("What is your last name?")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you {username}")

# Refactoring
# load username stored previously
def greet_user():
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("what is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"we'll remember you, {username}")
else:
    print(f"Welcome back, {username}")

greet_user()



# ********************************************
# Testing Your Code
# ********************************************
def get_formatte_name(first,last):
    full_name=f"{first} {last}"
    return full_name.title()

import unittest

class NamesTestCase(unittest.TestCase):
    """Tests """
    def test_first_last_name(self):
        """"""
        formatted_name=get_formatte_name('john','hoppkins')
        self.assertEqual(formatted_name,'John Hoppkins')
if __name__=='__main__':
    unittest.main()
