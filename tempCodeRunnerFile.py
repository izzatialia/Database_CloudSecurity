from PyQt5.QtWidgets import *
from PyQt5 import uic



class MyLogin(QMainWindow):

    def __init__(self):
        super(MyLogin, self).__init__()
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\login.ui", self)
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
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\dashboard.ui", self)
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

    def open_registration(self):
        self.registration = MyRegistration(self) #transition to registration
        self.registration.show()
        self.close() #close the dashboard window

    def open_patient_record(self):
        self.patientRecord = MyPatientRecord(self) #transition to registration
        self.patientRecord.show()
        self.close() #close the dashboard window

    def open_appointment(self):
        self.appointment = MyAppointment(self) #transition to registration
        self.appointment.show()
        self.close() #close the dashboard window

    def open_report(self):
        self.report = MyReport(self) #transition to registration
        self.report.show()
        self.close() #close the dashboard window

    def open_billing(self):
        self.billing = MyBilling(self) #transition to registration
        self.billing.show()
        self.close() #close the dashboard window

    def open_pharmacy(self):
        self.pharmacy = MyPharmacy(self) #transition to registration
        self.pharmacy.show()
        self.close() #close the dashboard window
          
class MyRegistration(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\registration.ui", self)
        self.dashboard_window = dashboard_window

        self.newRegistration.clicked.connect(self.open_new_registration)

    def open_new_registration(self):
        self.newRegistration = MyRegistration(self) #transition to registration
        self.newrRegistration.show()
        self.close() #close the dashboard window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
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
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\newRegistration.ui", self)
        self.dashboard_window = dashboard_window

        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

class MyPatientRecord(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\patientRecord.ui", self)
        self.dashboard_window = dashboard_window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window
        #self.dashboard = MyDashboard(role, self) #transition to Dashboard
        #self.dashboard.show()
        #self.close() #close the login window

class MyAppointment(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\appointment.ui", self)
        self.dashboard_window = dashboard_window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

class MyReport(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\report.ui", self)
        self.dashboard_window = dashboard_window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

class MyBilling(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\billing.ui", self)
        self.dashboard_window = dashboard_window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window

class MyPharmacy(QMainWindow):
    def __init__(self, dashboard_window, parent=None):
        super().__init__(parent)
        uic.loadUi(r"C:\Users\user\OneDrive - mmu.edu.my\3rd Year\DATABASE\Assignment 1\pharmacy.ui", self)
        self.dashboard_window = dashboard_window

    
        self.actionBack.triggered.connect(lambda: self.open_dashboard("admin"))
        
    def open_dashboard(self, role):
        if self.dashboard_window:  # Ensure the reference exists
            self.dashboard_window.show()
            self.close()  # Close the current window


def main():
    app = QApplication([])
    window = MyLogin()
    app.exec_()

if __name__ == '__main__':
    main()
    