# AIN3003 - DATABASE SYSTEMS AND CLOUD COMPUTING - Homework 2

## Running the code

### Prerequisites

- Python
- MySQL

And install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### Running the code

# Task 1

Task1 creates the database and tables in MySQL.

```bash
python task1.py
```

# Task 2

Task2 inserts fake data into the tables in MySQL.

```bash
python task2.py
```

Output:

```
Doctor table filled with 200 rows of fake data.
Patient table filled with 500 rows of fake data.
Patientdiagnosis table filled with 1000 rows of fake data.
Bill table filled with 1000 rows of fake data.
Staff table filled with 50 rows of fake data.
```

# Task 3

Task3 prints the doctor names and all of their patients.

```bash
python task3.py
```

Output:

```
|   Doctor name    |   Doctor fname   |   Patient name   |   Patient fname  |
| ---------------- | ---------------- | ---------------- | ---------------- |
| Tansev           | Akça             | Akif             | Aslan            |
| Fatigül          | Yüksel           | Tayaydın         | Şener            |
| Fatigül          | Yüksel           | Şali             | Akgündüz         |
| Fatigül          | Yüksel           | Hürdoğan         | Çamurcuoğlu      |
| Fatigül          | Yüksel           | Türkalp          | Çamurcuoğlu      |
| Fatigül          | Yüksel           | Tunahan          | Eraslan          |
| Lezize           | Zorlu            | Fenni            | Ergül            |
| Lezize           | Zorlu            | Ruhide           | Korutürk         |
| Korkmazalp       | Hayrioğlu        | Arıpınar         | Bilgin           |
```

# Task 4

Task4 prints the patient’s name, doctor name the total debt for each patient where they patient fee is over 100.

```bash
python task4.py
```

Output:

```
|   Patient name   |   Patient fname  |   Doctor name    |   Doctor fname   | Total debt       |
| ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| Nazende          | Korutürk         | Döner            | Ülker            | 18507            |
| Çamok            | Akçay            | Berran           | Durmuş           | 9889             |
| Ağakişi          | Durmuş           | Erinçer          | Manço            | 7121             |
| Gülüs            | Ertaş            | Abdiş            | Fırat            | 14316            |
| Yasemen          | Yıldırım         | Buhari           | Demir            | 8136             |
| Ergün            | Durdu            | Berran           | Durmuş           | 27434            |
| İlgi             | Zengin           | Dilara           | Bilir            | 19385            |
| Berksay          | Bilge            | Anargül          | Ergül            | 12681            |
```


## Description


Database is consistent of 5 tables

table Doctor
- dr_code (primary key)
- Name
- FName
- Gender
- Address
- designation

table Patient
- pat_id (primary key)
- Name
- FName
- Gender
- Address
- TelNo
- dr_code (foreign key to Doctor table)

table Patientdiagnosis
- DiagNo (primary key)
- DiagDetails
- DiagDate
- Remark
- Other
- pat_id (foreign key to Patient table)

table Bill
- BillNo (primary key)
- PatName
- DrName
- Datetime
- Amount
- pat_id (foreign key to Patient table)

table Staff
- staff_id (primary key)
- Name
- Dept
- Gender
- Address
- TelNo
- dr_code (foreign key to Doctor table)


The Above database is for a Hospital Management. The tables provide the doctor, staffs details and patient details including doctor's appointments and the billing system.
In the schema, the primary key of each relation is underlined, and the domain of each field is listed before the field name.

The Database consists of 5 tables; patient, doctor, staff, diagnosis and bill.
- The 'patient' table consists of the basic data about the patient.
- 'doctor' consists of the information about doctor.
- The table 'staff' consists of the information regarding the employees.
- 'diagnosis' consists of data about the patient's health analysis.
- And finally, 'bill' table has the fee for the patient.

The billing system is integrated within a single database.


## Tasks

### Task 1

Write the DDL statements required to create the tables, including appropriate primary and foreign key integrity constraints. Implement the task in python:

```python
from mysql import connector
my_connection = connector.connect(
 host="localhost",
 user="root",
 password="Secret_123",
 database="banking"
)
my_cursor = my_connection.cursor()
"""
create tables
"""
my_cursor.execute("""
insert a ddl statement
) engine=innodb
""")
```

### Task 2

Write the DML statements to insert sample data to every table. Implement the task in python.

### Task 3

Write the SQL statement to find the Doctor names and all of their patients.

### Task 4

Write the SQL statement that will return the patient’s name, doctor name the total debt for each patient where they patient fee is over 100. The total order value for a Patient debt is the sum of all the bills related to the patient. Implement the task in Python.
