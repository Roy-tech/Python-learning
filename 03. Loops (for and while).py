
# while loop execute statements as long as it is true.

i = 1

while i < 6:
    print(i)
    i += 1

# break statement can stop loop even if the condition is true.

while i < 10:
    print(i)
    if i == 4:
        break
    i += 1

# continue statement can stop the current iteration & go with the next.

i = 0
while i < 9:
    i += 1
    if i == 7:
        continue
    print(i)

# else statement print msg when condition is not true.

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print('i is no longer less than 10')

# For loop in general

name = "Roy"
for x in name:
    print(x, end=",")

# range will show 0 - 9 or 8 value

for x in range(0,10):
    print(x)
for x in range(0,10,2):
    print(x)

country = ["Bangladesh","India","China","Mayanmar"]
for i in country:
    print(i, end="-")
for x in range(1,len(country)):
    print(country[x])
for y in range(0,2):
    print(country[y])
else:
    print('No more country to show!')

num =[1,2,3]
country = ["Bangladesh","India","China","Mayanmar"]

for i in num:
    for x in country:
        print(i, x)
else:
    print('All combination is done!')
