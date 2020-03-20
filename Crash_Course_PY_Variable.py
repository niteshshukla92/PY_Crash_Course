# Variable definition


# Changing Case in a String with Methods
name = "ada lovelace"
print(name)
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#Below statement doesn't resolve
full_name_1 = f"[first_name] (last_name)"
print(full_name)
print(full_name_1)
message=f"Hello, {first_name}"
print(message)

full_name2 = "{} {}".format(first_name, first_name)
print(full_name2)

# Adding Whitespace to Strings with Tabs or Newlines
print("Languages:\nPython\nC\nJavaScript\tTAB")

# Stripping Whitespace
favorite_language = ' python '
a=favorite_language.rstrip()
b=favorite_language.lstrip()
c=favorite_language.strip()
print(a)
print(b)
print(c)
print(favorite_language)


# Numbers

print(3*2)
print(3**2)
print((3+2)*4)

#Using integer and Float gives float
#Division always gives FLoat
print(6/3)

# Underscores in Numbers
# long numbers, group digits using underscores to make large numbers more readable:
universe_age = 14_000_000_000
print(universe_age)

# Multiple Assignment
x,y,z=1,2,3

# ALL CAPITAL TO DEFINE CONSTANTS
MAX=100
MAX=MAX+1
print(MAX)
x=x+1
print(x)

# ************************************
# ***************LIST*****************
# ************************************

# Index position starts at 0 not 1
bicyles= ['trek','cannondale','redline']
print(bicyles)
print(bicyles[1])
print(bicyles[1].title())

# writing the string using List
print(f"My first bicycle was a {bicyles[0].title()}")
bicyles[0]="Hercules"
print(bicyles)
bicyles.append('Hero')
print(bicyles)

#New list.. Dynamic list
motorcycles =[]
motorcycles.append('TVS')
motorcycles.append('Hero')
motorcycles.append('Suzuki')
print(motorcycles)
motorcycles.insert(-1,'Yamaha')
print(motorcycles)

#Inset and append. Insertion is not possible after last... That is technically append
#Removing elements from List
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
motorcycles.remove('honda')
print(motorcycles)

# remove() method deletes only the first occurrence of the value
# value appears more than once in the list, you’ll need to use a loop

# Organizing a list
# Sorting permanently
cars=['bmw','audi','toyota','tata','mahindra']
cars.sort()
print(cars)
# below statement doesn't work
a=cars.sort(reverse=True)
print(cars)
print(a)

#temp sort
cars=['bmw','audi','AUDI','toyota','TATA','tata','mahindra']
print(sorted(cars))
print(cars)

#printing in reverse order
cars.reverse()
print(cars)
#above statement not working correctly- It should have reversed the order.

#Finding Length
cars=['bmw','audi','AUDI','toyota','TATA','tata','mahindra']
print(len(cars))
print(cars[1])

# Chapter 4:Working with LIST

# Loops
cars=['bmw','audi','AUDI','toyota','TATA','tata','mahindra']
for car in cars:
    print(f"hi, I want to by {car}")

# Avoid indentation error
# Numerical values Loop
for number in range (1,6):
    print(number)
#Storing value in list
numbers=list(range(1,6))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# page 58
# generate even numbers
for num in range(2,17,2):
    print(num)
sqr=[]
sqr2=[]
# even=range(2,17,2)
# print(even)
for i in range(2,12,2):
    sqr2.append(i**2)
    sq=i**2
    sqr.append(sq)
print(sqr)
print(sqr2)
# above code is not differentiating.. Output might be different in PyCharm vs Jupyter

# Simple stats
digits=[]
for i in range(0,10):
    digits.append(i)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

#Creating prime numbers ----> to be completed
# for i in range(1,101):
#     for j in range (1,101):
#         sum(j%i==0)>2
#     print(i)

# Working with Part of a List
# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
for player in players[:3]:
    print(player.title())
# points to the same location
fav_players=players
players.append("Sachin")
print(players)
print(fav_players)

# Tuples --> Immutable
dimensions = (200, 50)
print(dimensions[0])
my_t = (3,)
# You can't modify tuples, however you can reassign the tuples with new values
dimensions=(100,20,23)
print(dimensions[2])