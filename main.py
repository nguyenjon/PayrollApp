#Jonathan Nguyen
#Juan Sanchez
#Jithin Mathew
#CSCE 4350.070
#December 3, 2020

from database.db_manager import DatabaseManager



#Greetings Dialogue
print("Welcome to our program!!")

db = DatabaseManager()

#Choosing an option
x = input("Please enter a number: 1(Employee), 2(Department), or 3(Payroll) 4(Quit)")
choice = int(x)

while(choice is not 4) :
    #If Employee
    if choice == 1:
        print("\nYou chose Employee.\n")

        # Choosing an operation
        y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
        choice = int(y)

        # If Insert
        if choice == 1:
            print("\nYou chose Insert.\n")

        # If Delete
        elif choice == 2:
            print("\nYou chose Delete.\n")

        # If Update
        elif choice == 3:
            print("\nYou chose Update.\n")


    #If Department
    elif choice == 2:
        print("\nYou chose Department.\n")

        #Choosing an operation
        y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
        choice = int(y)

        #If Insert
        if choice == 1:
            print("\nYou chose Insert.\n")

        #If Delete
        elif choice == 2:
            print("\nYou chose Delete.\n")

        #If Update
        elif choice == 3:
            print("\nYou chose Update.\n")

    #If Payroll
    elif choice == 3:
        print("\nYou chose Payroll.\n")

        # Choosing an operation
        y = input("Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ")
        choice = int(y)

        # If Insert
        if choice == 1:
            print("\nYou chose Insert.\n")

        # If Delete
        elif choice == 2:
            print("\nYou chose Delete.\n")

        # If Update
        elif choice == 3:
            print("\nYou chose Update.\n")

    x = input("Please enter a number: 1(Employee), 2(Department), or 3(Payroll) 4(Quit)")
    choice = int(x)



