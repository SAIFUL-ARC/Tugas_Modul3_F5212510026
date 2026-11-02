# anggota_model.py
from config.database import Database
from mysql.connector import Error

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name} ORDER BY id_anggota"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
                val = (nama, alamat)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                print(f"Gagal menyimpan data: {e}")
                return False
        return False

    def update_anggota(self, id_anggota, nama, alamat):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"UPDATE {self.table_name} SET nama = %s, alamat = %s WHERE id_anggota = %s"
                val = (nama, alamat, id_anggota)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                print(f"Gagal mengubah data: {e}")
                return False
        return False

    def delete_anggota(self, id_anggota):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"DELETE FROM {self.table_name} WHERE id_anggota = %s"
                cursor.execute(query, (id_anggota,))
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                print(f"Gagal menghapus data: {e}")
                return False
        return False