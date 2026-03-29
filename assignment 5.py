# bubble_sort 
arr = [5,3,8,1]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

# count_vowels
s = input()
count = 0
for i in s.lower():
    if i in 'aeiou':
        count += 1
print(count)

# create_table
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="testdb")
cursor = conn.cursor()

cursor.execute("CREATE TABLE employees (id INT, name VARCHAR(50), salary INT, department VARCHAR(50))")
print("Table Created")

# dict_to_json.
import json

data = {"name":"A","age":20}
with open("output.json","w") as f:
    json.dump(data,f)

#  insert_fetch
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="testdb")
cursor = conn.cursor()

data = [(1,"A",60000,"IT"),(2,"B",40000,"HR"),(3,"C",70000,"IT"),(4,"D",30000,"Sales"),(5,"E",80000,"HR")]
cursor.executemany("INSERT INTO employees VALUES (%s,%s,%s,%s)", data)
conn.commit()

cursor.execute("SELECT * FROM employees")
for i in cursor.fetchall():
    print(i)

# json_read
import json

with open("json_create.json") as f:
    data = json.load(f)
    print(data)

# linear_search
arr = [1,2,3,4,5]
x = 3
for i in range(len(arr)):
    if arr[i] == x:
        print("Found at index",i)

#  palindrome
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#python_mysql_connection
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

print("Connected Successfully")

# reverse_string
s = input()
rev = ""
for i in s:
    rev = i + rev
print(rev)

#salary_filter
cursor.execute("SELECT * FROM employees WHERE salary > 50000")
print(cursor.fetchall())

#sql_queries.sql
-- 2nd highest salary
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);

-- department wise avg
SELECT department, AVG(salary) FROM employees GROUP BY department;

#update_delete
cursor.execute("UPDATE employees SET salary=90000 WHERE id=1")
cursor.execute("DELETE FROM employees WHERE id=2")
conn.commit()

