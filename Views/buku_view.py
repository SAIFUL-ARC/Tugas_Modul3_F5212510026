import tkinter as tk
from tkinter import ttk

class BukuView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Manajemen Perpustakaan")
        self.geometry("700x600")
        
        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=1) # Kolom Kanan (Tabel lebih lebar)
        self.grid_rowconfigure(0, weight=1)
        
        # ===== FRAME KIRI: FORMULIR INPUT =====
        from_kiri = tk.Frame(self)
        from_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        tk.Label(from_kiri, text="Form Data Buku", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Komponen Input
        tk.Label(from_kiri, text="Judul Buku", anchor="w").pack(fill="x")
        self.entry_judul = tk.Entry(from_kiri, font=("Arial", 12), width=30)
        self.entry_judul.pack(pady=(0,10), fill="x")

        tk.Label(from_kiri, text="Penulis", anchor="w").pack(fill="x")
        self.entry_penulis = tk.Entry(from_kiri, font=("Arial", 12), width=30)
        self.entry_penulis.pack(pady=(0,10), fill="x")

        tk.Label(from_kiri, text="Tahun Terbit (1901 - 2155)", anchor="w").pack(fill="x")
        self.entry_tahun = tk.Entry(from_kiri, font=("Arial", 12), width=30)
        self.entry_tahun.pack(pady=(0,10), fill="x")
        
        # Tombol Aksi
        self.btn_simpan = tk.Button(from_kiri, text="Simpan Data", fg="white", bg="green")
        self.btn_simpan.pack(pady=(20,5), fill="x")

        self.btn_edit = tk.Button(from_kiri, text="Edit Data", fg="white", bg="#1e6fd9")
        self.btn_edit.pack(pady=5, fill="x")

        self.btn_hapus = tk.Button(from_kiri, text="Hapus Data", fg="white", bg="#d93025")
        self.btn_hapus.pack(pady=5, fill="x")

        self.btn_reset = tk.Button(from_kiri, text="Bersihkan Form")
        self.btn_reset.pack(pady=5, fill="x")
        
        # ===== FRAME KANAN: TABEL DAFTAR BUKU =====
        from_kanan = tk.Frame(self)
        from_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        tk.Label(from_kanan, text="Daftar Buku Perpustakaan", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Komponen Tabel (Treeview dari tkinter ttk)
        kolom = ("id_buku", "judul", "penulis", "tahun_terbit")
        self.tabel = ttk.Treeview(from_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id_buku", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun_terbit", text="Tahun Terbit")

        self.tabel.column("id_buku", width=50, anchor="center")
        self.tabel.column("judul", width=200, anchor="w")
        self.tabel.column("penulis", width=150, anchor="w")
        self.tabel.column("tahun_terbit", width=90, anchor="center")
                
        self.tabel.pack(fill="both", expand=True, pady=10)
        
# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = BukuView()
    app.mainloop()