import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Aisha','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Ananya','Data Science','A',92)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','C',65)''')
cursor.execute('''Insert Into STUDENT values('Paul','Data Science','B',88)''')
cursor.execute('''Insert Into STUDENT values('Sara','DEVOPS','B',70)''')
cursor.execute('''Insert Into STUDENT values('Ravi','DEVOPS','A',95)''')
cursor.execute('''Insert Into STUDENT values('Leah','DEVOPS','C',45)''')
cursor.execute('''Insert Into STUDENT values('Michael','DEVOPS','B',60)''')
cursor.execute('''Insert Into STUDENT values('Sophie','Data Science','A',85)''')
cursor.execute('''Insert Into STUDENT values('Amit','Data Science','C',55)''')
cursor.execute('''Insert Into STUDENT values('Meera','Data Science','B',80)''')
cursor.execute('''Insert Into STUDENT values('Kiran','DEVOPS','A',78)''')
cursor.execute('''Insert Into STUDENT values('Nina','Data Science','B',90)''')
cursor.execute('''Insert Into STUDENT values('Arjun','DEVOPS','C',50)''')
cursor.execute('''Insert Into STUDENT values('Priya','Data Science','A',95)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
