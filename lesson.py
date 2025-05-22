import psycopg2
db_info = {
    'dbname':'books',
    'user':'postgres',
    'port':5432,
    'password':'Sohib030'
}
conn = psycopg2.connect(**db_info)
cursor = conn.cursor()

#1-funksiya
# def drop_column(column):
#     try:
#         cursor.execute(f"ALTER TABLE books DROP COLUMN {column}")
#         conn.commit()
#         print(f"{column} tabili o'chirildi!")
#     except psycopg2.errors.UndefinedColumn:
#         print("Bunaqa tabil yuq!")
# drop_column("data")

# conn.close()


#2-funksiya
# def delete_data(column,value):
#     try:
#         cursor.execute(f"DELETE FROM books WHERE {column} = {value}")
#         conn.commit()
#         print(f"{row} bulgan qator uchirildi!")
#     except psycopg2.errors.UndefinedFunction:
#         print("notugri malumot kiritildi!")
# delete_data("name","Cinderella Man")
# conn.close()

#3
def drop_database(uchiriladigan_baza):
    try:
        cursor.execute(f"DROP DATABASE {uchiriladigan_baza}")
        conn.commit()
        print(f"{uchiriladigan_baza} baza uchirildi!")
    # except errors.InvalidCatalogName:
    #     print(f"{uchiriladigan_baza} nomili baza mavjud emas!")
              
drop_database("students")    


#4
# def update_data()


#5
# def rename_table(table_nomi):
#     try:
#         cursor.execute(f"ALTER TABLE books RENAME TO {table_nomi}")
#         conn.commit()
#         print(f"bazani nomi {table_nomi} ga uzgartirildi!")
#     except psycopg2.errors.UndefinedTable:
#         print("Xatolik!")

# rename_table("boooks")


#6
# def rename_column(column_nomi,yangi_nomi):
#     try:
#         cursor.execute(f"ALTER TABLE boooks RENAME COLUMN {column_nomi} TO {yangi_nomi} ")
#         conn.commit()
#         print(f"{column_nomi} nomli column {yangi_nomi} columnga uzgartirildi")
#     except psycopg2.errors.UndefinedColumn:
#         print(f"{column_nomi} xato kirotildi!")

# rename_column("data","sana")


# #7
# def change_type_column(baza_nomi,column_nomi,type_nomi):
#     try:
#         cursor.execute(f"ALTER TABLE {baza_nomi} ALTER COLUMN {column_nomi} TYPE {type_nomi}")
#         conn.commit()
#         print(f"{column_nomi} nomi ustun tipi {type_nomi} tipga uzgartirildi!")
#     except psycopg2.errors.UndefinedType:
#         print("type xato kiritildi!")

# change_type_column("boooks","id","VARCHAR(5)")