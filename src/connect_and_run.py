#!/usr/bin/python3

import mysql.connector


class Mysql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None



    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
        else:
            print("Connection failed.")



    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

        print("Query executed successfully")


   # def select_all(self, select_query):
   #     self.select_query = select_query
   #     self.cursor.execute(select_query)
   #
   #     myresult = self.cursor.fetchall()
   #     for x in myresult:
   #         print(x)



host="localhost"
user="py_user"
password="py_pass"
database="py_db"

# Create an instance of MySQLConnector

mysql_connector = Mysql(host, user, password, database)

mysql_connector.connect()

#create_shop = "CREATE TABLE shop (id int, item varchar(255), price varchar(255));"
#add_item = "INSERT INTO shop VALUES ('1', 'Tank', '1M$')"
#delete_item = "DELETE FROM shop WHERE product_id=1"
#delete_shop = "DROP TABLE shop"
#show_table = "SELECT * FROM shop"
#
#
##mysql_connector.execute_query(create_shop)
#add = mysql_connector.execute_query(add_item)
#
#
#
##mysql_connector.execute_query(show_table)
#
#results = mysql_connector.select_all(show_table)




             



