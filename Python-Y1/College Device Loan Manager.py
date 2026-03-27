import time
from datetime import date

loans = [
    {
        "loan_id": 1, 

        "student_name": "Alex Green", 

        "student_id": "S12345", 

        "device_type": "Laptop", 

        "device_id": "L-001", 

        "date_out": "2025-11-24", 

        "due_back": "2025-12-01", 

        "returned": False 
    },
    
    {
        "loan_id": 2, 

        "student_name": "Malachi Bargate", 

        "student_id": "S15626", 

        "device_type": "Mobile", 

        "device_id": "L-006", 

        "date_out": "2025-05-22", 

        "due_back": "2025-06-05", 

        "returned": False 
    }
]

print("Please select an option from the list\n1. Create new Loan\n2. View all Loans\n3. Update a Loan\n4. Delete a Loan")
select = input("Input option: ")

def createLoan():
    loan_id = int(input("Input your loan id: "))
    student_name = input("Input your student name: ")
    student_id = input("Input your student id: ")
    device_type = input("Input your device type: ")
    device_id = input("Input your device id: ")
    date_out = input("Input the date loaned: ")
    date_back = input("Input the date due back: ")
    returned_val = False

    today = date.today()
    if str(today) == str(date_back):
        returned = input(f"The loan is finished for the device: {device_id}, have you returned your item(s)? ")
        if returned.lower() == "y" or returned.lower() == "yes":
            print("Okay, processing...")
            print("Successful!")
            returned_val = True
            return returned_val
        else:
            print("Please return your item(s) and do not continue to use it/them as the deadline is up.")
            return returned_val
    
    new_loan = {
        "loan_id": loan_id,
        "student_name": student_name,
        "student_id": student_id,
        "device_type": device_type,
        "device_id": device_id,
        "date_out": date_out,
        "due_back": date_back,
        "returned": returned_val
    }

    loans.append(new_loan)
    print("Loan added successfully.")

def viewLoans():
    print("Select options from the list\n1. View all loans\n2. Search by student id\n3. Search by device id")
    view_select = input("Input selection: ")

    if view_select == "1":
        print("Attempting to view all Loans on record...")
        if loans:
            print("Successful!")
            print(loans)
        else:
            print("ERROR: Loans does not exist!")

    elif view_select == "2":
        student_ids = [loan["student_id"] for loan in loans]
        id_input = input("Input student ID to search with: ")
        if id_input in student_ids:
            loan_match = next((loan for loan in loans if loan["student_id"] == id_input),None)
            print("Found matching loan!")
            print(loan_match)
        else:
            print("ERROR: Loan/Student ID doesn't exist!")

    elif view_select == "3":
        device_ids = [loan["device_id"] for loan in loans]
        id_input = input("Input device ID to search with: ")
        if id_input in device_ids:
            loan_match = next((loan for loan in loans if loan["device_id"] == id_input),None)
            print("Found matching loan!")
            print(loan_match)
        else:
            print("ERROR: Loan/Device ID doesn't exist!")
    
def updateLoan():
    selected_loan = int(input("Input loan ID to edit: "))
    loan_match = next((loan for loan in loans if loan["loan_id"] == selected_loan),None)
   
    for key, value in loan_match.items():
        print(f"{key}: {value}")
    print("Please select a value to edit")
    selected_value = input("Enter: ")

    if selected_value in loan_match:
        print("Enter new value")
        new_Value = input((f"{selected_value}: "))
        loan_match[selected_value] = new_Value

        print("Successfully updated value(s)")

        print(loan_match)

if select == "1":
    createLoan()
elif select == "2":
    viewLoans()
elif select == "3":
    updateLoan()
elif select == "4":
    pass