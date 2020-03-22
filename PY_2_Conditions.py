#IF statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#find prime number
a=[2,3,4,5,6,7]
# p=max(a)

for i in range(1,len(a)):
    count=0
    print(f"The number selected is {a[i]}")
    for j in range(1,a[i]):
        if a[i]%j==0:
            count=count+1
    if count<2:
        print(f" and is  prime")
    else:
        print(f" and is  not prime")

# checking the value
print(2 in a)

banned_users = ['andrew', 'carolina', 'david']
user='tax'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


age = 19
if age>=18:
    print("Adult")

# if-else Statements
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#List and If-else
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# ***********************************
# **********Dictionaries*************
# ***********************************
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'x_position': 3, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
fav_laguage={'Rohan':'C',
             'Radha':'Py',
             'Ankur':'Matlab',
             'Sam':'SAS',
    }
print(fav_laguage['Sam'].lower())

#Error handling--> invalid KEY
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through a Dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for language in favorite_languages.values():
    print(language.title())
for language in favorite_languages.keys():
    print(language.title())

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# a LIST OF Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# Make a empty list
alien=[]
# make 30 green aliens
for alien_num in range(30):
    new_alien={'color':'green', 'points':5,'speed':'slow'}
    alien.append(new_alien)
#show the first 5 aliens
for alie in alien[:5]:
    print(alie)
print("...")
print(f"Total number of aliens: {len(alien)}")

for alie in alien[0:3]:
    if alie['color'] == 'green':
        alie['color'] = 'yellow'
        alie['speed'] = 'medium'
        alie['points'] = 10
    elif alie['color'] == 'yellow':
        alie['color'] = 'red'
        alie['speed'] = 'fast'
        alie['points'] = 15
for alie in alien[0:3]:
    print(alie)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Financial Example
credit_1={'name':'nitesh','credit':820}
credit_2={'name':'rakesh','credit':720}
credit_3={'name':'playo','credit':620}
credit_hist=[credit_1,credit_2,credit_3]
for score in credit_hist:
    print(score)

# A Dictionary in a Dictionary
users ={
    'arun':{
        'first':'alex',
        'last':'pagal',
        'location':'palampur'
    },
    'archna':{
        'first':'archie',
        'last':'talli',
        'location':'Patna'
    }
}
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\t Full name : {full_name.title()}")
    print(f"\t Location : {location.title()}")
    