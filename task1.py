from mysql import connector

my_connection = connector.connect(
    host="localhost",
    user="root",
    password="root",
)
my_cursor = my_connection.cursor()

# Write the DDL statements required to create the tables,
# including appropriate primary and foreign key integrity constraints.

my_cursor.execute("""
CREATE DATABASE IF NOT EXISTS ain3003_hw2;
USE ain3003_hw2;

CREATE TABLE IF NOT EXISTS Doctor (
    dr_code INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    FName VARCHAR(255) NOT NULL,
    Gender VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    designation VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Patient (
    pat_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    FName VARCHAR(255) NOT NULL,
    Gender VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    TelNo VARCHAR(255) NOT NULL,
    dr_code INT NOT NULL,
    FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
);

CREATE TABLE IF NOT EXISTS Patientdiagnosis (
    DiagNo INT AUTO_INCREMENT PRIMARY KEY,
    DiagDetails VARCHAR(255),
    DiagDate DATE NOT NULL,
    Remark VARCHAR(255),
    Other VARCHAR(255),
    pat_id INT NOT NULL,
    FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
);

CREATE TABLE IF NOT EXISTS Bill (
    BillNo INT AUTO_INCREMENT PRIMARY KEY,
    PatName VARCHAR(255) NOT NULL,
    DrName VARCHAR(255) NOT NULL,
    Datetime DATETIME NOT NULL,
    Amount INT NOT NULL,
    pat_id INT NOT NULL,
    FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
);

CREATE TABLE IF NOT EXISTS Staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Dept VARCHAR(255) NOT NULL,
    Gender VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    TelNo VARCHAR(255) NOT NULL,
    dr_code INT,
    FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
);

""")

my_connection.close()
