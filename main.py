import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_products(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES(?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_products_quantity(conn, id, new_quantity):
    sql = '''UPDATE products SET new_quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_quantity, id))
        conn.commit()
    except Error as e:
        print(e)


def update_products_price(conn, id, new_price):
    sql = '''UPDATE products SET new_price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_price, id))
        conn.commit()
    except Error as e:
        print(e)


def delete_products(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)
database = r'akbar_hw8.db'


def select_products(conn):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)


def select_products_by_price_quantity(conn):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products WHERE price <= 100 and quantity >= 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Selected products by price and quantity:')

        for row in rows:
            print(row)

    except Error as e:
        print(e)


def find_by_product_title(conn):
    try:
        sql = '''select * from products  where product_title LIKE 'beet';'''
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        for row in rows:
            print(row)

        c.close()
    except Error as e:
        print(e)

sql_create_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
);
'''


connection = create_connection(database)
if connection is not None:
    print('Connected successfully!')
    # create_table(connection, sql_create_table)
    # create_products(connection, ('beef', 500, 4))
    # create_products(connection, ('Sausage', 120, 10))
    # create_products(connection, ('beet ', 60, 15))
    # create_products(connection, ('salmon', 300, 5))
    # create_products(connection, ('avocado', 100, 30))
    # create_products(connection, ('apple', 40, 20))
    # create_products(connection, ('potato', 30, 25))
    # create_products(connection, ('lentil', 90, 20))
    # create_products(connection, ('butter', 55, 9))
    # create_products(connection, ('cheese', 120, 9))
    # create_products(connection, ('milk', 60, 7))
    # create_products(connection, ('eggs ', 12, 20))
    # create_products(connection, ('cookie ', 100, 10))
    # create_products(connection, ('coffee', 120, 5))
    # create_products(connection, ('cream', 150, 10))
    update_products_price(connection, 2, 20)
    select_products(connection)
    select_products_by_price_quantity(connection)
    delete_products(connection, 4)
    find_by_product_title(connection)