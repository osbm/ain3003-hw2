from mysql import connector

my_connection = connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='ain3003_hw2',
)
my_cursor = my_connection.cursor()

# delete all the rows from all the tables
for table in ['Bill','Patientdiagnosis','Patient','Doctor','Staff']:
    my_cursor.execute(f'DELETE FROM {table};')
    my_connection.commit()

# reset the auto-increment values for all the tables
for table in ['Bill','Patientdiagnosis','Patient','Doctor','Staff']:
    my_cursor.execute(f'ALTER TABLE {table} AUTO_INCREMENT = 1;')
    my_connection.commit()

my_connection.close()