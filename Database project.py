#Jonathan Nguyen
#Juan Sanchez
#Jithin Mathew
#CSCE 4350.070
#December 3, 2020


#Greetings Dialogue
print("Welcome to our program!!")

#Choosing an option
x = input("Please enter a number: 1(Employee), 2(Department), or 3(Payroll) ")
a = int(x)

#If Employee
if a == 1:
    print("\nYou chose Employee.\n")

    # Choosing an operation
    y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
    b = int(y)

    # If Insert
    if b == 1:
        print("\nYou chose Insert.\n")

    # If Delete
    elif b == 2:
        print("\nYou chose Delete.\n")

    # If Update
    elif b == 3:
        print("\nYou chose Update.\n")


#If Department
elif a == 2:
    print("\nYou chose Department.\n")

    #Choosing an operation
    y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
    b = int(y)

    #If Insert
    if b == 1:
        print("\nYou chose Insert.\n")

    #If Delete
    elif b == 2:
        print("\nYou chose Delete.\n")

    #If Update
    elif b == 3:
        print("\nYou chose Update.\n")

#If Payroll
elif a == 3:
    print("\nYou chose Payroll.\n")

    # Choosing an operation
    y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
    b = int(y)

    # If Insert
    if b == 1:
        print("\nYou chose Insert.\n")

    # If Delete
    elif b == 2:
        print("\nYou chose Delete.\n")

    # If Update
    elif b == 3:
        print("\nYou chose Update.\n")



