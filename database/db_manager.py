import sqlite3

class DatabaseManager:

    def __init__(self):
        self.db_name = 'payroll.db'
        self.conn = None
        self.cursor = None

        try: #probe for db
            print('establishing connection to database')
            self.conn = sqlite3.connect('file:' + self.db_name + '?mode=rw')
            print('getting cursor')
            self.cursor = self.conn.cursor()
        except: # if no db, create it
            try: #create db
                self.conn = sqlite3.connect(self.db_name)
                self.cursor = self.conn.cursor()

                create_department_table = '''CREATE TABLE Department(
                                                Name VARCHAR(255), 
                                                Location VARCHAR(255))'''

                create_employee_table = '''CREATE TABLE Employee(
                                                First_Name VARCHAR(255) NOT NULL, 
                                                Last_Name VARCHAR(255), 
                                                Date_of_Birth DATE NOT NULL,
                                                Email VARCHAR(255),
                                                Phone_Num VARCHAR(255),
                                                Type VARCHAR(255),
                                                Status VARCHAR(255),
                                                Employee_ID INT,
                                                Dept_ID INT, 
                                                FOREIGN KEY(Dept_ID) REFERENCES Department(Dept_ID))'''

                create_payroll_table = '''CREATE TABLE Payroll(
                                                Type VARCHAR(255),
                                                Pay DECIMAL(10,2), 
                                                Employee_ID INT, 

                                                FOREIGN KEY(Employee_ID) REFERENCES Employee(Employee_ID))'''
                
                print('creating department')
                self.cursor.execute(create_department_table)
                print('creating employee')
                self.cursor.execute(create_employee_table)
                print('creating payroll')
                self.cursor.execute(create_payroll_table)

            except: #handle errors
                print('There was an error creating the tables')

    #--------------------- Department operations-------------------------------------------------

    def Insert_department(self):
        Name = input("Enter the name of the department: ")
        location = input("Enter the location: ")
        
        "INSERT INTO Department(Dept_ID) VALUES (" Name + i + Location")";
        VALUES({0},{1},{2})'''.format(Name, DeptID, Location)
        cursor.execute(insert_employee)
        except:
            print("ERROR: TABLE DOES NOT EXIST OR VALUES WERE FORMATTED INCORRECTLY\n")

    def Update_department(self, DeptID):
        print("1: Update DeptID\n")
        print("2: Update Name\n")
        print("3: Update Location\n")
       
       selection = input("")
       if selection == 1:
            newName = input("Enter the new name of the department you would like to update: ")
            try: #updates id if record exists
                update_id = "UPDATE Department SET Name={0} WHERE Dept_ID={2}".format(newDeptID, deptID)
                cursor.execute(update_id)    
            except:#record does not exist
                print("ERROR: DEPARTMENT WITH THE ID {} DOES NOT EXIST\n".format(deptID))
       
       if selection == 2:
            newDept_ID = input("Enter the new ID of the employee you would like to update: ")
            try: #updates name if record exists
                update_id = "UPDATE Department SET Dept_ID={0} WHERE Dept_ID={1}".format(newName, deptID)
                cursor.execute(update_Name)    
            except:#record does not exist
                print("ERROR: DEPARTMENT WITH THE ID {} DOES NOT EXIST\n".format(deptID))
                
      if selection == 3:
            newDept_ID = input("Enter the new location of the department you would like to update: ")
            try: #updates location if record exists
                update_id = "UPDATE Department SET Location={0} WHERE Dept_ID={1}".format(newLocation, deptID)
                cursor.execute(update_Location)    
            except:#record does not exist
                print("ERROR: DEPARTMENT WITH THE ID {} DOES NOT EXIST\n".format(deptID))   
             

    def delete_department(self):
       try:
            delete_department = '''DELETE FROM Department WHERE Department_ID={}'''.format(deptID)
            cursor.execute(delete_department)
        except:
           print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))


    #--------------------- Employee operations-------------------------------------------------

    def insertEmployee(self):
        firstName = input("Enter the first name of the employee: ")
        lastName = input("Enter the last name of the employee: ")
        dob = input("Enter the date of birth of the employee in the format of YYYY-MM-DD(dashes included): ")
        email = input("Enter the email address of the employee: ")
        phoneNum = input("Enter the phone number of the employee: ")
        Type = input("Enter the employee type(Manager, HR, CEO, etc.): ")
        status = input("Enter the status of the employee: ")
        try:
            insert_employee = '''INSERT INTO Employee(First_Name, 
                                                Last_Name, 
                                                Date_of_Birth,
                                                Email,
                                                Phone_Num,
                                                Type,
                                                Status)
                                 VALUES({0},{1},{2},{3},{4},{5},{6},{7},{8},)'''.format(firstName, lastName, dob, email, phoneNum, Type, status)
            cursor.execute(insert_employee)
        except:
            print("ERROR: TABLE DOES NOT EXIST OR VALUES WERE FORMATTED INCORRECTLY\n")

    def updateEmployee(self, empID):
        print("1: Update employee ID\n")
        print("2: Update name\n")
        print("3: Update email\n")
        print("4: Update phone number\n")
        print("5: Update type\n")
        print("6: Update status\n")
        print("7: Update department\n")
        
        selection = input("")
        if selection == 1:
            newEmployID = input("Enter the new ID of the employee you would like to update: ")
            try: #updates id if record exists
                update_id = "UPDATE Employee SET Employee_ID={0} WHERE Employee_ID={1}".format(newEmployID, empID)
                cursor.execute(update_id)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 2:
            newFirstName = input("Enter the new first name of the employee(if applicable): ")
            newLastName = input("Enter the new first name of the employee(if applicable): ")
            try: #updates name if record exists
                update_name = "UPDATE Employee SET First_Name={0}, Last_Name{1} WHERE Employee_ID={2}".format(newFirstName, newLastName, empID)
                cursor.execute(update_name)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 3:
            newEmail = input("Enter the employee's new email address: ")
            try: #updates email if record exists
                update_email = "UPDATE Employee SET Email={0} WHERE Employee_ID={1}".format(newEmail, empID)
                cursor.execute(update_email)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 4:
            newPhone = input("Please enter the new phone number of the employee: ")
            try: #updates phone number if record exists
                update_phone = "UPDATE Employee SET Phone_Num={0} WHERE Employee_ID={1}".format(newPhone, empID)
                cursor.execute(update_phone)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 5:
            newType = input("Please enter the new phone number of the employee: ")
            try: #updates type if record exists
                update_type = "UPDATE Employee SET Type={0} WHERE Employee_ID={1}".format(newType, empID)
                cursor.execute(update_type)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 6:
            newStatus = input("Please enter the new status of the employee: ")
            try: #updates phone number if record exists
                update_status = "UPDATE Employee SET Status={0} WHERE Employee_ID={1}".format(newStatus, empID)
                cursor.execute(update_status)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        elif selection == 7:
            newDept = input("Please enter the ID of the new department of the employee: ")
            try: #updates phone number if record exists
                update_dept = "UPDATE Employee SET Dept_ID={0} WHERE Employee_ID={1}".format(newDept, empID)
                cursor.execute(update_dept)
            except:#record does not exist
                print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))
        else:
            print("ERROR: OPTION NOT AVAILABLE\n")
        
    def deleteEmployee(self, empID):
        try:
            delete_employee = '''DELETE FROM Employee WHERE Employee_ID={}'''.format(empID)
            cursor.execute(delete_employee)
        except:
           print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT EXIST\n".format(empID))


    #--------------------- Payroll operations-------------------------------------------------

    def add_payroll(self, pay_type, pay, emp_ID):
        try:
            add = '''INSERT INTO Payroll(Type, Pay, Employee_ID)
                        VALUES({0} , {1}, {2})'''.format(pay_type, pay, emp_ID)
            cursor.execute(add)
        except:
            print('There was an error adding the payroll')


    def view_payroll(self, emp_ID):
        try:
            view = '''SELECT pay_type, pay FROM Payroll
                        WHERE Employee_ID = {0}'''.format(emp_ID)
            cursor.execute(view)
        except:
            print('ERROR: EMPLOYEE WITH THE ID {} DOES NOT HAVE A PAYROLL\n'.format(emp_ID))


    def edit_payroll(self, pay_type, pay, emp_ID):
        try:
            edit = '''UPDATE Payroll
                        SET Type = '{0}'
                            Pay = '{1}
                        WHERE Employee_ID = '{2}\''''.format(pay_type, pay, emp_ID)
            cursor.execute(edit)
        except:
            print('There was an error editing the payroll')


    def delete_payroll(self, emp_ID):
        try:
            delete = '''DELETE FROM Payroll 
                        WHERE Employee_ID={}'''.format(emp_ID)
            cursor.execute(delete)
        except:
           print("ERROR: EMPLOYEE WITH THE ID {} DOES NOT HAVE A PAYROLL\n".format(emp_ID))

    #--------------------- Payroll-Employee operations-------------------------------------------------



    # sqlStatements = "CREATE TABLE Payslip(Payslip_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Hours DECIMAL(5,2) NOT NULL, Payroll_ID INT, Net_Pay DECIMAL(10,2) NOT NULL, Gross_Pay DECIMAL(10,2) NOT NULL, Start_Date DATE NOT NULL NOT NULL, End_Date DATE NOT NULL NOT NULL, PRIMARY KEY(Payslip_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Bonus(Bonus_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Amount DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Bonus_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Raise(Raise_ID INT NOT NULL UNIQUE, Percent_Increase DECIMAL(5,2) NOT NULL, Previous_Pay DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Raise_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";
