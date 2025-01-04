CREATE TABLE Users (
    user_id VARCHAR(20) PRIMARY KEY NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    user_name VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    user_role VARCHAR(20) NOT NULL, 
    user_email VARCHAR(100),
    phone_number VARCHAR(15),
    CHECK (user_role IN ('Administrators', 'Doctor', 'BillingStaff', 'Pharmacist'))
);

CREATE TABLE Patients (
    patient_id VARCHAR(20) PRIMARY KEY NOT NULL,
    patient_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    patient_gender VARCHAr(2),
    contact_info VARCHAR(15),
    patient_email VARCHAR(100),
    address VARCHAR(150),
    medical_history VARCHAR(200),
    CHECK (patient_gender IN ('Male', 'Female'))
);

CREATE TABLE Appointment (
    appointment_id VARCHAR(20) PRIMARY KEY NOT NULL,
    patient_id VARCHAR(20),
    doctor_id VARCHAR(20),
    appointment_date DATETIME NOT NULL,
    appointment_status VARCHAR(20) NOT NULL,
    remarks TEXT,
    CHECK (appointment_status IN ('Scheduled', 'Completed', 'Cancelled')),
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id), 
    FOREIGN KEY (doctor_id) REFERENCES Users (user_id)
);

CREATE TABLE Diagnostic (
    diagnostic_id VARCHAR(20) PRIMARY KEY NOT NULL,
    patient_id VARCHAR(20),
    doctor_id VARCHAR(20),
    test_name VARCHAR(50),
    test_date DATETIME,
    results VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id), 
    FOREIGN KEY (doctor_id) REFERENCES Users (user_id)
);

CREATE TABLE Billing (
    bill_id VARCHAR(20) PRIMARY KEY NOT NULL,
    patient_id VARCHAR(20),
    medic_name VARCHAR(50),
    total_amount REAL,
    billingstaff_id VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id), 
    FOREIGN KEY (billingstaff_id) REFERENCES Users (user_id)
);

CREATE TABLE Pharmacy (
    pharmacy_id VARCHAR(20) PRIMARY KEY NOT NULL,
    prescription_id VARCHAR(20),
    medicine_name VARCHAR(50),
    stock_quantity INTEGER,
    price_per_unit INTEGER,
    expire_date DATE,
    FOREIGN KEY (prescription_id) REFERENCES Prescription (prescription_id)
);


CREATE TABLE Prescription (
    prescription_id VARCHAR(20) PRIMARY KEY NOT NULL,
    patient_id VARCHAR(20),
    doctor_id VARCHAR(20),
    medicine_name VARCHAR(50),
    dosage VARCHAR(50),
    duration_consume VARCHAR(50),
    pharmacy_id VARCHAR(20),
    pharmacist_id VARCHAR(20),
    dispense_date DATETIME,
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id), 
    FOREIGN KEY (doctor_id) REFERENCES Users (user_id), 
    FOREIGN KEY (pharmacist_id) REFERENCES Users (user_id),
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacy (pharmacy_id)
);



--SELECT * FROM Users;

DROP TABLE Users; 
DROP TABLE Patients;
DROP TABLE Appointment;
DROP TABLE Diagnostic;
DROP TABLE Billing;
DROP TABLE Pharmacy;
DROP TABLE Prescription;
