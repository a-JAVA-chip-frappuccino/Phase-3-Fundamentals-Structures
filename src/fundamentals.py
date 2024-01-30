'''
    VARIABLES AND DATA TYPES
'''

'''
    string concatenation: "string1" + "string2"
    f-string interpolation: f"{string1}{string2}"
'''

name = "Lantz" # string
favorite_color = 'purple'
age = 25 # integer

print("I am " + str(age) + " years old.") # typecasting
print(f"I am {age} years old.")

'''
    CONDITIONAL STATEMENTS
'''

if name == 'Eleanor' or name == "Lantz":
    print("You are teaching the lecture!")

if favorite_color == 'green':
    print("Your favorite color is green!")
else:
    print("Your favorite color is not green!")

if age < 0:
    print("Negative ages don't exist!")
elif age > -1 and age < 31:
    print("You are a child!")
else:
    print("You are an adult!")

'''
    LOOPS AND SEQUENCES
'''

for i in range(10):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)

for letter in name:
    print(letter)

counter = 0

while counter < age:
    print(counter)
    counter = counter + 1 # counter += 1

# infinite loop: AVOID!
# while True:
#     print("help")

'''
    FUNCTIONS
'''

def say_hello():
    print("Hello!")

say_hello()

def say_hello_to_someone(name = "Jay"):
    print("Hello there, " + name + "!")

say_hello_to_someone("Isaiah")

def say_color_and_food(fav_color, fav_food):
    print(f"Your favorite food is {fav_food} and your favorite color is {fav_color}!")

say_color_and_food("red", "pancakes")

def get_book():
    return "The Great Gatsby"

worst_book = get_book()

print(worst_book)