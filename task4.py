
from mysql import connector

my_connection = connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ain3003_hw2',
)
my_cursor = my_connection.cursor()

# Write the SQL statement that will return the patient’s name,
# doctor name the total debt for each patient where they
# patient fee is over 100. The total order value for a Patient
# debt is the sum of all the bills related to the patient.

my_cursor.execute('''
SELECT patient.name, patient.fname, doctor.name, doctor.fname, SUM(bill.amount)
FROM patient
INNER JOIN doctor
ON patient.dr_code = doctor.dr_code
INNER JOIN bill
ON patient.pat_id = bill.pat_id
WHERE bill.amount > 100
GROUP BY patient.pat_id
''')

print(f'| {"  Patient name": <16} | {"  Patient fname": <16} | {"  Doctor name": <16} | {"  Doctor fname": <16} | {"Total debt": <16} |', end='\n| ')
print(*('-' * 16 for _ in range(5)), sep=' | ', end=' |\n')
for (name, fname, name2, fname2, amount) in my_cursor:
    print(f'| {name: <16} | {fname: <16} | {name2: <16} | {fname2: <16} | {amount: <16} |')
    
my_connection.close()


