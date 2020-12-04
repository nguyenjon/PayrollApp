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

    def add_department(self):
        
        #"INSERT INTO Department(Dept_ID) VALUES (" + i +")";
        pass

    def edit_department(self):
        pass

    def delete_department(self):
        pass

    #--------------------- Employee operations-------------------------------------------------

    def add_employee(self):
        pass

    def edit_employee(self):
        pass

    def delete_employee(self):
        pass


    #--------------------- Payroll operations-------------------------------------------------

    def add_payroll(self, pay_type, pay, emp_ID):
        try:
            add = '''INSERT INTO Payroll(Type, Pay, Employee_ID)
                        VALUES({0} , {1}, {2})'''.format(pay_type, pay, emp_ID)
            cursor.execute(add)
        except:
            print('There was an error adding the payroll')

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
            delete = '''DEELETE from Payroll
                            WHERE Employee_ID = '{0}\''''.format(emp_ID)
            cursor.execute(delete)
        except:
            print('There was an error adding the payroll')





    # sqlStatements = "CREATE TABLE Payslip(Payslip_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Hours DECIMAL(5,2) NOT NULL, Payroll_ID INT, Net_Pay DECIMAL(10,2) NOT NULL, Gross_Pay DECIMAL(10,2) NOT NULL, Start_Date DATE NOT NULL NOT NULL, End_Date DATE NOT NULL NOT NULL, PRIMARY KEY(Payslip_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Bonus(Bonus_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Amount DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Bonus_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Raise(Raise_ID INT NOT NULL UNIQUE, Percent_Increase DECIMAL(5,2) NOT NULL, Previous_Pay DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Raise_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";
