# --- BAGIAN 1: IMPORT ---
import mysql.connector #Lengkapi import untuk library mysql.connector
from mysql.connector import Error# dan import Error dari mysql.connector
# --- LENGKAPI BAGIAN INI ---

#Saiful_F5212510026

class Database:
    def __init__(self):
        # --- BAGIAN 2: INISIALISASI DATA DIRI ---
        self.host = "localhost" # Isi self.host dengan "localhost"
        self.db_name = "perpustakaan" # Isi self.db_name dengan "perpustakaan"
        self.username = "root" # Isi self.username dengan "root"
        self.password = "" # Isi self.password dengan "" (string kosong)
        self.conn = None  # Isi self.conn dengan None
        # --- LENGKAPI BAGIAN INI ---

    def get_connection(self):
        # --- BAGIAN 3: PROSES KONEKSI (TRY) ---
        try :
            self.conn = mysql.connector.connect(
                host = self.host, 
                database = self.db_name,  
                user =self.username,
                password = self.password
            )

            if self.conn.is_connected() :
                return self.conn

        except Error as e :
            print (f"koneksi gagal, {e}")
            return None