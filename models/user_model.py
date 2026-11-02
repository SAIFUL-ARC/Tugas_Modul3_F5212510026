#Saiful_f5212510026
import hashlib
from config.database import Database
from mysql.connector import Error


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Pengubah plain text password menjadi hash SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)

            # Parameterized Query untuk mencegah SQL Injection
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None

    def register_user(self, username, password, role="anggota"):
        # Mendaftarkan user baru; password otomatis di-hash SHA-256 sebelum disimpan
        if not username or not password:
            return False

        # Sesuai kolom role pada tabel users: ENUM('admin', 'anggota')
        if role not in ("admin", "anggota"):
            return False

        if self.conn:
            try:
                cursor = self.conn.cursor()
                password_hash = self.hash_password(password)

                # Parameterized Query untuk mencegah SQL Injection
                query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
                cursor.execute(query, (username, password_hash, role))
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                # Contoh kegagalan: username sudah dipakai (kolom username bersifat UNIQUE)
                print(f"Gagal mendaftarkan user: {e}")
                return False
        return False