#Jonathan Nguyen
#Juan Sanchez
#Jithin Mathew
#CSCE 4350.070
#December 3, 2020

from database.db_manager import DatabaseManager

#--------------------- Department operations-------------------------------------------------

def add_department():
    
    #"INSERT INTO Department(Dept_ID) VALUES (" + i +")";
    pass

def edit_department():
    pass

def delete_department():
    pass

#--------------------- Employee operations-------------------------------------------------

def add_employee():
    pass

def edit_employee():
    pass

def delete_employee():
    pass


#--------------------- Payroll operations-------------------------------------------------

# def add_payroll():
#     x = input('Please enter a pay type: 1(hourly), 2(salary)')
#     choice = int(x)


#     x = input('Please enter the employee\'s ID: ')
#     choice = int(x)


#     db.add_payroll(pay_type, pay, emp_ID)

# def edit_payroll():

#     db.edit_payroll(pay_type, pay, emp_ID)

# def delete_payroll():

#     db.delete_payroll(emp_ID)


def main():
    #Greetings Dialogue
    print('Welcome to our program!!')

    db = DatabaseManager()

    #Choosing an option
    x = input('Please enter a number: 1(Employee), 2(Department), 3(Payroll), 4(Quit)')
    choice = int(x)

    while(choice not in [1, 2, 3]) :
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
            print('\nYou chose Department.\n')

            #Choosing an operation
            y = input('Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ')
            choice = int(y)

            #If Insert
            if choice == 1:
                print('\nYou chose Insert.\n')

            #If Delete
            elif choice == 2:
                print('\nYou chose Delete.\n')

            #If Update
            elif choice == 3:
                print('\nYou chose Update.\n')

        #If Payroll
        elif choice == 3:
            print('\nYou chose Payroll.\n')

            # Choosing an operation
            y = input('Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update) ')
            choice = int(y)

            # If Insert
            if choice == 1:
                print('\nYou chose Insert.\n')
                add_payroll()

            # If Delete
            elif choice == 2:
                print('\nYou chose Delete.\n')
                edit_payroll()

            # If Update
            elif choice == 3:
                print('\nYou chose Update.\n')
                delete_payroll()

        else:
            print('\nEnding program.\n')
            exit()

        x = input('Please enter a number: 1(Employee), 2(Department), 3(Payroll), 4(Quit)')
        choice = int(x)

if __name__ == '__main__':
    main()

