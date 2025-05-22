import psycopg2
class Database:
    def __init__(self,dbname,password,user,host='localhost',port=5432):
        self.conn = psycopg2.connect(
            dbname= dbname,
            password=password,
            user=user,
            host=host,
            port=port
        )
        self.cursor=self.conn.cursor()
        self.conn.autocommit=True

    def delete_data(self,table_name,column_name,data):
        self.cursor.execute(f"SELECT *FROM {table_name} WHERE {column_name}={data}")
        if self.cursor.fetchone():
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}={data}")
            self.conn.close()
            print("O'chirildi")
        else:
            print("BUnaqa malumot topilmadi")

    def select_from(self,table_name):
        self.cursor.execute(f"SELECT *FROM {table_name}")
        # print(self.cursor.execute)
        columns=[i[0] for i in self.cursor.description]
        lst=[]
        for i in columns:
            data = input(f"{i}ni kiriting!")

database1=Database(dbname="students",user="postgres",password="Sohib030")
database1.select_func('students')