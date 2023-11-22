from mysql import connector
from faker import Faker
import random
# faker library is used to generate fake data
faker = Faker('tr_TR')

my_connection = connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ain3003_hw2',
)
my_cursor = my_connection.cursor()

num_bills = 1000
num_patients = 500
num_doctors = 200
num_staff = 50
num_diagnosis = 1000

# TABLE 1/5: Doctor

doctor_designations = [
    'General practitioner',
    'Internal medicine',
    'Psychiatrist',
    'Ophthalmology',
    'Surgeon',
    'Family medicine',
    'Doctor of Medicine',
    'Psychiatry',
    'Endocrinologist',
    'Emergency medicine',
    'Otorhinolaryngology',
    'Anesthesiologist',
    'Pediatrician',
    'Dermatology',
    'Cardiology',
    'Neurology',
    'Pathologist',
    'Urology',
    'Dermatologist',
    'Anesthesiology',
    'Gastroenterology',
    'General surgery',
    'Cardiologist',
    'Radiologist',
]

doctor_list = []
for i in range(num_doctors):
    doctor_list.append(
        (
            faker.first_name(),
            faker.last_name(),
            random.choice(['M', 'F']),
            faker.address(),
            random.choice(doctor_designations),
        )
    )

my_cursor.executemany(
    'INSERT INTO doctor (dr_code, Name, FName, Gender, Address, designation) VALUES (NULL, %s, %s, %s, %s, %s)',
    doctor_list
)
my_connection.commit()
print(f'Doctor table filled with {num_doctors} rows of fake data.')

# TABLE 2/5: Patient

patient_list = []
for i in range(num_patients):
    patient_list.append(
        (
            faker.first_name(),
            faker.last_name(),
            random.choice(['M', 'F']),
            faker.address(),
            faker.phone_number(),
            random.randint(1, num_doctors),
        )
    )

my_cursor.executemany(
    'INSERT INTO patient (Name, FName, Gender, Address, TelNo, dr_code) VALUES (%s, %s, %s, %s, %s, %s)',
    patient_list
)
my_connection.commit()
print(f'Patient table filled with {num_patients} rows of fake data.')

# TABLE 3/5: Patientdiagnosis

diagnosis_list = []
for i in range(num_diagnosis):
    diagnosis_list.append(
        (
            faker.sentence(), # sentences are latin sentences, not turkish 
            faker.date(),
            faker.sentence(),
            faker.sentence(),
            random.randint(1, num_patients),
        )
    )

my_cursor.executemany(
    'INSERT INTO patientdiagnosis (DiagDetails, DiagDate, Remark, Other, pat_id) VALUES (%s, %s, %s, %s, %s)',
    diagnosis_list
)
my_connection.commit()
print(f'Patientdiagnosis table filled with {num_diagnosis} rows of fake data.')

# TABLE 4/5: Bill
patient_names = [patient[0] for patient in patient_list]
patiend_doctor_ids = [patient[5]-1 for patient in patient_list]
doctor_names = [doctor_list[id][0] for id in patiend_doctor_ids]
zipped_doctor_patient = zip(doctor_names, patient_names)

bill_list = []
for i in range(num_bills):
    doctor_name, patient_name = random.choice(list(zip(doctor_names, patient_names)))
    bill_list.append(
        (
            patient_name,
            doctor_name,
            faker.date_time(),
            random.randint(1, 10000),
            random.randint(1, num_patients),
        )
    )

my_cursor.executemany(
    'INSERT INTO bill (PatName, DrName, Datetime, Amount, pat_id) VALUES (%s, %s, %s, %s, %s)',
    bill_list
)
my_connection.commit()
print(f'Bill table filled with {num_bills} rows of fake data.')

# TABLE 5/5: Staff

staff_departments = [
    'Administration',
    'Accounting',
    'Human Resources',
    'Marketing',
    'Sales',
    'Information Technology',
    'Customer Service',
    'Research and Development',
    'Production',
    'Legal',
    'Distribution',
    'Customer Service',
    'Purchasing',
    'Training',
    'Maintenance',
    'Security',
    'Facilities',
    'Management',
    'Support',
    'Nursing',
    'Dentistry',
    'Therapy',
    'Psychology',
    'Hospitality',
    'Food Service',
    'Culinary',
]
staff_list = []
for i in range(num_staff):
    staff_list.append(
        (
            faker.name(),
            random.choice(staff_departments),
            random.choice(['M', 'F']),
            faker.address(),
            faker.phone_number(),
            random.randint(1, num_doctors),
        )
    )

my_cursor.executemany(
    'INSERT INTO staff (Name, Dept, Gender, Address, TelNo, dr_code) VALUES (%s, %s, %s, %s, %s, %s)',
    staff_list
)
my_connection.commit()
print(f'Staff table filled with {num_staff} rows of fake data.')

my_connection.close()