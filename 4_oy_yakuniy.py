# import psycopg2

# class Database:
#     def __init__(self,dbname,user,password,host='localhost',port=5432):
#         self.conn = psycopg2.coonect(
#             dbname=dbname,
#             user=user,
#             password=password,
#             host=host,
#             port=port
#         )
#         self.cursor=self.conn.cursor()
#         self.conn.autocommit = True

#     def add_table(self,table_name):
#         a=True
#         while a:
#             self.cursor.execute(f"select *from {table_name} limit 0")
#             columns = [i[0] for i in self.cursor.description]
#             new_data=[]
#             add_column=[]
#             if len(columns)>2:
#                 for i in columns[1:]:
#                     data=input("{i} kiriting:")
#                     if data:
#                         add_column.append(i)
#                         new_data.append(data)
#                 columns = ", ".join(added_columns)
#                 placeholders = ", ".join(["%s"] * len(new_data))
#                 self.cursor.execute(f"insert into {table_name}({columns}) values ({placeholders})", new_data)
#                 self.conn.commit()
#             else:
#                 i = self.cursor.description[1][0]
#                 data = input(f"Enter {i} here:\t")
#                 self.cursor.execute(f"insert into {table_name}({i}) values ('{data}')")
#             try:
#                 a = eval(input("Want to continue?(True/False?:\t"))
#             except NameError:
#                 pass

#     def view_data(self, table_name, quantity=None):
#         if not quantity:
#             self.cursor.execute(f"select * from {table_name}")
#         else:
#             self.cursor.execute(f"select * from {table_name} limit {quantity}")

#         for row in self.cursor.fetchall():
#             print(row)


#     def update_table(self, table_name):
#         changing_column = input("Which column do you want to update?:\t")
#         new_data = input("What do you want it to be?:\t")
#         conditional_column = input("What is the column with conditions?:\t")
#         try:
#             if conditional_column:
#                 cond_data = input("What is the data of that column?:\t")

#                 self.cursor.execute(f"update {table_name} set {changing_column} = '{new_data}' where {conditional_column} = '{cond_data}'")
#             else:
#                 self.cursor.execute(f"update {table_name} set {changing_column} = '{new_data}'")

#         except psycopg2.errors.UndefinedTable:
#             print("Bunday table yuq")
#         except psycopg2.errors.UndefinedColumn:
#             print("Bunday column yuq")
#         except psycopg2.errors.InvalidTextRepresentation:
#             print("Bu column bunday type dagi infoni qabul qilmaydi.")


#     def delete_rows(self, table_name):
#         cond_column = input("Enter the conditional column:\t")
#         cond_data = input("Enter the cond data:\t")
#         try:
#             if cond_column and cond_data:
#                 self.cursor.execute(f"delete from {table_name} where {cond_column} = '{cond_data}'")
#             else:
#                 self.cursor.execute((f"delete from {table_name}"))
#         except psycopg2.errors.UndefinedTable:
#             print("Bunday nomli jadval yuq")
#         except psycopg2.errors.UndefinedColumn:
#             print("Bundan nomli column yuq")


# database = Database('shopping', 'postgres', 18122006)

# #database.delete_rows('category')





#  CREATE TABLE customers (
#      id SERIAL PRIMARY KEY,
#      name VARCHAR(50),
#      city VARCHAR(50)
#  );

#  CREATE TABLE orders (
#      id SERIAL PRIMARY KEY,
#      customer_id INT REFERENCES customers(id),
#      order_date DATE,
#      amount NUMERIC
#  );

#  CREATE TABLE products (
#      id SERIAL PRIMARY KEY,
#      name VARCHAR(50),
#      price NUMERIC
#  );

#  CREATE TABLE order_items (
#      id SERIAL PRIMARY KEY,
#      order_id INT REFERENCES orders(id),
#      product_id INT REFERENCES products(id),
#      quantity INT
#  );

#  CREATE TABLE employees (
#      id SERIAL PRIMARY KEY,
#      name VARCHAR(50),
#      department_id INT
#  );

#  CREATE TABLE departments (
#      id SERIAL PRIMARY KEY,
#      name VARCHAR(50)
#  );
#  insert into customers(name,city) values('Ali','qashqadaryo'),('Vali','surxondaryo'),('Soli','sirdaryo'),('Karim','jizzax'),('Shavkat','toshkent');
#  insert into orders(customer_id, order_date, amount) values(1,'2025-05-18',256000),(2,'2025-05-15',221000),(3,'2025-05-10',927000),(2,'2025-02-18',188000);
#  insert into products(name, price) values('telefon',2_200),('kompyuter',9_200),('BMW',812_700);
#  insert into order_items(order_id,product_id,quantity) values(1,1,2),(2,2,3),(3,2,4);
#  insert into employees(name,department_id) values('Kamil',1),('Bahodir',2),('Jalil',3),('Komil',2),('Bekzod',3),('Rustam',1);
#  insert into departments(name) values('Ish_boshqaruvchi'),('Sotuvchi'),('Kassir');

# select customers.name, customers.city from customers 
# left join orders on customers.id = orders.customer_id
# where orders.customer_id is null;
