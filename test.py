from datetime import date
import mysql.connector
from tabulate import tabulate
import random

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com:3306",
    user="sql6683942",
    password="q5teqr1i3m",
    database="sql6683942")


mycursor = mydb.cursor()
mycursor2= mydb.cursor(buffered=True)
d1 = date.today().strftime("%Y/%m/%d")

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

class customer:
    def __init__(self, first_name, last_name, phone, email, address):
        self.cust_id = random.randint(10000, 1000000)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

    def add_customer(self):
        sql = "INSERT INTO customer (cust_id, first_name,last_name,phone,email,address) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.cust_id, self.first_name, self.last_name, self.phone, self.email, self.address))
        mydb.commit()

class inventory:
    def __init__(self, item_name, variant, stock, price, cost_price, sku):
        self.item_id = random.randint(10000, 1000000)
        self.item_name = item_name
        self.variant = variant
        self.stock = stock
        self.price = price
        self.cost_price = cost_price
        self.sku = sku

    def add_item(self):
        sql = "INSERT INTO inventory (item_id,item_name,variant,stock,price,cost_price,sku) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.item_id, self.item_name, self.variant, self.stock, self.price, self.cost_price, self.sku))
        mydb.commit()

    def update_stock(self):
        sql = "UPDATE inventory SET stock = %s WHERE item_id = %s"
        mycursor.execute(sql, (self.stock, self.item_id))
        mydb.commit()
    
    def update_price(self):
        sql = "UPDATE inventory SET price = %s WHERE item_id = %s"
        mycursor.execute(sql, (self.price, self.item_id))
        mydb.commit()

    def update_cost_price(self):
        sql = "UPDATE inventory SET cost_price = %s WHERE item_id = %s"
        mycursor.execute(sql, (self.cost_price, self.item_id))
        mydb.commit()

    def update_sku(self):
        sql = "UPDATE inventory SET sku = %s WHERE item_id = %s"
        mycursor.execute(sql, (self.sku, self.item_id))
        mydb.commit()

class sale:
    def __init__(self, sale_date, cust_id, payment_mode, total_bill, items_qty):
        self.sale_id = random.randint(10000, 1000000)
        self.sale_details_id = random.randint(10000, 1000000)
        self.sale_date = sale_date
        self.cust_id = cust_id
        self.payment_mode = payment_mode
        self.total_bill = total_bill
        self.items_qty = items_qty

    def add_sale(self):
        sql = "INSERT INTO sale (sale_id,sale_date,cust_id,payment_mode,total_bill) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.sale_id, self.sale_date, self.cust_id, self.payment_mode, self.total_bill))
        mydb.commit()

    def add_sales_details(self):
        for i in self.items_qty:
            sql = "INSERT INTO sale_details (sale_details_id,sale_id,item_id,quantity) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql, (self.sale_details_id, self.sale_id, i, self.items_qty[i]))
            mydb.commit()
            self.sale_details_id += 1

class expense:
    def __init__(self, bill_date, item_name, bill_amount, due, gst, type):
        self.purchaces_id = random.randint(10000, 1000000)
        self.bill_date = bill_date
        self.item_name = item_name
        self.bill_amount = bill_amount
        self.due = due
        self.gst = gst
        self.type = type

    def add_purchaces(self):
        sql = "INSERT INTO sale_purchaces (purchaces_id,bill_date,item_name,bill_amount,due,gst,type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.purchaces_id, self.bill_date, self.item_name, self.bill_amount, self.due, self.gst, self.type))
        mydb.commit()

    








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




















