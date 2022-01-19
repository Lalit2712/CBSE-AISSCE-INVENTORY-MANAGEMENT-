# CODING
# INVENTORY MANAGEMENT
# About Project
# Inventory management is the practice of ordering, storing, tracking, and controlling inventory.
# Inventory management applies to every item a business uses to produce its products or services –
# From Raw Materials to Finished Goods.
# In other words,
# Inventory management covers every aspect of a business’s inventory.
# The project contains following modules:-
# 1. Product Management: This module is used to add, update and delete the products.
# 2. Purchase Management: This module is used to manage the purchase system.
# 3. Sales Management: This module is used to manage the sale of the products.
# 4. User Management: This module is used to add/delete the user/staff.
# 5. Database setup: This module is used to setup the database in the system for the first time.
# SOFTWARE SPECIFICATION:-
# Operating System : Windows 10
# Platform : Python IDLE 3.8.0
# Database : MySQL 8.0
#Languages : Python
# Note: For Python-MySQL connectivity, following data have been used:-
# Host- localhost, user- root, password- ‘lalit‘, database- stock


# MODULES NEED TO BE IMPORTED
# BUILT_IN
import os
import mysql.connector
import datetime
import random
import time
now = datetime.datetime.now()

# MAIN MENU OF PRODUCT MANAGEMENT


def product_mgmt():
    clrscr()
    while True:
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| PRODUCT DETAILS MANAGEMENT SYSTEM  |")
        print("\t\t\t\t\t|*********************************** |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE           |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| 1. | \t   Add New Product           |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| 2. | \t   List Product              |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| 3. | \t   Update Product            |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| 4. | \t   Delete Product            |")
        print("\t\t\t\t\t======================================")
        print("\t\t\t\t\t| 5. | \t   Back (Main Menu)          |")
        print("\t\t\t\t\t======================================")
        print("\n"*11)
        print("=" * 121)
        p = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        print("\n"*5)
        if p == 1:
            add_product()
        if p == 2:
            search_product()
        if p == 3:
            update_product()
        if p == 4:
            delete_product()
        if p == 5:
            break


# MAIN MENU OF PURCHASE MANAGEMENT
def purchase_mgmt():
    while True:
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| PRODUCT PURCHASE MANAGEMENT SYSTEM  |")
        print("\t\t\t\t\t|************************************ |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 1. | \t   ADD NEW ORDER DETAILS      |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 2. | \t   LIST ORDERS DETAILS        |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
        print("\t\t\t\t\t=======================================")
        print("\n"*12)
        print("=" * 121)
        o = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        print("\n"*5)
        if o == 1:
            add_order()
        if o == 2:
            clrscr()
            list_order()
        if o == 3:
            break


# MAIN MENU OF SALES MANAGEMENT
def sales_mgmt():
    while True:
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|   PRODUCT SALES MANAGEMENT SYSTEM   |")
        print("\t\t\t\t\t| *********************************** |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 1. | \t   ADD SALE ITEMS DETAILS     |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 2. | \t   LIST SALES DETAILS         |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
        print("\t\t\t\t\t=======================================")
        print("\n"*12)
        print("=" * 121)
        s = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        if s == 1:
            sale_product()
        if s == 2:
            clrscr()
            list_sale()
        if s == 3:
            break


# MAIN MENU OF USER MANAGEMENT
def user_mgmt():
    while True:
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|  EMPLOYEE DATA MANAGEMENT SYSTEM    |")
        print("\t\t\t\t\t| *********************************** |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 1. | \t   ADD USER DETAILS           |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 2. | \t   LIST USER DETAILS          |")
        print("\t\t\t\t\t=======================================")
        print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
        print("\t\t\t\t\t=======================================")
        print("\n"*12)
        print("=" * 121)
        u = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        print("=" * 121)
        if u == 1:
            add_user()
        if u == 2:
            list_user()
        if u == 3:
            break


# Note: For Python-MySQL connectivity, following data have been used:-
# Host- localhost, user- root, password- ‘ ‘, database- stock
# Database setup MANAGEMENT: This module is used to setup the database in the system for the first time.
def create_database():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456")
    mycursor = mydb.cursor()
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating DATABASE Stock **")
    print(("=")*121)
    sql = "CREATE DATABASE stock"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** DATABASE STOCK CREATED ** ")
    print(("=")*121)
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    print("\t\t\t\t\t\t** Creating PRODUCT table** ")
    print(("=")*121)
    sql = "CREATE TABLE if not exists product(pcode int(4) PRIMARY KEY,pname varchar(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30));"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** Product Table Created** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating ORDER table** ")
    print(("=")*121)
    sql = "CREATE TABLE if not exists orders(orderid int(4)PRIMARY KEY,orderdate DATE,pcode varchar(30) NOT NULL ,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30));"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** ORDER table created** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating SALES table** ")
    print(("=")*121)
    sql = "CREATE TABLE if not exists sales(salesid int(4) PRIMARY KEY,salesdate DATE,pcode varchar(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2));"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t** SALES table created** ")
    sql = "CREATE TABLE if not exists user (uid varchar(100) PRIMARY KEY,uname varchar(30) NOT NULL);"
    mycursor.execute(sql)
    print(("=")*121)
    print("\t\t\t\t\t\t** Creating USER Table** ")
    print(("=")*121)
    print("\t\t\t\t\t\t** USER table created** ")
    print("=" * 121)
    print("\t\t\t\t\tROLLING BACK TO PREVIOUS MENU AFTER SUCCESSFULL CREATION")
    print(("=")*121)
    time.sleep(5)
    print("\n"*5)


# TO LIST DATABASE TABLES PRESENT IN STOCK
def list_database():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "show tables;"
    print("=" * 121)
    print("=" * 121)
    print("\t\t\t\t\t===================================")
    print("\t\t\t\t\t|        DATABASE - STOCK         |")
    print("\t\t\t\t\t| ******************************* |")
    print("\t\t\t\t\t|           TABLES LIST           |")
    print("\t\t\t\t\t| ******************************* |")
    print("\t\t\t\t\t===================================")
    mycursor.execute(sql)
    for i in mycursor:
        print("\t\t\t\t\t|\t", i, "\t\t  |")
        print("\t\t\t\t       ", "-" * 35)
    print("="*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print("=" * 121)
    time.sleep(5)
    print("\n"*10)


# TO CREATE A NEW ORDER FOR THE TABLE ORDER
def add_order():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    sql = "INSERT INTO orders (orderid, orderdate, pcode,pprice, pqty, supplier, pcat) values(%s,%s,%s,%s,%s,%s,%s)"
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter product code :"))
    print(("=")*121)
    oid = now.year+now.month+now.day+now.hour+now.minute+now.second
    qty = int(input("\t\t\t\t\t\tEnter product quantity : "))
    print(("=")*121)
    price = float(input("\t\t\t\t\t\tEnter Product unit price: "))
    print(("=")*121)
    cat = input("\t\t\t\t\t\tEnter product category: ")
    print(("=")*121)
    supplier = input("\t\t\t\t\t\tEnter Supplier details: ")
    print(("=")*121)
    val = (oid, now, code, price, qty, supplier, cat)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t\t\t\t  ORDER SUCCESSFULLY CREATED WITH ORDER ID-->", oid)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO DISPLAY DETAILS OF THE ORDER ENTERED
def list_order():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from orders"
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  ORDERS DETAILS           **********************************************")
    print(("=")*121)
    print(("=")*121)
    print("-" * 121)
    print(" ORDER ID |\t  DATE      \t| PRODUCT CODE   |  PRICE  |   QUANTITY   |  \t SUPPLIER\t   |\t CATEGORY\t|")
    print("-" * 121)
    print(("=")*121)
    for i in mycursor:
        print("  ", i[0], "\t", i[1], "\t    ", i[2], "\t   ",
              i[3], "\t", i[4], "\t\t ", i[5], "\t\t   ", i[6])
    print("-" * 121)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# MAIN MENU FOR DATABASE MANAGEMENT SETUP
def db_mgmt():
    password = "lalit2712"
    print(("=")*121)
    passwd = input(
        "\t\t\t\tENTER PASSWORD TO GET ACCESS TO DATABASE ADMINISTRATION=")
    print(("=")*121)
    if passwd == password:
        while True:
            clrscr()
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t|   DATABASE ADMINISTRATION SYSTEM    |")
            print("\t\t\t\t\t| *********************************** |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t|S.NO| \t OPTIONS AVAILABLE            |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 1. | \t   DATABASE CREATION          |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 2. | \t  LIST DATABASE TABLES        |")
            print("\t\t\t\t\t=======================================")
            print("\t\t\t\t\t| 3. | \t   Back (Main Menu)           |")
            print("\t\t\t\t\t=======================================")
            print("\n"*12)
            print("=" * 121)
            p = int(input("\t\t\t\t\t\t Enter Your Choice :"))
            print("=" * 121)
            clrscr()
            if p == 1:
                create_database()
            if p == 2:
                list_database()
            if p == 3:
                break
    else:
        print("\t\t\t\t\tWRONG PASSWORD OR PASSWORD NOT ENTERED")
        print(("=")*121)
        time.sleep(5)
        return


# TO ADD A NEW PRODUCT DETAILS
# IN PRODUCT TABLE
def add_product():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)"
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter Product Code :"))
    print(("=")*121)
    search = "SELECT count(*) FROM product WHERE pcode=%s;"
    val = (code,)
    mycursor.execute(search, val)
    for x in mycursor:
        cnt = x[0]
    if cnt == 0:
        name = input("\t\t\t\t\t\tEnter Product Name :")
        print(("=")*121)
        qty = int(input("\t\t\t\t\t\tEnter Product Quantity :"))
        print(("=")*121)
        price = float(input("\t\t\t\t\t\tEnter Product Unit Price :"))
        print(("=")*121)
        cat = input("\t\t\t\t\t\tEnter Product Category :")
        print(("=")*121)
        val = (code, name, price, qty, cat)
        mycursor.execute(sql, val)
        mydb.commit()
        print("\t\t\t\t\t\tPRODUCT DETAILS SUCCESSFULLY ADDED")
        print("="*121)
        time.sleep(3)
        print("\n"*10)
    else:
        print("\t\t\t\t\t\tProduct Already Exists")
        print(("=")*121)
        print("\t\t\t\t\t\tROLLING BACK TO MAIN MENU----->")
        print(("=")*121)
        time.sleep(3)
        clrscr()


# TO UPDATE PRODUCT DETAILS
# MAINLY QUANTITY
# IN PRODUCT TABLE
def update_product():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter the Product Code :"))
    print(("=")*121)
    qty = int(input("\t\t\t\t\t\tEnter the quantity :"))
    print(("=")*121)
    sql = "UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
    val = (qty, code)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t\t\t\t\tProduct details updated")
    print(("=")*121)
    time.sleep(2)
    print("\n"*5)


# TO REMOVE COMPLETE PRODUCT DETAILS
# FROM PRODUCT TABLE
def delete_product():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    print(("=")*121)
    code = int(input("\t\t\t\t\t\tEnter the Product Code :"))
    print(("=")*121)
    sql = "DELETE FROM product WHERE pcode = %s;"
    val = (code,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(("=")*121)
    print("\t\t\t\t\t\t", mycursor.rowcount, "record(s) deleted")
    print(("=")*121)
    time.sleep(2)
    print("\n"*10)


# TO SEARCH PRODUCT DETAILS
# IN PRODUCT TABLE
def search_product():
    while True:
        print("=" * 121)
        print("|\t\t\t\t\t       OPTIONS AVAILABLE  \t\t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     1. List All Products \t\t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     2. List Products Code Wise  \t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     3. List Product Category Wise \t\t\t\t\t\t|")
        print(("=")*121)
        print("|\t\t\t\t\t     4. Back To Previous Menu \t\t\t\t\t\t\t|")
        print(("=")*121)
        s = int(input("\t\t\t\t\t\t Enter Your Choice :"))
        if s == 1:
            clrscr()
            list_product()
        if s == 2:
            print(("=")*121)
            code = int(input("\t\t\t\t\t\tEnter product code :"))
            clrscr()
            list_prcode(code)
        if s == 3:
            print(("=")*121)
            cat = input("\t\t\t\t\t\tEnter category :")
            clrscr()
            list_prcat(cat)
        if s == 4:
            clrscr()
            break


# TO LIST PRODUCT DETAILS
# IN PRODUCT TABLE
def list_product():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from product"
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  PRODUCT DETAILS           *********************************************")
    print("-" * 121)
    print("\t\t CODE |\t    NAME     \t\t\t| PRICE (Rs.) |\t      QUANTITY \t       CATEGORY ")
    print("-" * 121)

    for i in mycursor:
        print("\t\t", i[0], " |    ", i[1], "\t\t\t|",
              i[2], "\t|", "\t\t", i[3], "\t\t", i[4])
        print("-" * 121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO LIST PRODUCT DETAILS CODE WISE
# IN PRODUCT TABLE
def list_prcode(code):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * from product WHERE pcode=%s"
    val = (code,)
    mycursor.execute(sql, val)
    print(("=")*121)
    print(("=")*121)
    print("--------------------------------------\t\t  PRODUCT DETAILS           ---------------------------------------------")
    print("-" * 121)
    print("\t\t CODE |\t\t  NAME         \t\t| PRICE |\t      QUANTITY \t       CATEGORY ")
    print("-" * 121)
    for i in mycursor:
        print("\t\t", i[0], " |", " \t", i[1], " \t\t|",
              i[2], "\t|", "\t\t", i[3], "\t\t", i[4])
        print("-" * 121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO ADD DETAILS OF THE SALE PRODUCTS
# IN SALE TABLE
def sale_product():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    print(("=")*121)
    pcode = input("\t\t\t\t\t\tEnter product code: ")
    print(("=")*121)
    sql = "SELECT count(*) from product WHERE pcode=%s;"
    val = (pcode,)
    mycursor.execute(sql, val)
    for x in mycursor:
        cnt = x[0]
    if cnt != 0:
        sql = "SELECT * from product WHERE pcode=%s;"
        val = (pcode,)
        mycursor.execute(sql, val)
        for x in mycursor:
            print("\t\t\t\tDETAILS OF PRODUCT WITH PRODUCT CODE",
                  pcode, "ARE AS FOLLOWS-->")
            print(("=")*121)
            print(("-")*121)
            print("\t\t\t\t\t\tPRODUCT CODE =", x[0])
            print(("-")*121)
            print("\t\t\t\t\t\tPRODUCT NAME =", x[1])
            print(("-")*121)
            print("\t\t\t\t\t\tPRODUCT PRICE =", "Rs.", x[2])
            print(("-")*121)
            print("\t\t\t\t\t\tQUANTITY IN HAND=", x[3])
            print(("-")*121)
            print("\t\t\t\t\t\tPRODUCT CATEGORY=", x[4])
            print(("-")*121)
            price = int(x[2])
            pqty = int(x[3])
            print(("=")*121)
            qty = int(input("\t\t\t\t\t\tEnter No. Of Quantity To Sell :"))
            if qty <= pqty:
                total = qty * price
                print(("=")*121)
                print("\t\t\t\t\t\tCollect Rs. ", total)
                print(("=")*121)
                sid = random.randint(1000, 99999)
                print("\t\t\t\t\tSALES ORDER CREATED SUCCESSFULLY WITH SALES ID=", sid)
                sql = "INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                val = (sid, datetime.datetime.now(), pcode, price, qty, total)
                mycursor.execute(sql, val)
                sql = "UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                val = (qty, pcode)
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                print(("=")*121)
                print("\t\t\t\t\t\tQUANTITY NOT AVAILABLE")
                print(("=")*121)
                print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
                print(("=")*121)
                time.sleep(5)
                clrscr()
                return
        else:
            print(("=")*121)
            print("\t\t\t\t\t\tTHANK YOU FOR SHOPPING WITH US.")
            print(("=")*121)
            print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
            print(("=")*121)
            time.sleep(5)
            clrscr()


# TO LIST DETAILS OF THE SALE PRODUCTS
# FROM SALE TABLES
def list_sale():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM sales"
    mycursor.execute(sql)
    print(("=")*121)
    print(("=")*121)
    print("***************************************\t\t  SALES DETAILS         *************************************************")
    print(("=")*121)
    print(("=")*121)
    print("-" * 121)
    print("  SALES ID  |\t   DATE       \t|   PRODUCT CODE    |    PRICE (Rs.)    |    QUANTITY    |  \t  TOTAL PRICE (Rs.)\t|")
    print("-" * 121)
    print(("=")*121)
    for x in mycursor:
        print("  ", x[0], "\t", x[1], "\t\t ", x[2],
              "\t\t", x[3], "\t\t\t", x[4], "\t\t   ", x[5])
        print("-"*121)
    print("-" * 121)
    print(("=")*121)
    print(("=")*121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print(("=")*121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO LIST PRODUCT DETAILS
# FROM TABLE PRODUCT
def list_prcat(cat):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    print(cat)
    sql = "SELECT * from product WHERE pcat =%s"
    val = (cat,)
    mycursor.execute(sql, val)
    clrscr()
    print(("=")*121)
    print(("=")*121)
    print("--------------------------------------\t\t  PRODUCT DETAILS           ---------------------------------------------")
    print("-" * 121)
    print("\t\t CODE |\t\t  NAME         \t\t| PRICE |\t      QUANTITY \t       CATEGORY ")
    print("-" * 121)
    for i in mycursor:
        print("\t\t", i[0], " |", " \t", i[1], " \t\t|",
              i[2], "\t|", "\t\t", i[3], "\t\t", i[4])
        print("-" * 121)
    print(("=")*121)
    time.sleep(5)
    clrscr()


# TO ADD DETAILS OF ANY NEW USER
# TABLE- USER
def add_user():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    passwd = "lalit2712"
    print("=" * 121)
    uid = input("\t\t\t\t\t\tENTER EMAIL ID OF EMPLOYEE :")
    print("=" * 121)
    name = input("\t\t\t\t\t\tENTER NAME OF EMPLOYEE :")
    print("=" * 121)
    password = input("\t\t\t\t\tENTER PASSWORD TO ENCRYPT EMPLOYEE DETAILS :")
    print("=" * 121)
    if passwd == password:
        print("\t\t\t\t\t\tSTORING AND ENCRYPTING DATA")
        sql = "INSERT INTO user values (%s,%s);"
        val = (uid, name)
        mycursor.execute(sql, val)
        mydb.commit()
        print(("=")*121)
        print("\t\t\t\t\t\t", mycursor.rowcount, "USER DETAILS ENCRYPTED")
        print("=" * 121)
        print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
        print("=" * 121)
        time.sleep(5)
        clrscr()
    else:
        print("=" * 121)
        print("\t\t\t\t\t\tWRONG PASSWORD OR PASSWORD NOT ENTERED")
        print("=" * 121)
        print("\t\t\t\t\t\tUSER DETAILS NOT ENCRYPTED")
        print("=" * 121)
        print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
        print("=" * 121)
        time.sleep(5)
        clrscr()


# LIST ALL THE DETAILS OF THE USER
# FROM TABLE USER
def list_user():
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="123456", database="stock")
    mycursor = mydb.cursor()
    sql = "SELECT uid, uname from user"
    mycursor.execute(sql)
    clrscr()
    print(("=")*121)
    print(("=")*121)
    print("--------------------------------------\t\t     USER DETAILS           ---------------------------------------------")
    print("-" * 121)
    print("|\t\t\tEMAIL ID\t\t\t\t|\t\tEMPLOYEE NAME\t\t\t|")
    print("-" * 121)
    for i in mycursor:
        print("|\t\t\t", i[0], "\t\t|", "\t\t", i[1], "\t\t\t|")
        print("-" * 121)
    print("=" * 121)
    print("\n"*2)
    print("=" * 121)
    print("\t\t\t\t\t\tROLLING BACK TO PREVIOUS MENU")
    print("=" * 121)
    time.sleep(5)
    clrscr()


# CLEAR THE SCREEN
def clrscr():
    print("\n"*50)


# MAIN FUNCTION
while True:
    clrscr()
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|                   INVENTORY MANAGEMENT SYSTEM              |")
    print("\t\t\t\t|                *********************************           |")
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|S.NO|               AVAILABLE CHOICES                       |")
    print("\t\t\t\t==============================================================")
    # IT REFERS TO DETAILS OF PRODUCT WE ARE CURRENTLY HAVING.
    print("\t\t\t\t|  1.| PRODUCT DETAILS MANAGEMENT                            |")
    print("\t\t\t\t==============================================================")
    # IT REFERS TO DETAILS OF TRANSACTIONS DONE TO PURCHASE PRODUCTS DROM COMPANY.
    print("\t\t\t\t|  2.| PRODUCT PURCHASE MANAGEMENT                           |")
    print("\t\t\t\t==============================================================")
    # IT REFERS TO DETAILS OF TRANSACTIONS IN WHICH PRODUCTS ARE SOLD TO CONSUMERS.
    print("\t\t\t\t|  3.| PRODUCT SALES MANAGEMENT                              |")
    print("\t\t\t\t==============================================================")
    # IT REFERS TO THE MEMBERS OF THE INVENTORY
    print("\t\t\t\t|  4.| EMPLOYEE USER MANAGEMENT                              |")
    print("\t\t\t\t==============================================================")
    # IT REFERS TO THE MAIN FUNCTIONING DATABASE IN WHICH ALL DETAILS ARE STORED.
    print("\t\t\t\t|  5.| DATABASE ADMINISTRATION                               |")
    print("\t\t\t\t==============================================================")
    print("\t\t\t\t|  6.| EXIT                                                  |")
    print("\t\t\t\t==============================================================")
    print(("=")*121)
    print("    |NOTE| IF YOU ARE USING THIS PROGRAM FOR FIRST TIME THEN PLEASE FIRSTLY SELECT OPTION '5' 'DATABASE ADMINISTRATION'")
    print(("=")*121)
    print("\n"*6)
    print("=" * 121)
    n = int(input("\t\t\t\t\t\tEnter your choice :"))
    print("=" * 121)
    if n == 1:
        clrscr()
        product_mgmt()
    if n == 2:
        clrscr()
        os.system('cls')
        purchase_mgmt()
    if n == 3:
        clrscr()
        sales_mgmt()
    if n == 4:
        clrscr()
        user_mgmt()
    if n == 5:
        clrscr()
        db_mgmt()
    if n == 6:
        clrscr()
        print(
            " \t\t                          THANK YOU FOR USING INVENTORY MANAGEMENT SYSTEM")
        print(" \t\t                              PROGRAMMED & DESIGNED BY ---> ")
        print(" \t\t                            LALIT SHROTRIYA  ")
        print(" \t\t                               XII-B1      ")
        print(" \t\t                            ST. MARY'S CONVENT SR. SEC. SCHOOL ")
        print('\n'*2)
        print(
            " \t\t                            CBSE BOARD 2019-20 COMPUTER SCIENCE PROJECT")
        print('\n'*2)
        print(" \t\t                                     SUPERVISED BY-")
        print("\t\t                                    MAM BINDU VASUDEVAN")
        print('\n'*5)
        break
# PROGRAM OVER.......
