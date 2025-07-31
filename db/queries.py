CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        is_bought INTEGER DEFAULT 0
    )
"""

INSERT_PRODUCT = """
    INSERT INTO products (name) VALUES (?)
"""

SELECT_PRODUCTS = """
    SELECT id, name, is_bought FROM products
"""

UPDATE_PRODUCT = """
    UPDATE products SET is_bought = ? WHERE id = ?
"""

DELETE_PRODUCT = """
    DELETE FROM products WHERE id = ?
"""