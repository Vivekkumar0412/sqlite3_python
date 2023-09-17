import sqlite3
conn = sqlite3.connect("dataBase.db")
# try:
#     conn.execute(''' 
#         Create table students(
#              s_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
#              s_name VARCHAR(30),
#              s_class VARCHAR(10),
#              s_email VARCHAR(40)
#         )
#     ''')
#     conn.close()


    
# except:
#     print("THE TABLE ALREDY EXISTS")

ins = '''
    insert into students values
    (5,"Vivek singh","B.tech","vivek@gmail.com")
'''
# conn.execute(ins)
# conn.commit()
# conn.close()

# conn.execute('''
#     insert into students values
#     (2,"Divya Singh","M.sc","divya@gmail.com"),
#     (3,"Pranav Gupta","B.tech","pranav@gmail.com")
# ''')

data = conn.execute("select * from students order by s_id")
for a in data:
    print(a)

data2 = conn.execute("select * from students group by s_class")
data3 = conn.execute("select * from students")
for a in data2:
    print(a)
conn.commit()
conn.close()