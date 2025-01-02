from PyQt5.QtWidgets import *
from PyQt5 import uic
from database import *
import sqlite3


class MyLogin(QMainWindow):

    def __init__(self):
        super(MyLogin, self).__init__()
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\login.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.login)
        self.actionClose.triggered.connect(exit)

    def login(self):
        username = self.Username.text()
        password = self.Password.text()

        # Chck Login credentials
        if username == "admin" and password  == "Pa$$w0rd":
            self.open_dashboard("admin")
        elif username == "doctor" and password == "Pa$$w0rd":
            self.open_dashboard("doctor")
        elif username == "billingstaff" and password == "Pa$$w0rd":
            self.open_dashboard("billingstaff")
        elif username == "pharmacist" and password == "Pa$$w0rd":
            self.open_dashboard("pharmacist")
        else:
            message = QMessageBox()
            message.setText("Invalid Login")
            message.exec_()

    def open_dashboard(self, role):
        self.dashboard = MyDashboard(role, self) #transition to Dashboard
        self.dashboard.show()
        self.close() #close the login window

class MyDashboard(QMainWindow):
    def __init__(self, role, login_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\dashboard.ui", self)
        self.role = role
        self.login_window = login_window
        
        self.setup_dashboard()
        self.show()
        self.actionSign_Out.triggered.connect(self.sign_out)

    def sign_out(self):
         self.login_window.Username.clear()  # Clear the username field
         self.login_window.Password.clear()  # Clear the password fiel
         self.login_window.show()
         self.close

    def setup_dashboard(self):
        if self.role == "doctor":
            # Resrtict access for the doctor role
            
            self.patientRecord.setEnabled(True)
            self.Report.setEnabled(True)
            self.Pharmacy.setEnabled(True)
            self.Registration.setEnabled(False)
            self.Appointment.setEnabled(False)
            self.Billing.setEnabled(False)

            # Connect buttons to actions
           
            self.patientRecord.clicked.connect(self.open_patient_record)
            self.Report.clicked.connect(self.open_report)
            self.Pharmacy.clicked.connect(self.open_pharmacy)

        elif self.role == "admin":
            # Full access for admin
               
            self.Registration.setEnabled(True)
            self.patientRecord.setEnabled(True)
            self.Appointment.setEnabled(True)
            self.Report.setEnabled(True)
            self.Billing.setEnabled(True)
            self.Pharmacy.setEnabled(True)

            self.Registration.clicked.connect(self.open_registration)
            self.patientRecord.clicked.connect(self.open_patient_record)
            self.Appointment.clicked.connect(self.open_appointment)
            self.Report.clicked.connect(self.open_report)
            self.Billing.clicked.connect(self.open_billing)
            self.Pharmacy.clicked.connect(self.open_pharmacy)

        elif self.role == "billingstaff":
               
            self.patientRecord.setEnabled(False)
            self.Report.setEnabled(False)
            self.Pharmacy.setEnabled(True)
            self.Registration.setEnabled(False)
            self.Appointment.setEnabled(False)
            self.Billing.setEnabled(True)

            self.Billing.clicked.connect(self.open_billing)
            self.Pharmacy.clicked.connect(self.open_pharmacy)
        
        elif self.role == "pharmacist":
               
            self.patientRecord.setEnabled(False)
            self.Report.setEnabled(True)
            self.Pharmacy.setEnabled(True)
            self.Registration.setEnabled(False)
            self.Appointment.setEnabled(False)
            self.Billing.setEnabled(False)

            self.Pharmacy.clicked.connect(self.open_pharmacy)
            self.Report.clicked.connect(self.open_report)

    def open_registration(self):
        self.registration = MyRegistration(self) #transition to registration
        self.registration.show()
        self.close() #close the dashboard window

    def open_patient_record(self):
        self.patientRecord = MyPatientRecord(self) #transition to patient record
        self.patientRecord.show()
        self.close() #close the dashboard window

    def open_appointment(self):
        self.appointment = MyAppointment(self) #transition to appointment
        self.appointment.show()
        self.close() #close the dashboard window

    def open_report(self):
        self.report = MyReport(self) #transition to report
        self.report.show()
        self.close() #close the dashboard window

    def open_billing(self):
        self.billing = MyBilling(self) #transition to billing
        self.billing.show()
        self.close() #close the dashboard window

    def open_pharmacy(self):
        self.pharmacy = MyPharmacy(self) #transition to pharmacy
        self.pharmacy.show()
        self.close() #close the dashboard window
          
class MyRegistration(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\registration.ui", self)
        self.dashboard_window = dashboard_window

        self.newRegister.clicked.connect(self.open_new_registration)
        self.viewPatientList.clicked.connect(self.view_patient_list)
        
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))


    def open_new_registration(self):
        self.newRegistration = MyNewRegistration(self) #transition to new registration
        self.newRegistration.show()
        self.close()

    
        # self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
    
    def view_patient_list(self):
        self.display_patient_list = MyPatientRecord(self) 
        self.display_patient_list.show()
        self.close() 
        # records = get_patient_records()
    
        # self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
        
        ##self.dashboard = MyDashboard(role, self) #transition to Dashboard
        #self.dashboard.show()
        #self.close() #close the login window

class MyNewRegistration(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\newRegistration.ui", self)
        self.dashboard_window = dashboard_window

        self.pushButton.clicked.connect(self.save_data)
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
            
    def save_data(self):
        # Retrieve data from textboxes
        patient_id = self.lineEdit_1.text()
        patient_name = self.lineEdit_2.text()
        date_of_birth = self.lineEdit_3.text()
        patient_gender = self.lineEdit_4.text()
        contact_info = self.lineEdit_5.text()
        patient_email = self.lineEdit_6.text()
        address = self.lineEdit_7.text()
        
        try:
            conn = sqlite3.connect('C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database\\main.db')
            cursor = conn.cursor()

            # Step 4: Insert data into the Patients table
            query = """
            INSERT INTO Patients (patient_id, patient_name, date_of_birth, patient_gender, contact_info, patient_email, address)
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (patient_id, patient_name, date_of_birth, patient_gender, contact_info, patient_email, address))

            # Commit the transaction
            conn.commit()

            # Step 5: Show success message
            QMessageBox.information(self, "Success", "Patient data saved successfully!")

        except sqlite3.Error as e:
            # Handle database errors
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        
        # finally:
        #     # Close the database connection
        #     if conn:
        #         conn.close()

class MyPatientRecord(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\patientRecord.ui", self)
        self.dashboard_window = dashboard_window

        # call method to display patient records
        self.display_patient_records()
        
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
        #self.dashboard = MyDashboard(role, self) #transition to Dashboard
        #self.dashboard.show()
        #self.close() #close the login window
        
    def display_patient_records(self):
        records = get_patient_records()
        
        # Assuming a QTableWidget in the UI with the object name "patientTable"
        self.patientTable.setRowCount(0)  # Clear existing rows
        self.patientTable.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # Dynamically set column headers based on the database table (optional)
        column_headers = ["Patient ID", "Name", "Date of Birth", "Gender", "Contact Info", "Email", "Address", "Medical History"]  # Replace with your actual columns
        self.patientTable.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.patientTable.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.patientTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class MyAppointment(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\appointment.ui", self)
        self.dashboard_window = dashboard_window
        
        # display appointment schedule
        self.display_appointment()

        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
            
    def display_appointment(self):
        records = get_appointment()
        
        self.AppointmentSchedule.setRowCount(0)  # Clear existing rows
        self.AppointmentSchedule.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # Set column headers
        column_headers = ["Appointment ID", "Patient ID", "Doctor ID", "Date", "Status", "Remarks"]  
        self.AppointmentSchedule.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.AppointmentSchedule.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.AppointmentSchedule.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class MyReport(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\report.ui", self)
        self.dashboard_window = dashboard_window

        self.display_diagnostic_report()
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
            
    def display_diagnostic_report(self):
        records = get_diagnostic_report()
        
        self.DiagnosticReport.setRowCount(0)  # Clear existing rows
        self.DiagnosticReport.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # Set column headers
        column_headers = ["Diagnostic ID", "Patient ID", "Doctor ID", "Test Name", "Date", "Results"]  
        self.DiagnosticReport.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.DiagnosticReport.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.DiagnosticReport.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class MyBilling(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\billing.ui", self)
        self.dashboard_window = dashboard_window

        # display billing records
        self.display_billing()
            
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
            
    def display_billing(self):
        records = get_billing_records()
        
        self.BillingRecords.setRowCount(0)  # Clear existing rows
        self.BillingRecords.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # Set column headers
        column_headers = ["Bill ID", "Patient ID", "Medicine Name", "Amount", "BillingStaff ID"]  
        self.BillingRecords.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.BillingRecords.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.BillingRecords.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class MyPharmacy(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\pharmacy.ui", self)
        self.dashboard_window = dashboard_window

        self.display_pharmacy_inventory()
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
            
    def display_pharmacy_inventory(self):
        records = get_pharmacy_inventory()
        
        self.PharmacyInventory.setRowCount(0)  # Clear existing rows
        self.PharmacyInventory.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # Set column headers
        column_headers = ["Pharmacy ID", "Prescription ID", "Medicine Name", "Stock Quantity", "Price Per Unit (RM)", "Expiry Date"]  
        self.PharmacyInventory.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.PharmacyInventory.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.PharmacyInventory.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

def main():
    app = QApplication([])
    window = MyLogin()
    app.exec_()

if __name__ == '__main__':
    main()
    