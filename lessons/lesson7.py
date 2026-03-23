import sqlite3

# Альбом из А4 листов
connect = sqlite3.connect("users.db")

# Рука у которой есть карандаш
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT 
    )
''')
connect.commit()


# CRUD - Create - Read - Update - Delete


def add_user(name: str, age: int, hobby="None"):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"{name} - Добавили")


# add_user("user1", 33, "Спать")
# add_user("user2", 33, "Спать")
# add_user("user3", 33, "Спать")
# add_user("user4", 33, "Спать")


def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

    for i in users:
        print(f"NAME: {i[0]} AGE: {i[1]} HOBBY: {i[2]}")

# get_all_users()

def update_user(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
        (name, id)
    )
    connect.commit()
    print("Обновлен пользователь!!")

update_user("Arzybek", 4)


def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('Пользователь удален!!')

# delete_user(3)



import sqlite3

# A4
connect = sqlite3.connect("users.db")
# рука с ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


#CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    connect.commit()
    print('пользователь добавлен!!')

# create_user("Arzybek", 27, "Аниме-Манга-Манхва")
