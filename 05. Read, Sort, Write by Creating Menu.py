# The open() function takes two parameters; filename, and mode.
# four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# First we will create menu to make this exercise fun

import sys  # this allows you to use the sys.exit command to quit/logout of the application


def main():
    login()


def login():
    username = "tutor"
    password = "tutorpass"
    print("Enter username : ")
    answer1 = input()
    print("Enter password : ")
    answer2 = input()
    if answer1 == username and answer2 == password:
        print("Welcome - Access Granted")
        menu1()
    else:
        print("Please try again! or Contact Roy to get your access info.")
        login()


def menu1():
    print("************MAIN MENU**************")
    print()

    choice1 = input("""   Please choose an option.
                          A: You want to open the people's info file
                          Q: Quit/Log Out
                          Please enter your choice: """)
    if choice1 == "A" or choice1 == "a":
        print("File is ready!")

        choice2 = input(""" Now please choose from the following options
                                      B: You want to sort data
                                      Q: Quit/Log Out
                                      Please enter your choice: """)
        if choice2 == "B" or choice2 == "b":
            choice3 = input(""" Great! How do you want to sort the data?
                                                  I: By ID
                                                  F: By First Name
                                                  L: By Last Name
                                                  G: By Age
                                                  Q: Quit/Log Out
                                                  Please enter your choice: """)
            if choice3 == "I" or choice3 == "i":
                import csv
                import operator
                with open('/Roy/Python/Notepad.txt', 'r') as txt_file:
                    name = csv.reader(txt_file)
                    sort0 = sorted(name, key=operator.itemgetter(0))
                    for x in sort0:
                        print(x)
            elif choice3 == "F" or choice3 == "f":
                import csv
                import operator
                with open('/Roy/Python/Notepad.txt', 'r') as txt_file:
                    name = csv.reader(txt_file)
                    sort1 = sorted(name, key=operator.itemgetter(1))
                    for x in sort1:
                        print(x)
            elif choice3 == "L" or choice3 == "l":
                import csv
                import operator
                with open('/Roy/Python/Notepad.txt', 'r') as txt_file:
                    name = csv.reader(txt_file)
                    sort2 = sorted(name, key=operator.itemgetter(2))
                    for x in sort2:
                        print(x)
            elif choice3 == "G" or choice3 == "g":
                import csv
                import operator
                with open('/Roy/Python/Notepad.txt', 'r') as txt_file:
                    name = csv.reader(txt_file)
                    sort3 = sorted(name, key=operator.itemgetter(3))
                    for x in sort3:
                        print(x)
            elif choice3 == "Q" or choice3 == "q":
                sys.exit
            else:
                print("You must only select either I,F,L, or G.")
                print("Please try again")
                menu1()
        elif choice2 == "Q" or choice2 == "q":
            sys.exit
        else:
            print("You must only select either B or Q.")
            print("Please try again")
            menu1()
    elif choice1 == "Q" or choice1 == "q":
        sys.exit
    else:
        print("You must only select either A or Q.")
        print("Please try again")
        menu1()


main()

# Writing in text files

import csv
with open('/Roy/Python/Notepad.txt', 'a') as txt_file:
    name_write = csv.writer(txt_file)
    name_write.writerow(['720032', 'Ray', 'Lu', '45'])
    name_write.writerow(['720033', 'Remi', 'Dalton', '35'])
    name_write.writerow(['720034', 'Jackie', 'Sharp', '39'])
    name_write.writerow(['720035', 'Francis', 'Underwood', '54'])
    name_write.writerow(['720036', 'Doug', 'Stamper', '46'])
    name_write.writerow(['720037', 'Rony', 'James', '30'])
    name_write.writerow(['720038', 'Duke', 'Stamp', '46'])
    name_write.writerow(['720039', 'Claire', 'Underwood', '52'])
    name_write.writerow(['720040', 'Rachel', 'Lian', '46'])

# What's wrong with writing in this way? I am getting extra line space under each line