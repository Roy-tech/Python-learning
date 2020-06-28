# Function name with parenthesis to call it.

def my_function():
    print('Hi everyone! It is my function.')
my_function()

def name_function(fname, lname):
    print(f'Hello {fname} {lname}! Welcome to the function world.')
name_function('Suvra','Roy')

# using default parameter without given parameter.

def country_function(country = 'Bangladesh'):
    print(f'I am from {country} and love my {country} very much!')
country_function()
country_function('India')

# using any type of parameter into function

def list_function(food):
    for i in food:
        print(i)

dishes = ['Butter Panir','Soyabin Curry','Chickpeas Curry', 'Afghani Kebab']

list_function(dishes)

# If we are not sure about the number of arguments getting into the parameter, use *.

def dish_function(*food):
    print('I love all of these', food[:])

dish_function('Chicken','Lamb','Dal','Goat','Panir')
dish_function('Chinese food')

# how can I remove , and parenthesis from above code result

def printinfo(*varTuple):
    if(len(varTuple) > 1):
        print('I love all of these', varTuple)
    else:
        somString = ''.join(varTuple)
        print('I love all of these', somString[:])

printinfo('Chinese')
printinfo('Chicken','Lamb','Dal')

# Return statement is used to return a value

def func_calculation(x):
    return (1.05*x)**2

print(func_calculation(3))

def dish_function(*food):
    output = f'I love all of these {food[:]}'
    return output

print(dish_function('Chicken','Lamb','Dal','Goat','Panir'))
print(dish_function('Chinese food'))

# using numbers in calculation function

def sum(input1,input2):
    return input1 + input2

# if you use return, you state 'print' to execute function

print(sum(1,2)) # or

def sum(input1,input2):
    print(input1 + input2)

sum(1,2)

# using lambda as function

return_calculation = lambda x: (1.05*x)**2
print(return_calculation(100))

# Using lamda for multiple inputs (lambda cannot be used for muliple lines functions)

fullname = lambda fn, ln: fn.strip().title() + " " + ln.strip().title() # strip() to remove space from both sides & title() to keep first letter of a word always capital
print(fullname(' Suvra', 'roy'))

# Sorting list by last name

full_names = ["Athar Imtiaz", "Suvra Roy", "Robert Kyosaki", "Rylie Baxter", "Collum Thames"]
full_names.sort(key=lambda names: names.split(" ")[1].lower()) # splitting name and choosing last name and converting last name to lower section in case anybody types wrongly
print(full_names)

