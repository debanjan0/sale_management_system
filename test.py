from datetime import date
import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com:3306",
    user="sql6683942",
    password="q5teqr1i3m",
    database="sql6683942")


mycursor = mydb.cursor()
mycursor2= mydb.cursor(buffered=True)
today = date.today()
d1 = today.strftime("%Y/%m/%d")

create_table_customer = """
CREATE TABLE IF NOT EXISTS customer(
cust_id integer primary key NOT NULL,
first_name varchar(30),
last_name varchar(30),
phone varchar(14),
email varchar(30),
address varchar(255));
"""

create_table_inventory = """
CREATE TABLE IF NOT EXISTS inventory(
item_id integer primary key NOT NULL,
item_name varchar(225) NOT NULL,
variant varchar(225),
stock integer NOT NULL,
price integer NOT NULL,
cost_price integer,
sku varchar(225));
"""

create_table_sale = """
CREATE TABLE IF NOT EXISTS sale(
sale_id integer integer primary key NOT NULL,
sale_date date NOT NULL,
cust_id integer NOT NULL,
payment_mode varchar(20),
total_bill integer NOT NULL,
FOREIGN KEY (cust_id) REFERENCES customer (cust_id));
"""

create_table_sale_details = """
CREATE TABLE IF NOT EXISTS sale_details(
sale_details_id integer primary key NOT NULL, 
sale_id integer NOT NULL,
item_id integer NOT NULL,
sku char(225) NOT NULL,
quantity integer NOT NULL,
FOREIGN KEY (item_id) REFERENCES inventory (item_id),
FOREIGN KEY (sale_id) REFERENCES sale (sale_id));
"""

create_table_sale_purchaces = """
CREATE TABLE IF NOT EXISTS sale_details(
purchaces_id integer primary key NOT NULL,
bill_date date NOT NULL, 
item_name varchar(225) NOT NULL,
bill_amount integer NOT NULL,
due integer NOT NULL,
gst char(3),
type varchar(225));
"""


def table_creation():
    mycursor.execute(create_table_customer)
    mycursor.execute(create_table_inventory)
    mycursor.execute(create_table_sale)
    mycursor.execute(create_table_sale_details)
    mycursor.execute(create_table_sale_purchaces)


def add_item():
    tempo_list = []
    for i in item_list:
        x = input("enter the " + i + " :- ")
        tempo_list.append(x)
    sql = "INSERT INTO item (name,price,stock) VALUES (%s, %s, %s)"
    mycursor.execute(sql, tuple(tempo_list))
    mydb.commit()


def add_sale():
    tempo_list = [str(d1)]
    for i in sale_list:
        x = input("enter the " + i + " :- ")
        tempo_list.append(x)
    sql = "INSERT INTO sale (sale_date,cust_id,mop) VALUES (%s, %s, %s)"
    mycursor2.execute(sql, tuple(tempo_list))
    mydb.commit()
    sql1 = "SELECT * FROM sale ORDER BY sale_id DESC"
    mycursor2.execute(sql1)
    myresult = mycursor2.fetchone()
    add_order_details(myresult[0])




















