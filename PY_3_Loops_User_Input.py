# User Input and while Loops
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# For entering numerical
age=input("Age")
print(age*2)
# if changed to integer
age1=int(age)
print(age1*2)

# Modulo operator
print(4%3)
# Check if even
in_num=input("Enter number to be checked")
if int(in_num)%2==0:
    print(f"{in_num} is Even")
else:
    print(f"{in_num} is ODD")

# Introducing while Loops
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

# USE code with Break and Continue
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message=''
# while message!='quit':
#     message=input(prompt)
#         print(message)
while True:
    city=input(prompt)

    if city=='quit':
        break
    else:
        print(f"go to {city.title()}")

current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number)

# Using a while Loop with Lists and Dictionaries
# Moving items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user=unconfirmed_users.pop()

    print(f"Verifying user :{current_user.title()}")
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
# Filling a Dictionary with User Input

responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name?")
    response=input("Which pub would you like to go")
    responses[name]=response
    repeat=input('Would you like to let other person respond? (yes/no)')
    if repeat=='no':
        polling_active = False
    else:
        continue
    #polling is complete. Show results.
    print("\n ----- Poll Results----")
    for name,response in responses.items():
        print(f"{name} would like to go to pub {response}")