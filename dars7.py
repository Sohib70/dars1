# #1
# import psycopg2
#
# class Database:
#     def __init__(self,dbname,password,user,host='localhost',port=5432):
#         self.conn = psycopg2.connect(
#             dbname = dbname,
#             password = password,
#             user = user,
#             host = host,
#             port = port
#         )
#         self.cursor = self.conn.cursor()
#         self.conn.autocommit = True
#
#     def insert_func(self,table_name):
#         self.cursor.execute(f"SELECT *FROM {table_name}")
#         columns = [i[0] for i in self.cursor.description]
#         values = []
#         for i in columns[1:]:
#             data = input(f"{i}ni kiriting: ")
#             if data=="":
#                 values.append(None)
#             else:
#                 values.append(data)
#
#         columns_str = ",".join(columns[1:])
#         self.cursor.execute(f"INSERT INTO {table_name} ({columns_str}) VAlUES{tuple(values)}")
#
#
# database1 = Database(dbname="students",user="postgres",password="Sohib030")
# database1.insert_func("students")
#
#
# #2
#     def yangi_ustun(self,jadval_nomi,ustun_nomi,ustun_type):
#         self.cursor.execute(f"ALTER TABLE {jadval_nomi} ADD COLUMN {ustun_nomi} {ustun_type} ")
#
# database2 = Database(dbname="students",user="postgres",password="Sohib030")
# database2.yangi_ustun("students","yunalishi","VARCHAR(15)")
#
#
# #3
#     def ustunni_uchirish(self,jadval_nomi,ustun_nomi):
#         self.cursor.execute(f"ALTER TABLE {jadval_nomi} DROP COLUMN {ustun_nomi}")
#
# database3 = Database(dbname="students",user="postgres",password="Sohib030")
# database3.ustunni_uchirish("students","yunalishi")
#
#
# # 4
#     def table_nomini_uzgartirish(self,jadval_nomi,table_nomi):
#         self.cursor.execute(f"ALTER TABLE {jadval_nomi} RENAME TO {table_nomi}")
#         print(f"table nomi {table_nomi} ga uzgartirildi!")
#
# database4 = Database(dbname="students",user="postgres",password="Sohib030")
# database4.table_nomini_uzgartirish("students","talabalar")
#
#
# #5
#     def turini_uzgartirish(self,jadval_nomi,ustun_nomi,yangi_tur):
#         self.cursor.execute(f"ALTER TABLE {jadval_nomi} ALTER COLUMN {ustun_nomi} TYPE {yangi_tur}")
#         print(f"{ustun_nomi} ustun turi {yangi_tur} ga uzgartirildi!")
#
# database5 = Database(dbname="students",user="postgres",password="Sohib030")
# database5.turini_uzgartirish("talabalar","score","VARCHAR(5)")
#
#
# #6
#     def database_nomini_uzgartirish(self,database_nomi,yangi_database_nomi):
#         self.cursor.execute(f"ALTER DATABASE {database_nomi} RENAME TO {yangi_database_nomi}")
#         print(f"Database nomi {yangi_database_nomi}ga uzgartirildi!")
#
# database6=Database(dbname="books",user="postgres",password="Sohib030")
# database6.database_nomini_uzgartirish("students","uquvchilar")




# CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL
# );
#
# CREATE TABLE students_profiles(
#     id SERIAL PRIMARY KEY,
#     students_id INT UNIQUE,
#     address VARCHAR(255),
#     phone VARCHAR(15),
#     FOREIGN KEY (students_id) REFERENCES students(id) ON DELETE CASCADE
# );