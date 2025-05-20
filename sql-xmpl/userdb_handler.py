import sqlite3
from typing import List, Tuple, Optional

class UserDatabase:
    def __init__(self, db_name: str = "users.db"):
        """Inicializa la conexión a la base de datos."""
        self.db_name = db_name
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Establece la conexión a la base de datos."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.conn:
            self.conn.commit()
            self.conn.close()
    
    def create_table(self):
        """Crea la tabla users si no existe."""
        self.connect()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        self.close()
    
    def insert_user(self, username: str, password: str) -> int:
        """
        Inserta un nuevo usuario en la tabla.
        
        Args:
            username: Nombre de usuario
            password: Contraseña del usuario
            
        Returns:
            El ID del usuario insertado
        """
        self.connect()
        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            user_id = self.cursor.lastrowid
            self.conn.commit()
            return user_id
        except sqlite3.IntegrityError:
            print(f"Error: El usuario {username} ya existe")
            return -1
        finally:
            self.close()
    
    def get_all_users(self) -> List[Tuple]:
        """
        Obtiene todos los usuarios de la base de datos.
        
        Returns:
            Lista de tuplas con los datos de los usuarios
        """
        self.connect()
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.close()
        return users
    
    def get_user_by_id(self, user_id: int) -> Optional[Tuple]:
        """
        Busca un usuario por su ID.
        
        Args:
            user_id: ID del usuario a buscar
            
        Returns:
            Tupla con los datos del usuario o None si no existe
        """
        self.connect()
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = self.cursor.fetchone()
        self.close()
        return user
    
    def get_user_by_username(self, username: str) -> Optional[Tuple]:
        """
        Busca un usuario por su nombre de usuario.
        
        Args:
            username: Nombre del usuario a buscar
            
        Returns:
            Tupla con los datos del usuario o None si no existe
        """
        self.connect()
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchone()
        self.close()
        return user
    
    def delete_user_by_id(self, user_id: int) -> bool:
        """
        Elimina un usuario por su ID.
        
        Args:
            user_id: ID del usuario a eliminar
            
        Returns:
            True si se eliminó correctamente, False si no
        """
        self.connect()
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        rows_affected = self.cursor.rowcount
        self.conn.commit()
        self.close()
        return rows_affected > 0
    
    def delete_user_by_username(self, username: str) -> bool:
        """
        Elimina un usuario por su nombre de usuario.
        
        Args:
            username: Nombre del usuario a eliminar
            
        Returns:
            True si se eliminó correctamente, False si no
        """
        self.connect()
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        rows_affected = self.cursor.rowcount
        self.conn.commit()
        self.close()
        return rows_affected > 0
    
    def update_password(self, username: str, new_password: str) -> bool:
        """
        Actualiza la contraseña de un usuario.
        
        Args:
            username: Nombre del usuario
            new_password: Nueva contraseña
            
        Returns:
            True si se actualizó correctamente, False si no
        """
        self.connect()
        self.cursor.execute(
            "UPDATE users SET password = ? WHERE username = ?",
            (new_password, username)
        )
        rows_affected = self.cursor.rowcount
        self.conn.commit()
        self.close()
        return rows_affected > 0