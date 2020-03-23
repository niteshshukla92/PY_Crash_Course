# Functions
def greet_user():
    name=input("Enter the name")
    """Display a simple greeting."""
    print(f"Hello! {name}")
greet_user()

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

# Equivalent Function Calls
def get_formatted_name(first_name, last_name):
    """Return a full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name"""
    if middle_name:
        full_name= f"{first_name} {middle_name} {last_name}"
    else:
        full_name= f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'hooker','play')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#passing a list to function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Passing an Arbitrary Number of Arguments
def make_pizza (*toppings):
    """Print the list of toppings that have been requested."""
    # print(toppings)
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('pepperoni','extra cheese')

# Mixing Positional and Arbitrary Arguments
def pizza_prep(size,*toppings):
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
pizza_prep(8,'extra cheese','no mushroom')

# generic parameter name *args is often used which collects arbitrary positional arguments.
# generic parameter name **kwargs is often used which collects non-specific keyword arguments.
# Using Arbitrary Keyword Arguments
# won’t know ahead what kind of information will be passed --> write functions that accept as many key-value pairs

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we know about a suer."""
    user_info['first name']=first
    user_info['last name']=last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# Storing Your Functions in Modules
# Importing an Entire Module



# Ways of assigning a function
# import module_name
# from module_name import function_0, function_1, function_2
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# Styling function
# function_name(value_0, parameter_1='value')
import sample_module
sample_module.make_my_pizza(16,'pepperoni')