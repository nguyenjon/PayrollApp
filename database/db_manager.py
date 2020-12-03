import sqlite3

class DatabaseManager:

    def __init__(self):
        self.db_name = 'payroll.db'
        self.conn = None
        self.cursor = None

        try: #probe for db
            self.conn = sqlite3.connect(self.db_name + '?mode=rw')
            self.cursor = conn.cursor()
        except: # if no db, create it
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = conn.cursor()

            create_department_table = '''CREATE TABLE Department(
                                            Dept_ID INT NOT NULL UNIQUE, 
                                            Name VARCHAR(255), 
	                                        Location VARCHAR(255),

                                            PRIMARY KEY(Dept_ID))'''

            create_employee_table = '''CREATE TABLE Employee(
                                            Employee_ID INT NOT NULL UNIQUE, 
                                            First_Name VARCHAR(255) NOT NULL, 
                                            Last_Name VARCHAR(255), 
                                            Date_of_Birth DATE NOT NULL,
                                            Email VARCHAR(255),
                                            Phone_Num VARCHAR(255),
                                            Dept_ID VARCHAR(255), 
                                            Type VARCHAR(255),
                                            Status VARCHAR(255),
                                            Dept_ID INT, 

                                            PRIMARY KEY(Employee_ID), 
                                            FOREIGN KEY(Dept_ID) REFERENCES Department(Dept_ID))'''

            create_payroll_table = '''CREATE TABLE Payroll(
                                            Payroll_ID INT NOT NULL UNIQUE, 
                                            Type VARCHAR(255),
                                            Pay DECIMAL(10,2), 
                                            Employee_ID INT, 

                                            PRIMARY KEY(Payroll_ID), 
                                            FOREIGN KEY(Employee_ID) REFERENCES Employee(Employee_ID))''';

            cursor.execute(create_department_table)
            cursor.execute(create_employee_table)
            cursor.execute(create_payroll_table)
        
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

    def add_payroll(self):
        pass

    def edit_payroll(self):
        pass

    def delete_payroll(self):
        pass





    # sqlStatements = "CREATE TABLE Payslip(Payslip_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Hours DECIMAL(5,2) NOT NULL, Payroll_ID INT, Net_Pay DECIMAL(10,2) NOT NULL, Gross_Pay DECIMAL(10,2) NOT NULL, Start_Date DATE NOT NULL NOT NULL, End_Date DATE NOT NULL NOT NULL, PRIMARY KEY(Payslip_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Bonus(Bonus_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Amount DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Bonus_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Raise(Raise_ID INT NOT NULL UNIQUE, Percent_Increase DECIMAL(5,2) NOT NULL, Previous_Pay DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Raise_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";