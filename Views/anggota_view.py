import mysql.connector as mc
from tkinter import ttk
import customtkinter as ctk

class Anggota(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Mengatur Grid Frame (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=3) # Kiri (form input)
        self.grid_columnconfigure(1, weight=2) # Kanan (Tabel Data)
        self.grid_rowconfigure(0, weight=1)
        
        # FRAME KIRI: FORM INPUT DATA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Judul Form
        self.label_form = ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold"))
        self.label_form.pack(pady=10)
        
        # Input Anggota
        self.label_anggota = ctk.CTkLabel(self.frame_kiri, text="Nama Anggota", anchor="w")
        self.label_anggota.pack(fill="x", padx=10, pady=(5,0))
        self.entry_anggota = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_anggota.pack(fill="x", padx=10, pady=5)
        
        # Input Alamat
        self.label_alamat = ctk.CTkLabel(self.frame_kiri, text="Alamat", anchor="w")
        self.label_alamat.pack(fill="x", padx=10, pady=(5,0))
        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat")
        self.entry_alamat.pack(fill="x", padx=10, pady=5)
        
        # Tombol Aksi 1 (Simpan)
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=10, fill="x")

        # Tombol Aksi 2 (Update) - Variabel diubah agar tidak menimpa tombol 1
        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue")
        self.btn_update.pack(pady=20, padx=10, fill="x")
        
        # Tombol Aksi 3 (Hapus) - Variabel diubah agar tidak menimpa tombol sebelumnya
        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red")
        self.btn_hapus.pack(pady=20, padx=10, fill="x")

        # FRAME KANAN: TABEL DATA ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Judul Tabel
        self.label_tabel = ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold"))
        self.label_tabel.pack(pady=10)
        
        # Komponen Tabel (Treeview dari tkinter standar)
        kolom = ("ID Anggota", "Nama Anggota", "Alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        # Mengatur Header Tabel
        for col in kolom:
            self.tabel.heading(col, text=col)
        
        # Mengatur Lebar Kolom (Disesuaikan agar rapi seperti di gambar)
        self.tabel.column("ID Anggota", width=80, anchor="center")
        self.tabel.column("Nama Anggota", width=150)
        self.tabel.column("Alamat", width=200)
       
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)

        # Memuat data dummy agar tampilan sesuai gambar
        self.load_data()

    def load_data(self):
        # Data dummy sesuai gambar yang Anda lampirkan
        data_anggota = [
            ("1", "Abdi", "Jl.Lagurutu"),
            ("2", "Laode", "Perdos"),
            ("3", "Tama", "Silae"),
            ("4", "Adit", "Dayoada Pancing"),
            ("5", "Ipul", "Tondo")
        ]
        
        # Memasukkan data ke dalam tabel
        for item in data_anggota:
            self.tabel.insert("", "end", values=item)


# --- Bagian Utama Program ---
app = ctk.CTk()
app.title("Sistem Manajemen Perpustakaan - Data Anggota") # Judul disesuaikan dengan gambar
app.geometry("1080x600")

# Hanya buat satu instance frame Anggota, lalu tampilkan (pack)
anggota_frame = Anggota(app)
anggota_frame.pack(fill="both", expand=True) 

app.mainloop()