import userdb_handler as handler

def main():
    
    # Instancio la clase UserDatabase
    # y le paso el nombre de la base de datos
    db = handler.UserDatabase(db_name="../dbs/mydb.db")

    # Se crea la base de datos
    db.create_table()

    # Se inserta un usuario y contraseña
    user_id = db.insert_user("lucas", "123")

    # Se visualiza toda la información de la tabla 'users'
    all_users = db.get_all_users()
    for user in all_users:
        print(f"ID: {user[0]}, Username: {user[1]}, Password: {user[2]}")

    # Busco un usuario por su nombre
    user = db.get_user_by_username("lucas")
    if user:
        print(f"Usuario encontrado: ID: {user[0]}, Username: {user[1]}, Password: {user[2]}")
    else:
        print("Usuario no encontrado")

if __name__ == "__main__":
    main()


