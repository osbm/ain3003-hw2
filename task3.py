from mysql import connector

my_connection = connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ain3003_hw2',
)
my_cursor = my_connection.cursor()

# Write the SQL statement to find the Doctor names and all of their patients.

my_cursor.execute('''
SELECT doctor.name, doctor.fname, patient.name, patient.fname
FROM doctor
INNER JOIN patient
ON doctor.dr_code = patient.dr_code
''')

print(f'| {"  Doctor name": <16} | {"  Doctor fname": <16} | {"  Patient name": <16} | {"  Patient fname": <16} |', end='\n| ')
print(*('-' * 16 for _ in range(4)), sep=' | ', end=' |\n')
for (name, fname, name2, fname2) in my_cursor:
    print(f'| {name: <16} | {fname: <16} | {name2: <16} | {fname2: <16} |')

my_connection.close()
