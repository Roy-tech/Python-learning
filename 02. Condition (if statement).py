# If it the temp is > 30, it's a hot day. Drink plenty of water.
# Otherwise if the temp is < 20, it's a cold day. Wear warm clothes.
# Otherwise it's a lovely day. Always end with Enjoy your day.

temp = int(input(" Write today's temperature celsius: "))
if temp > 30:
    print('It is a hot day!')
    print('Drink plenty of water.')
elif temp < 20:
    print('It is a cold day!')
    print('Wear warm clothes.')
else:
    print('It is a lovely day!')
print('Hope you are looking forward to this day!')


# If an applicant has high income along with good credit and deposit,
# then they are eligible for opening a stock trading account.
# Once you do, You need to put down >= $5000 deposit to start. End with Happy Trading!
monthly_income_standard = 4500
credit_rating = .80  # 0 being no credit to 1 being highest credit rating
deposit = 5000

inc = int(input('How much is your income per month?: '))
credit = float(input('What is your credit rating in decimal?: '))


if inc >= monthly_income_standard and credit >= credit_rating:
    print('Congratulations! You are eligible to open a trading account.')
    print('Please get ready to deposit money.')
    dep = int(input("How much do you want to deposit?: "))
    if dep >= deposit:
       print('Great choice to plant a tree now!')
       print('Happy Trading!')
    else:
       print('Please deposit minimum $5000.')
       print('We want you to devote more to secure your future!')
else:
    print("I am sorry! You are not eligible for this account.")
print('Enjoy your day!')

# Price of a house is $1m. If buyer has good credit,
# they need to put down 10%, otherwise 20%. Print downpayment

house_price = 1000000
rating = bool(input('''I believe I have good credit rating.
Please answer this with True or False: '''))

if rating == True:
    down_payment1 = (.10*house_price)
    print(f'Your down payment will be ${down_payment1}') # using formatted text
else:
    down_payment2 = (.20*house_price)
    print(f'Your down payment will be ${down_payment2}') # using formatted text
print('Congratulations! Wish you get a fantastic house!')
# What to do as I get same answers for both?
# How can I convert yes no answer to boolean?
