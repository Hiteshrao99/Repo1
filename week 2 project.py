import mysql.connector

# Establish a connection to the database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="employee_management"
    )

# Function to add an employee
def add_employee(name, email, phone, address, post, salary):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, email, phone, address, post, salary) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, email, phone, address, post, salary))
    conn.commit()
    cursor.close()
    conn.close()

# Function to display all employee records
def display_records():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
    conn.close()

# Function to update employee information
def update_employee(emp_id, email, phone, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET email = %s, phone = %s, address = %s WHERE id = %s",
                   (email, phone, address, emp_id))
    conn.commit()
    cursor.close()
    conn.close()

# Function to promote an employee
def promote_employee(emp_id, salary_increase):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET salary = salary + %s WHERE id = %s", (salary_increase, emp_id))
    conn.commit()
    cursor.close()
    conn.close()

# Function to remove an employee record
def remove_employee(emp_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = %s", (emp_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Function to search for an employee by ID
def search_employee(emp_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (emp_id,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    return record

# User-friendly interface
def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Records")
        print("3. Update Information")
        print("4. Promote Employee")
        print("5. Remove Employee")
        print("6. Search Employee")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            address = input("Address: ")
            post = input("Post: ")
            salary = float(input("Salary: "))
            add_employee(name, email, phone, address, post, salary)
        
        elif choice == '2':
            display_records()
        
        elif choice == '3':
            emp_id = int(input("Employee ID: "))
            email = input("New Email: ")
            phone = input("New Phone: ")
            address = input("New Address: ")
            update_employee(emp_id, email, phone, address)
        
        elif choice == '4':
            emp_id = int(input("Employee ID: "))
            salary_increase = float(input("Salary Increase: "))
            promote_employee(emp_id, salary_increase)
        
        elif choice == '5':
            emp_id = int(input("Employee ID: "))
            remove_employee(emp_id)
        
        elif choice == '6':
            emp_id = int(input("Employee ID: "))
            record = search_employee(emp_id)
            if record:
                print(record)
            else:
                print("Employee not found.")
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

