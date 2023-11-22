
5 tables

table Patientdiagnosis
- DiagNo (primary key)
- DiagDetails
- DiagDate
- Remark
- Other
- pat_id (foreign key to Patient table)

table Patient
- pat_id (primary key)
- Name
- FName
- Gender
- Address
- TelNo
- dr_code (foreign key to Doctor table)

table Doctor
- dr_code (primary key)
- Name
- FName
- Gender
- Address
- designation

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
The Database consists of 5 tables; patient, doctor, staff, diagnosis and bill. The 'patient' table consists of the basic data about the patient. 'doctor' consists of the information about doctor.
The table 'staff' consists of the information regarding the employees. 'diagnosis' consists of data about the patient's health analysis. And finally, 'bill' table has the fee for the patient. The billing system is integrated within a single database.