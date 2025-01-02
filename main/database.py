import sqlite3

# Establish connection to the database
def connect_to_database():
    return sqlite3.connect('C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database\\main.db')

# Fetch patient records
def get_patient_records():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patients") 
    records = cursor.fetchall()
    connection.close() 
    return records

# Fetch appointment schedule
def get_appointment():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Appointment") 
    records = cursor.fetchall()
    connection.close() 
    return records

# Fetch billing records
def get_billing_records():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Billing") 
    records = cursor.fetchall()
    connection.close() 
    return records

# Fetch diagnostic reports
def get_diagnostic_report():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Diagnostic") 
    records = cursor.fetchall()
    connection.close() 
    return records

# Fetch pharmacy inventory
def get_pharmacy_inventory():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pharmacy") 
    records = cursor.fetchall()
    connection.close() 
    return records