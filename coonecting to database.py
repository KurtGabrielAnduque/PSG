import pyodbc

try:
    user_input = input('Create a name of the databse: ')
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-6AIOAKJ\\SQLEXPRESS;'
        'DATABASE=SampleDB;'
        'Trusted_Connection=yes;'
    )

    connection.autocommit = True
    connection.execute(f'CREATE DATABASE {user_input}')
    print(f'{user_input} name DATABASE has been created successfully')
except pyodbc.Error as ex:
    print('CONNECTION FAILED:', ex)
