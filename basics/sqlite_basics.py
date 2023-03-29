"""
The SQLite project provides a simple command-line program named sqlite3 (or sqlite3.exe on Windows) 
that allows the user to manually enter and execute SQL statements against an SQLite database or against a ZIP archive. 
Special commands to sqlite3 (dot-commands)
For a listing of the available dot commands, you can enter ".help"

The BEGIN TRANSACTION starts a new transaction. 
It ensures that all subsequent statements execute successfully or nothing executes at all.
The COMMIT statement commits all the statements.
The last_insert_rowid() function returns the ROWID of the last row insert from the database connection which invoked the function. 

# 1. Create / Open a database
$ sqlite3 company.db
SQLite version 3.37.0 2021-12-09 01:34:53
Enter ".help" for usage hints.
sqlite> 

# 2. List names of tables matching LIKE pattern ?TABLE? 
sqlite> .tables         
sqlite>                 

# 3. Create table Department
sqlite> CREATE TABLE IF NOT EXISTS Department (
   ...>     DepartmentID INTEGER NOT NULL,
   ...>     Name text NOT NULL,
   ...>     PRIMARY KEY(DepartmentID AUTOINCREMENT));

# 4. Check if the table is created:
sqlite> .tables
Department

# 5. Display schema of the table:
sqlite> .schema Department
CREATE TABLE Department (
    DEPARTMENT_ID INTEGER NOT NULL,
    NAME text NOT NULL,
    PRIMARY KEY(DEPARTMENT_ID AUTOINCREMENT));

# 6. Turn display of headers on and set output mode (for the display of query results)
sqlite> .headers on     
sqlite> .mode column 

# 7. insert new records, and delete existing records in Department:
sqlite> INSERT INTO Department(Name) VALUES ("Sales");      
sqlite> INSERT INTO Department(Name) VALUES ("OLD");
sqlite> DELETE FROM Department WHERE Name = "OLD";
sqlite> INSERT INTO Department(Name) VALUES ("Finance");    

# 8. Select inserted records. Note that PRIMARY KEY is autoincremented.
# Note that although DepartmentID=2 is deleted, we still get 3 from sequence at new insertion!
sqlite> SELECT * FROM Department;       
DepartmentID  Name   
------------  -------
1             Sales  
3             Finance

# 9. Create another table for Employee records:
sqlite> CREATE TABLE IF NOT EXISTS Employee (   
   ...>     EmployeeID INTEGER NOT NULL,
   ...>     LastName text NOT NULL,
   ...>     DepartmentID INTEGER NOT NULL,
   ...>     Salary REAL,
   ...>     PRIMARY KEY(EmployeeID AUTOINCREMENT)
   ...>     FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID));

sqlite> .tables
Department  Employee  

# 10. Insert a new record into Employee:
sqlite> INSERT INTO Employee(LastName, DepartmentID, Salary) VALUES ("Fin", 3, 10000.50);

# 11. Select inserted records 
sqlite> SELECT * FROM Employee;
EmployeeID  LastName  DepartmentID  Salary 
----------  --------  ------------  -------
1           Fin       2             10000.5

# 12. See autoincremented fields' current values: 
sqlite> SELECT * FROM sqlite_sequence;
name        seq
----------  ---
Department  2  
Employee    1


In computer science, a database cursor is a mechanism that enables traversal over the records in a database.
Cursors are used by database programmers to process individual rows returned by database system queries. 
The database cursor characteristic of traversal makes cursors akin to the programming language concept of iterator.

In SQL standard, the primary key column must not contain NULL values. 
It means that the primary key column has an implicit NOT NULL constraint.

SQLite primary key and rowid table
When you create a table without specifying the WITHOUT ROWID option, SQLite adds an implicit column called rowid that stores 64-bit signed integer. 
The rowid column is a key that uniquely identifies the rows in the table.
If a table has the primary key that consists of one column, and that column is defined as INTEGER then this primary key column becomes an alias for the rowid column.
Because the rowid table organizes its data as a B-tree, querying and sorting data of a rowid table are very fast.

SQLite recommends that you should not use AUTOINCREMENT attribute because 
the AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.
The main purpose of using attribute AUTOINCREMENT is to prevent SQLite to reuse a value that has not been used or a value from the previously deleted row.

How to persist objects, into relational tables?
------------------------------------------------
Suppose we have Employee who works for a Department.

Employee class, we have 
id: int
lastname: str, 
salary: float, 
department: Department      # instance of Department

Employee table, we have 
EmployeeID INTEGER NOT NULL,        # employee.id
LastName text NOT NULL,             # employee.lastname
Salary REAL,                        # employee.salary
DepartmentID INTEGER NOT NULL (FK)  # employee.department.id

Employee's department, as a foreign key, is kind of a prerequisite:
    1. Create a department object without an id.
    2. Insert into database. 
    3. Update department object with the id from the last insert statement (take a look at sqlite_sequence table)
    4. Create an employee object without an id. The department must have an id, so should have been saved previously.
    5. Insert employee into database. 
    6. ID will be autoincremented, update employee object's ID. 
    
Note that Employee.DepartmentID field will have the id (int) of the Department.DepartmentID field in the database.


"""
import os
import sqlite3
from util import clear_terminal, show_menu # we can import a function from a module !
from domain import * 

SQL_CREATE_TABLE_Employee = """CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER NOT NULL,
    LastName text NOT NULL,
    DepartmentID INTEGER NOT NULL,
    Salary REAL,
    PRIMARY KEY(EmployeeID AUTOINCREMENT)
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID));"""

SQL_CREATE_TABLE_Department = """CREATE TABLE IF NOT EXISTS Department (
    DepartmentID INTEGER NOT NULL,
    Name text NOT NULL,
    PRIMARY KEY(DepartmentID AUTOINCREMENT));"""

SQL_INSERT_Department = "INSERT INTO Department(Name) VALUES (?)"
SQL_INSERT_Employee = "INSERT INTO Employee(LastName, DepartmentID, Salary) VALUES (?, ?, ?)"

SQL_SELECT_Department = "SELECT DEPARTMENT_ID FROM Department WHERE NAME = (?)"

def main():

    clear_terminal()

    print("Welcome to the Workforce Management System.")

    mainMenuItems = [MenuItem("Departments"), MenuItem("Employees")]
    op = show_menu("Main Menu", mainMenuItems)
    if op == "Departments":
        clear_terminal()
        deptMenuItems = [MenuItem("List & Update Departments"), MenuItem("Create New Department")]
        dept_op = show_menu("Departments >", deptMenuItems)

        if dept_op == "List & Update Departments":
            departments = get_departments()
            # list comprehension - iterate each element, and apply a transformation (wrap into MenuItem)
            menu_items_dep = [MenuItem(department, department.name) for department in departments]
            selected_dept = show_menu("Departments > List & Update Departments", menu_items_dep)
            print(selected_dept)

            dept_name_new = input("Please provide a new name for the department: ").title()
            update_department(selected_dept, dept_name_new)

        elif dept_op == "Create New Department":
            # create a department object, and save it to the database.
            dept_name = input("Department Name: ").title()
            department = Department(dept_name)
            department = save_department(department)

        
    elif op == "Employees":
        clear_terminal()
        empMenuItems = [MenuItem("List & Update Employees"), MenuItem("Create New Employee")]
        emp_op = show_menu("Employees >", empMenuItems)

        if emp_op == "List & Update Employees":
            employees = get_employees()
            # list comprehension - iterate each element, and apply a transformation (wrap into MenuItem)
            menu_items_emp = [MenuItem(emp, f"{emp.lastname} ({emp.department.name})") for emp in employees]
            selected_employee = show_menu("Employees > List & Update Employees >", menu_items_emp)
            print(selected_employee)
            # update_employee(selected_employee)

        elif emp_op == "Create New Employee":
            # create an employee object, and save it to the database.
            emp_lastname = input("Employee Lastname: ").capitalize()
            emp_salary = float(input("Salary: "))

            # Let the user select one of the existing departments
            departments = get_departments()
            # list comprehension - iterate each element, and apply a transformation (wrap into MenuItem)
            menu_items_dep = [MenuItem(department, department.name) for department in departments]
            selected_dept = show_menu("Employees > Create New Employee > Select Department", menu_items_dep)

            # create an Employee instance, and save it to db:
            employee = Employee(emp_lastname, emp_salary, selected_dept)
            employee = save_employee(employee)




    # departments = get_departments()

    # menuItems = []
    # for department in departments:
    #     menuItems.append(department.name)
    # menuItems.append('Create New Department')

    # selection = menu(menuItems)
    # print(selection)


def mainOLD():
    with sqlite3.connect("data/company.db") as con :

        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()

        cursor.execute(SQL_CREATE_TABLE_Employee)
        
        # to create an employee, there is a foreign key prerequisite!
        save_department(con)


        # SQLite implicitly  creates a column named "rowid" and automatically assigns an integer value whenever you insert a new row into the table.
        # When you create a table that has an INTEGER PRIMARY KEY column, this column is the alias of the rowid column.
        # If you don’t specify the rowid value or you use a NULL value when you insert a new row, SQLite automatically assigns the next sequential integer, which is one larger than the largest rowid in the table. 
        # The rowid value starts at 1.


        # cursor.execute("""SELECT Employee.LAST_NAME, Department.NAME From Employee
        #     LEFT JOIN Department
        #     ON Employee.DEPARTMENT_ID = Department.DEPARTMENT_ID
        #     ORDER BY Employee.LAST_NAME""")
        # results = cursor.fetchall()
        # print("Showing: ", len(results), "results:")
        # for employee in results:
        #     print(employee)


        
        cursor.execute("SELECT * FROM Employee WHERE salary > 20000")
        results = cursor.fetchall()
        print("High-Paying Positions:", len(results))
        for employee in results:
            print(employee)


def get_db_abspath():

    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the database file
    return os.path.join(script_dir, 'data/company.db')  # /Users/mk/dev/python/basics/data/company.db


def get_departments():

    with sqlite3.connect(get_db_abspath()) as con :
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Department")
        # Note that rowcount is only accurate after the entire result set has been fetched.
        # print(cursor.rowcount, "rows.")

        # When you use a for loop to iterate over the cursor, the data is retrieved from the cursor one row at a time, as the loop iterates. 
        # This can be useful when dealing with large datasets, as it allows you to process the data incrementally, without loading all the rows into memory at once.
        # On the other hand, when you call cursor.fetchall(), all the rows in the result set are retrieved from the cursor and returned as a list of tuples. 
        # This can be convenient when you need to process all the data at once or when the size of the result set is relatively small.

        # Option 1 - cursor.fetchall()
        # row = cursor.fetchone()      # fetch 1 row.
        # rows = cursor.fetchmany(3)   # fetch 3 rows.
        # rows = cursor.fetchall()       # fetch all rows - loads all the rows into memory at once.
        # print("Showing: ", len(rows), "results:")
        # for department in rows:
        #     print(department)

        # Option 2 - iterate over cursor, without fetchall that loads all the rows into memory at once.
        cnt = 0
        departments = []
        for row in cursor:  # list of tuples.
            # print(row)      # each row is a tuple representing a record. i.e, (1, 'Technology')
            dept = Department(row[1])
            dept.id = row[0]
            departments.append(dept)
            cnt += 1
        # print("Total: ", cnt, "records.")

        return departments
    
def get_department_by_ID(id: int):
    with sqlite3.connect(get_db_abspath()) as con :
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Department WHERE DepartmentID = (?)", (id,))

        # Option 1 - cursor.fetch...()
        row = cursor.fetchone()      # fetch 1 row.
        dept = Department(row[1])
        dept.id = row[0]

        return dept
    
def update_department(department: Department, newName: str):
    with sqlite3.connect(get_db_abspath()) as con :

        cursor = con.cursor()
        cursor.execute("UPDATE Department SET Name = ?  WHERE DepartmentID = ?", (newName, department.id))

        # check if any rows were modified by the query
        if cursor.rowcount == 0:
            print("No rows modified.")
            #raise ValueError(f"No department with id {dept_id} found in the database")
        else:
            print(cursor.rowcount, "rows modified.")


        con.commit()    # commit the changes to the database


def get_employees():
    with sqlite3.connect(get_db_abspath()) as con :
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Employee")

        # Option 2 - iterate over cursor, without fetchall that loads all the rows into memory at once.
        cnt = 0
        employees = []
        for row in cursor:  # list of tuples.
            # print(row)      # each row is a tuple representing a record. i.e, (1, 'Relater', 5, 5555.55)

            # get FK object, from its ID
            dept = get_department_by_ID(row[2])

            emp = Employee(lastname=row[1], salary=row[3], department=dept)
            emp.id = row[0]
            employees.append(emp)
            # cnt += 1
        # print("Total: ", cnt, "records.")

        return employees
    

def save_department(department: Department):
    print("Saving department", department)

    with sqlite3.connect(get_db_abspath()) as con :
        cursor = con.cursor()
        cursor.execute(SQL_CREATE_TABLE_Department)
        
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()
        
        cursor.execute(SQL_INSERT_Department, (department.name,))
        res = cursor.execute('SELECT last_insert_rowid()')
        last_insert_rowid = res.fetchone()[0]
        department.id = last_insert_rowid     # Update department object with the id from the last insert statement
        # The INSERT statement implicitly opens a transaction, which needs to be committed before changes are saved in the database 
        # Call con.commit() on the connection object to commit the transaction:
        con.commit()

        print("Saved. ", department)
        return department
    
def save_employee(employee: Employee):
    print("Saving employee", employee)

    with sqlite3.connect(get_db_abspath()) as con :
        cursor = con.cursor()
        cursor.execute(SQL_CREATE_TABLE_Employee)
        
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()
        
        cursor.execute(SQL_INSERT_Employee, (employee.lastname, employee.department.id, employee.salary))
        res = cursor.execute('SELECT last_insert_rowid()')
        last_insert_rowid = res.fetchone()[0]
        employee.id = last_insert_rowid     # Update department object with the id from the last insert statement
        # The INSERT statement implicitly opens a transaction, which needs to be committed before changes are saved in the database 
        # Call con.commit() on the connection object to commit the transaction:
        con.commit()

        print("Saved. ", employee)
        return employee

def create_author():
    full_name = input("\nFull Name: ")
    return Author(full_name)

def create_book():
    title = input("\nTitle: ").capitalize()
    author = input("Author: ").capitalize()
    isbn = input("ISBN: ")
    g = input("Comma seperated list of Genres: ")
    genres = g.strip().split(',')   # Note that genres is List[str]
    author = create_author()
    return Book(title, author, isbn, genres)

def save_author(author: Author):
    with sqlite3.connect(get_db_abspath()) as con :
        
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()

        # Create table if not exists
        cursor.execute(SQL_CREATE_TABLE_AUTHOR)

        # Notice that ? placeholders are used to bind data to the query.
        # Always use placeholders instead of string formatting to bind Python values to SQL statements, to avoid SQL injection attacks
        res = cursor.execute(SQL_INSERT_AUTHOR, (author.fullname))

def save_book(book):
    
    with sqlite3.connect(get_db_abspath()) as con :
        
        # In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
        cursor = con.cursor()

        # Create table if not exists
        cursor.execute(SQL_CREATE_TABLE_BOOK)

        # Notice that ? placeholders are used to bind data to the query.
        # Always use placeholders instead of string formatting to bind Python values to SQL statements, to avoid SQL injection attacks
        book = create_book()

if __name__ == "__main__":
    main()