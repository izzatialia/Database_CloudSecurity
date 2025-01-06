from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt  
from database import *
import sqlite3


class MyLogin(QMainWindow):

    def __init__(self):
        super(MyLogin, self).__init__()
        uic.loadUi(r'C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\login.ui', self)
        self.show()
        
        self.resize(700, 500)
        self.setCentralWidget(self.centralwidget)  # Set central widget for resizing purposes

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
        uic.loadUi(r'C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\dashboard.ui', self)
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
        self.actionDashboard.triggered.connect(lambda: self.open_dashboard("admin"))

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
        date_of_birth = self.dateEdit.date().toString("dd-MM-yyyy")
        if self.MaleButton.isChecked():
            patient_gender = "Male"
        elif self.FemaleButton.isChecked():
            patient_gender = "Female"

        contact_info = self.lineEdit_5.text()
        patient_email = self.lineEdit_6.text()
        address = self.lineEdit_7.text()
        
        try:
            conn = sqlite3.connect(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\Database\\main.db")
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
        self.actionDashboard.triggered.connect(lambda: self.open_dashboard("admin"))
        self.actionNew_Record.triggered.connect(self.open_new_record)
        self.actionDelete.triggered.connect(self.delete_patient_record)

        # Connect search button to search method
        self.searchButton.clicked.connect(self.on_search_button_click)
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
        
        
    def display_patient_records(self):
        records = get_patient_records()

        # Connect QTableWidget in the UI with the object name "patientTable"
        self.patientTable.setRowCount(0)  # Clear existing rows
        self.patientTable.setColumnCount(len(records[0]))  # Set the column count based on the records
        
        # set column headers based on the database table
        column_headers = ["Patient ID", "Name", "Date of Birth", "Gender", "Contact Info", "Email", "Address", "Medical History"]  # Replace with your actual columns
        self.patientTable.setHorizontalHeaderLabels(column_headers)

        for row_idx, row_data in enumerate(records):
            self.patientTable.insertRow(row_idx)  # Add a new row
            for col_idx, col_data in enumerate(row_data):
                self.patientTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
            
    def on_search_button_click(self):
        """
        Triggered when the search button is clicked.
        Fetch the Patient ID from the search input and highlight the matching row.
        """
        patient_id = self.lineEdit.text().strip()  # Get text from QLineEdit
        
        if patient_id:
            self.search_and_highlight_patient(patient_id)
        else:
            print("Please enter a Patient ID.")

    def search_and_highlight_patient(self, patient_id):
        """
        Search for a Patient ID in the table, scroll to it, and highlight the row.
        """
        found = False

        # Loop through all rows in the table
        for row in range(self.patientTable.rowCount()):
            item = self.patientTable.item(row, 0)  # Assuming Patient ID is in the 1st column (index 0)
            
            if item and item.text() == patient_id:
                # Highlight the row
                for col in range(self.patientTable.columnCount()):
                    self.patientTable.item(row, col).setBackground(Qt.yellow)

                # Scroll to the row and make it appear at the top
                self.patientTable.scrollToItem(item, QAbstractItemView.PositionAtTop)
                
                # Select the row (optional for better visibility)
                #self.patientTable.selectRow(row)
                
                print(f"Patient ID {patient_id} found and highlighted.")
                found = True
                break
        
        if not found:
            print("Patient ID not found.")    

    def open_new_record(self):
        # Open a form or dialog to input new patient data
        # For example, you can use another window to capture input
        self.new_record_window = MyNewPatientRecord(self)  # Assuming you have this class
        self.new_record_window.show()
        
    def delete_patient_record(self):
        """
        Deletes the selected patient record from both the table and the database.
        """
        selected_row = self.patientTable.currentRow()

        if selected_row >= 0:  # Check if a row is selected
            patient_id_item = self.patientTable.item(selected_row, 0)  # Patient ID is in column 0
            patient_id = patient_id_item.text()

            # Ask for confirmation before deletion
            reply = QMessageBox.question(self, 'Delete Patient', f"Are you sure you want to delete Patient ID {patient_id}?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    conn = sqlite3.connect(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\Database\\main.db")
                    cursor = conn.cursor()

                    # Delete record from database
                    query = "DELETE FROM Patients WHERE patient_id = ?"
                    cursor.execute(query, (patient_id,))

                    # Commit the transaction
                    conn.commit()

                    # Remove the record from the table
                    self.patientTable.removeRow(selected_row)

                    QMessageBox.information(self, "Success", "Patient record deleted successfully!")
                except sqlite3.Error as e:
                    QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
                finally:
                    if conn:
                        conn.close()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a patient record to delete.")   

class MyNewPatientRecord(QMainWindow):

    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\newPatientRecord.ui", self)
        self.dashboard_window = dashboard_window

        # call method to display new patient records
        #self.display_new_patient_records()

        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        self.saveButton.clicked.connect(self.save_data)

    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

    def save_data(self):
        # Retrieve Patient ID and Medical History from the input fields
        patient_id = self.lineEdit.text().strip()
        medical_history = self.textEdit.toPlainText().strip()
        medicine_name = self.textEdit_2.toPlainText().strip()
    
        if not patient_id:
            QMessageBox.warning(self, "Input Error", "Please enter a valid Patient ID.")
            return
    
        try:
            conn = sqlite3.connect(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\Database\\main.db")
            cursor = conn.cursor()
        
            # Check if the Patient ID exists in the database
            cursor.execute("SELECT * FROM Patients WHERE patient_id = ?", (patient_id,))
            result = cursor.fetchone()
        
            if result:
             # Update the medical history for the existing patient
                cursor.execute("""
                    UPDATE Patients 
                    SET medical_history = ?
                    WHERE patient_id = ?
                """, (medical_history, patient_id))
            
                conn.commit()
                QMessageBox.information(self, "Success", f"Medical history for Patient ID {patient_id} updated successfully!")

                # Update the medicine for the existing patient
                cursor.execute("""
                    UPDATE Prescription 
                    SET medicine_name = ?
                    WHERE patient_id = ?
                """, (medicine_name, patient_id))
            
                conn.commit()
                QMessageBox.information(self, "Success", f"Medicine Name for Patient ID {patient_id} updated successfully!")

            else:
                QMessageBox.warning(self, "Patient Not Found", f"No patient found with ID {patient_id}.")
    
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
    
        finally:
            if conn:
                conn.close()

class MyAppointment(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\appointment.ui", self)
        self.dashboard_window = dashboard_window
        
        # display appointment schedule
        self.display_appointment()

        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        self.actionDashboard.triggered.connect(lambda: self.open_dashboard("admin"))
        self.actionNew_Appointment.triggered.connect(self.open_newAppointment)
        self.actionDelete.triggered.connect(self.delete_appointment)


        # Connect search button to search method
        self.searchButton.clicked.connect(self.on_search_button_click)

    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

    def open_newAppointment(self):
            self.newAppointment_window = MyNewAppointment(self)
            self.newAppointment_window.show()
            self.close()

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

    def on_search_button_click(self):
        """
        Search for a Patient ID and scroll to it in the AppointmentSchedule table.
        """
        # Get the patient ID from the search lineEdit
        patient_id = self.lineEdit.text().strip()
        
        if not patient_id:
            QMessageBox.warning(self, "Search Error", "Please enter a Patient ID to search.")
            return
        
        # Search for the patient ID in the table
        found = False
        for row in range(self.AppointmentSchedule.rowCount()):
            item = self.AppointmentSchedule.item(row, 1)  # Column 1 is Patient ID
            if item and item.text() == patient_id:
                found = True
                
                # Scroll to the matching row
                self.AppointmentSchedule.scrollToItem(item, QAbstractItemView.PositionAtTop)
                
                # Highlight the row
                for col in range(self.AppointmentSchedule.columnCount()):
                    self.AppointmentSchedule.item(row, col).setBackground(Qt.yellow)
                
                # Stop searching after the first match
                break
        
        if not found:
            QMessageBox.information(self, "Not Found", f"No record found for Patient ID: {patient_id}")

    def delete_appointment(self):
        """
        Deletes the selected appointment record from both the table and the database.
        """
        selected_row = self.AppointmentSchedule.currentRow()

        if selected_row >= 0:  # Check if a row is selected
            appointment_id_item = self.AppointmentSchedule.item(selected_row, 0)  # Appointment ID is in column 0
            appointment_id = appointment_id_item.text()

            # Ask for confirmation before deletion
            reply = QMessageBox.question(self, 'Delete Appointment', 
                                         f"Are you sure you want to delete Appointment ID {appointment_id}?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                try:
                    conn = sqlite3.connect(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\Database\\main.db")
                    cursor = conn.cursor()

                    # Delete record from database
                    query = "DELETE FROM Appointment WHERE appointment_id = ?"
                    cursor.execute(query, (appointment_id,))

                    # Commit the transaction
                    conn.commit()

                    # Remove the record from the table
                    self.AppointmentSchedule.removeRow(selected_row)

                    QMessageBox.information(self, "Success", "Appointment record deleted successfully!")
                except sqlite3.Error as e:
                    QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
                finally:
                    if conn:
                        conn.close()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select an appointment record to delete.")    

class MyNewAppointment(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\newAppointment.ui", self)
        self.dashboard_window = dashboard_window

        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        self.setButton.clicked.connect(self.set_appointment)

         # Calendar widget for date selection
        self.calendar.selectionChanged.connect(self.update_date_from_calendar)
        self.selected_date = self.calendar.selectedDate().toString("dd-MM-yyyy")

    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window


    def update_date_from_calendar(self):
        """Update selected date from the calendar widget."""
        self.selected_date = self.calendar.selectedDate().toString("dd-MM-yyyy")
        print(f"Selected Date: {self.selected_date}")  # Debugging: Print selected date to console

    def set_appointment(self):
        """
        Save appointment for an existing or new patient into the database.
        """
        patient_id = self.lineEdit.text().strip()
        doctor_id = self.lineEdit_2.text().strip()
        appointment_id = self.lineEdit_5.text().strip()
        appointment_date = self.selected_date  # Date selected from the calendar widget
        appointment_status = self.lineEdit_3.text().strip()
        remarks = self.lineEdit_4.text().strip()
        
        if not patient_id or not doctor_id or not appointment_status or not appointment_id:
            QMessageBox.warning(self, "Validation Error", "Patient ID, Doctor ID, and Status are required fields!")
            return
        
        try:
            conn = sqlite3.connect(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\Database\\main.db")
            cursor = conn.cursor()
            
            # Insert or Update Appointment
            query = """
            INSERT INTO Appointment (patient_id, doctor_id, appointment_id, appointment_date, appointment_status, remarks)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (patient_id, doctor_id, appointment_id, appointment_date, appointment_status, remarks))
            
            conn.commit()
            QMessageBox.information(self, "Success", f"Appointment saved successfully for {appointment_date}!")
            print(f"Appointment Date Saved: {appointment_date}")  # Debugging: Print the saved date
        
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        
        finally:
            if conn:
                conn.close()

class MyReport(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\report.ui", self)
        self.dashboard_window = dashboard_window

        self.display_diagnostic_report()
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))

        # Connect search button to search method
        self.searchButton.clicked.connect(self.on_search_button_click)

        
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

    def on_search_button_click(self):
        """
        Triggered when the search button is clicked.
        Fetch the Patient ID from the search input and highlight the matching row.
        """
        patient_id = self.lineEdit.text().strip()  # Assuming searchPatientID is QLineEdit
        
        if patient_id:
            self.search_and_highlight_patient(patient_id)
        else:
            print("Please enter a Patient ID.")
    
    def search_and_highlight_patient(self, patient_id):
        """
        Search for a Patient ID in the table, scroll to it, and highlight the row.
        """
        found = False

        # Iterate through each row in the QTableWidget
        for row in range(self.DiagnosticReport.rowCount()):
            item = self.DiagnosticReport.item(row, 1)  # Assuming Patient ID is in the 2nd column (index 1)
            
            if item and item.text() == patient_id:
                # Highlight the row
                for col in range(self.DiagnosticReport.columnCount()):
                    self.DiagnosticReport.item(row, col).setBackground(Qt.yellow)

                # Scroll to the row and make it appear at the top
                self.DiagnosticReport.scrollToItem(item, QAbstractItemView.PositionAtTop)
                
                # Select the row (optional for better visibility)
                #self.DiagnosticReport.selectRow(row)
                
                print(f"Patient ID {patient_id} found and highlighted.")
                found = True
                break
        
        if not found:
            print("Patient ID not found.")

class MyBilling(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\billing.ui", self)
        self.dashboard_window = dashboard_window

        # display billing records
        self.display_billing()
            
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))

         # Connect search button to search method
        self.searchButton.clicked.connect(self.on_search_button_click)
        
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

    def on_search_button_click(self):
        """
        Triggered when the search button is clicked.
        Fetch the Patient ID from the search input and highlight the matching row.
        """
        patient_id = self.lineEdit.text().strip()  # Assuming searchPatientID is QLineEdit
        
        if patient_id:
            self.search_and_highlight_patient(patient_id)
        else:
            print("Please enter a Patient ID.")
    
    def search_and_highlight_patient(self, patient_id):
        """
        Search for a Patient ID in the table, scroll to it, and highlight the row.
        """
        found = False

        # Iterate through each row in the QTableWidget
        for row in range(self.BillingRecords.rowCount()):
            item = self.BillingRecords.item(row, 1)  # Assuming Patient ID is in the 2nd column (index 1)
            
            if item and item.text() == patient_id:
                # Highlight the row
                for col in range(self.BillingRecords.columnCount()):
                    self.BillingRecords.item(row, col).setBackground(Qt.yellow)

                # Scroll to the row and make it appear at the top
                self.BillingRecords.scrollToItem(item, QAbstractItemView.PositionAtTop)
                
                # Select the row (optional for better visibility)
                #self.DiagnosticReport.selectRow(row)
                
                print(f"Patient ID {patient_id} found and highlighted.")
                found = True
                break
        
        if not found:
            print("Patient ID not found.")

class MyPharmacy(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\\Users\\IZZATI ALIA.LAPTOP-ERD37JJV\\Downloads\\DATABASE & CLOUD SECURITY\\Assignment\\Database_CloudSecurity-main\\pharmacy.ui", self)
        self.dashboard_window = dashboard_window

        self.display_pharmacy_inventory()
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))

        # Connect search button to search method
        self.searchButton.clicked.connect(self.on_search_button_click)
        
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

    def on_search_button_click(self):
        """
        Triggered when the search button is clicked.
        Fetch the Patient ID from the search input and highlight the matching row.
        """
        prescription_id = self.lineEdit.text().strip()  # Assuming searchPatientID is QLineEdit
        
        if prescription_id:
            self.search_and_highlight_patient(prescription_id)
        else:
            print("Please enter a Patient ID.")
    
    def search_and_highlight_patient(self, prescription_id):
        """
        Search for a Patient ID in the table, scroll to it, and highlight the row.
        """
        found = False

        # Iterate through each row in the QTableWidget
        for row in range(self.PharmacyInventory.rowCount()):
            item = self.PharmacyInventory.item(row, 1)  # Assuming Patient ID is in the 2nd column (index 1)
            
            if item and item.text() == prescription_id:
                # Highlight the row
                for col in range(self.PharmacyInventory.columnCount()):
                    self.PharmacyInventory.item(row, col).setBackground(Qt.yellow)

                # Scroll to the row and make it appear at the top
                self.PharmacyInventory.scrollToItem(item, QAbstractItemView.PositionAtTop)
                
                # Select the row (optional for better visibility)
                #self.DiagnosticReport.selectRow(row)
                
                print(f"Prescription ID {prescription_id} found and highlighted.")
                found = True
                break
        
        if not found:
            print("Patient ID not found.")

def main():
    app = QApplication([])
    window = MyLogin()
    app.exec_()

if __name__ == '__main__':
    main()
    