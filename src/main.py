#!/usr/bin/python3

#from connect_and_run import mysql_connector

from connect_and_run import Mysql




# тут класс создать 
# - create_shop - will create "shop" table in mysql with fields: id, item, price
# - add_item - will add records to the "shop" table. Params: item, price
# - delete_item - will remove item from "shop" by name
# - delete_shop - will drop "shop" table



#localhost = Mysql("py_user", "py_pass", "py_db")

class Query(Mysql):


    def delete_item(self, table, condition):
        # Example: DELETE FROM table WHERE condition;
        delete_query = f"DELETE FROM {table} WHERE {condition};"
        self.execute_query(delete_query)

    def select_all(self, table):
        select_query = f"SELECT * FROM {table};"
        self.cursor.execute(select_query)

        myresult = self.cursor.fetchall()
        for x in myresult:
            print(x)

    def create_shop(self, table):
        create_query = f"CREATE TABLE IF NOT EXISTS {table} (id int, item varchar(255), price varchar(255));"
        self.execute_query(create_query)

    def delete_shop(self, table):
        delete_shop_query = f"DROP TABLE {table};"
        self.execute_query(delete_shop_query)

    def add_item(self, table):
        add_query = f"INSERT INTO {table} VALUES ('1', 'Tank', '1M$');"
        self.execute_query(add_query)

#create_shop = "CREATE TABLE IF NOT EXISTS shop (id int, item varchar(255), price varchar(255));"
#add_item = "INSERT INTO shop VALUES ('1', 'Tank', '1M$')"
#delete_item = "DELETE FROM shop WHERE id=1"
#delete_shop = "DROP TABLE shop"
#show_table = "SELECT * FROM shop"


host="localhost"
user="py_user"
password="py_pass"
database="py_db"

# Create an instance of MySQLConnector
#mysql_connector = Mysql(host, user, password, database)
#mysql_connector.connect()


create = Query(host, user, password, database)
#mysql_connector.connect()
create.connect()

create.create_shop("shop")
create.select_all("shop")
create.add_item("shop")
#create.delete_item("shop", "id=1") 
#create.delete_shop("shop")





#create = mysql_connector.execute_query(create_shop)
#results = mysql_connector.select_all(show_table)

#add = mysql_connector.execute_query(add_item)
#results = mysql_connector.select_all(show_table)

#delete_i = mysql_connector.execute_query(delete_item)
#results = mysql_connector.select_all(show_table)

#delete_s = mysql_connector.execute_query(delete_shop)
#results = mysql_connector.select_all(show_table)


