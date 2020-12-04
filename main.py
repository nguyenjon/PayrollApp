#Jonathan Nguyen
#Juan Sanchez
#Jithin Mathew
#CSCE 4350.070
#December 3, 2020

import re

from database.db_manager import DatabaseManager

db = DatabaseManager()

#--------------------- Employee operations-------------------------------------------------

def add_employee():
    pass

def edit_employee():
    while True:
        emp_id = input("Enter the ID of the employee: ")
        if id.isnumeric():
            break
        else:
            print('Invalid ID')
    
    db.updateEmployee(emp_id)

def delete_employee():
    while True:
        emp_id = input("Enter the ID of the employee: ")
        if id.isnumeric():
            break
        else:
            print('Invalid ID')

    db.deleteEmployee(emp_id)


#--------------------- Payroll operations-------------------------------------------------

def add_payroll():
    while True:
        id = input("Enter the ID of the employee: ")
        if id.isnumeric():
            break
        else:
            print('Invalid ID')

    while True:
        pay_type = input("Enter the type of pay (Hourly, Salary): ")
        if pay_type in ['Hourly', 'Salary']:
            break
        else:
            print('Invalid Option')
    
    r = re.compile('[1-9][0-9]*.[0-9][0-9]') #format of decimal number with two decimal places
    while True:
        pay = input("Enter the pay of the employee: $")
        if r.match(pay):
            break
        else:
            print('Invalid Option')

    db.add_payroll(id, pay_type, pay, id)


def view_payroll():
    while True:
        emp_id = input("Enter the ID of the employee: ")
        if emp_id.isnumeric():
            break
        else:
            print('Invalid ID')
    db.view_payroll(emp_id)


def edit_payroll():
    while True:
        emp_id = input("Enter the ID of the employee: ")
        if id.isnumeric():
            break
        else:
            print('Invalid ID')
    
    print("1: Update pay type\n")
    print("2: Update pay\n")

    while True:    
        choice = input("")

        if choice is '1':
            while True:
                pay_type = input("Enter the new pay type (Hourly, Salary): ")
                if pay_type in ['Hourly', 'Salary']:
                    break
                else:
                    print('Invalid Option')

        elif choice is '2':
            r = re.compile('[1-9][0-9]*.[0-9][0-9]') #format of decimal number with two decimal places
            while True:
                pay = input("Enter the new pay of the employee: $")
                if r.match(pay):
                    break
                else:
                    print('Invalid Option')
        else:
            print('Invalid Option')
            continue

    db.edit_payroll(pay_type, pay, emp_id)


def delete_payroll():
    emp_id = input('Enter the id of the employee whose payroll is to be deleted: ')
    db.delete_payroll(emp_id)


def main():
    #Greetings Dialogue
    print('Welcome to our program!!')

    #Choosing an option
    while True: 
        x = input('Please enter a number: 1(Employee), 2(Payroll), any other number(Quit)')
        if x.isnumeric():
            break
        else:
            print('Not a valid option')
    choice = int(x)

    while(choice in [1, 2]) :
        
        #If Employee
        if choice == 1:
            print("\nYou chose Employee.\n")

            # Choosing an operation
            while True: 
                x = input('Please enter a number to select an operation: 1(Insert), 2(Delete), or 3(Update)')
                if x.isnumeric():
                    break
                else:
                    print('Not a valid option')
            choice = int(x)

            # If Insert
            if choice == 1:
                print("\nYou chose Insert.\n")
                db.insertEmployee()

            # If Delete
            elif choice == 2:
                print("\nYou chose Delete.\n")
                delete_employee()

            # If Update
            elif choice == 3:
                print("\nYou chose Update.\n")
                edit_employee()

        #If Payroll
        elif choice == 2:
            print('\nYou chose Payroll.\n')

            # Choosing an operation
            while True: 
                x = input('Please enter a number to select an operation: 1(Insert), 2(View), 3(Delete), or 4(Update)')
                if x.isnumeric():
                    break
                else:
                    print('Not a valid option')
            choice = int(x)

            # If Insert
            if choice == 1:
                print('\nYou chose Insert.\n')
                add_payroll()

            # If Delete
            elif choice == 2:
                print('\nYou chose View.\n')
                view_payroll()

            elif choice == 3:   
                print('\nYou chose Delete.\n')
                delete_payroll()

            # If Update
            elif choice == 3:
                print('\nYou chose Update.\n')
                edit_payroll()
                

        else:
            break

        while True: 
            x = input('Please enter a number: 1(Employee), 2(Payroll), any other number(Quit)')
            if x.isnumeric():
                break
            else:
                print('Not a valid option')
        choice = int(x)

    print('Ending Program')

if __name__ == '__main__':
    main()

