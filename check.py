import sqlite3
cn = sqlite3.connect("dataBase.db")
# a = cn.execute(''' 
#         SELECT * FROM students
#     ''')
# for b in a:
#     print(b)

print(" ")
che = cn.execute(''' 
        SELECT * FROM STUDENTS WHERE s_name LIKE '%v'
    ''')
for c in che:
    print(c)
for k in che:
    print(c)