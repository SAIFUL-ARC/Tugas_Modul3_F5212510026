import mysql.connector as mc
from tkinter import ttk
import customtkinter as ctk

class Buku(ctk.CTkFrame):
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
        self.label_form = ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold"))
        self.label_form.pack(pady=10)
        
        # Input Judul
        self.label_judul = ctk.CTkLabel(self.frame_kiri, text="Judul Buku", anchor="w")
        self.label_judul.pack(fill="x", padx=10, pady=(5,0))
        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(fill="x", padx=10, pady=5)
        
        # Input Penulis
        self.label_penulis = ctk.CTkLabel(self.frame_kiri, text="Penulis", anchor="w")
        self.label_penulis.pack(fill="x", padx=10, pady=(5,0))
        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(fill="x", padx=10, pady=5)
        
        # Input Tahun
        self.label_tahun = ctk.CTkLabel(self.frame_kiri, text="Tahun Terbit", anchor="w")
        self.label_tahun.pack(fill="x", padx=10, pady=(5,0))
        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)")
        self.entry_tahun.pack(fill="x", padx=10, pady=5)
        
        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=10, fill="x")
        
        # FRAME KANAN: TABEL DATA BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Judul Tabel
        self.label_tabel = ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold"))
        self.label_tabel.pack(pady=10)
        
        # Komponen Tabel (Treeview dari tkinter standar)
        kolom = ("ID", "Judul", "Penulis", "Tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        # Mengatur Header Tabel
        for col in kolom:
            self.tabel.heading(col, text=col)
            self.tabel.column(col, width=100) # Lebar default
        
        # Mengatur Lebar Kolom
        self.tabel.column("ID", width=40, anchor="center")
        self.tabel.column("Judul", width=150)
        self.tabel.column("Penulis", width=120)
        self.tabel.column("Tahun", width=60, anchor="center")
        
        self.tabel.pack(fill="both", expand=True, padx=10, pady=10)
        
# Panggil method untuk memuat data saat aplikasi pertama kali dibuka
# self.load_data()


app = ctk.CTk()
app.title("Aplikasi Manajemen Perpustakaan")
app.geometry("1080x600")
Buku(app)

Buku(app).pack(fill="both", expand=True) 
app.mainloop()