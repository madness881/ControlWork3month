import sqlite3
from db import queries
from config import db_path


def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    conn.commit()
    conn.close()


def get_products():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_PRODUCTS)
    products = cursor.fetchall()
    conn.close()
    return products


def add_product(name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_PRODUCT, (name,))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return product_id


def update_product(product_id, is_bought):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_PRODUCT, (int(is_bought), product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_PRODUCT, (product_id,))
    conn.commit()
    conn.close()