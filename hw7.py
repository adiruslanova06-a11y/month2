import sqlite3


def create_connection():
    conn = sqlite3.connect('store.db')
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def create_product(name, price, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
        (name, price, quantity)
    )
    conn.commit()
    conn.close()


def read_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


def update_product(product_id, new_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE products SET price = ? WHERE id = ?',
        (new_price, product_id)
    )
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()


# Пример использования:
if __name__ == "__main__":
    create_table()
    create_product("Laptop", 1200.50, 5)
    create_product("Mouse", 25.00, 50)

    print("Список товаров:")
    read_products()

    update_product(1, 1150.00)
    print("\nПосле обновления цены:")
    read_products()

    delete_product(2)
    print("\nПосле удаления товара:")
    read_products()




