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
                                            PRIMARY KEY(Dept_ID))'''

            create_employee_table = '''CREATE TABLE Employee(
                                            Employee_ID INT NOT NULL UNIQUE, 
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




    #--------------------- Employee operations-------------------------------------------------




    #--------------------- Payroll operations-------------------------------------------------







    
    # sqlStatements = "CREATE TABLE Payslip(Payslip_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Hours DECIMAL(5,2) NOT NULL, Payroll_ID INT, Net_Pay DECIMAL(10,2) NOT NULL, Gross_Pay DECIMAL(10,2) NOT NULL, Start_Date DATE NOT NULL NOT NULL, End_Date DATE NOT NULL NOT NULL, PRIMARY KEY(Payslip_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Bonus(Bonus_ID INT NOT NULL UNIQUE, Deductions DECIMAL(10,2) NOT NULL, Amount DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Bonus_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";

    # sqlStatements = "CREATE TABLE Raise(Raise_ID INT NOT NULL UNIQUE, Percent_Increase DECIMAL(5,2) NOT NULL, Previous_Pay DECIMAL(10,2) NOT NULL, Payroll_ID INT, Date DATE NOT NULL NOT NULL, PRIMARY KEY(Raise_ID), FOREIGN KEY(Payroll_ID) REFERENCES Payroll(Payroll_ID))";