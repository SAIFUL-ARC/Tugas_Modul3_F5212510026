# anggota_view.py
import tkinter as tk
from tkinter import ttk

class AnggotaView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Manajemen Perpustakaan - Anggota")
        self.geometry("700x600")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=1) # Kolom Kanan (Tabel)
        self.grid_rowconfigure(0, weight=1)

        # ===== FRAME KIRI: FORMULIR INPUT =====
        from_kiri = tk.Frame(self)
        from_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(from_kiri, text="Form Data Anggota", font=("Arial", 14, "bold")).pack(pady=10)

        # Komponen Input (label sesuai kolom tabel anggota di database)
        # Catatan: id_anggota tidak diinput karena AUTO_INCREMENT (diisi otomatis oleh MySQL)
        tk.Label(from_kiri, text="Nama Anggota", anchor="w").pack(fill="x")
        self.entry_nama = tk.Entry(from_kiri, font=("Arial", 12), width=30)
        self.entry_nama.pack(pady=(0,10), fill="x")

        # Kolom alamat bertipe TEXT di database, jadi memakai kotak teks beberapa baris
        tk.Label(from_kiri, text="Alamat", anchor="w").pack(fill="x")
        self.entry_alamat = tk.Text(from_kiri, font=("Arial", 12), width=30, height=4)
        self.entry_alamat.pack(pady=(0,10), fill="x")

        # Tombol Aksi
        self.btn_simpan = tk.Button(from_kiri, text="Simpan Data", fg="white", bg="green")
        self.btn_simpan.pack(pady=(20,5), fill="x")

        self.btn_edit = tk.Button(from_kiri, text="Edit Data", fg="white", bg="#1e6fd9")
        self.btn_edit.pack(pady=5, fill="x")

        self.btn_hapus = tk.Button(from_kiri, text="Hapus Data", fg="white", bg="#d93025")
        self.btn_hapus.pack(pady=5, fill="x")

        self.btn_reset = tk.Button(from_kiri, text="Bersihkan Form")
        self.btn_reset.pack(pady=5, fill="x")

        # ===== FRAME KANAN: TABEL DAFTAR ANGGOTA =====
        from_kanan = tk.Frame(self)
        from_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        tk.Label(from_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 14, "bold")).pack(pady=10)

        # Komponen Tabel (Treeview dari tkinter ttk)
        kolom = ("id_anggota", "nama", "alamat")
        self.tabel = ttk.Treeview(from_kanan, columns=kolom, show="headings", height=15)

        # Label Heading (urutan sama dengan kolom tabel di database)
        self.tabel.heading("id_anggota", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        # Konfigurasi Lebar Kolom
        self.tabel.column("id_anggota", width=50, anchor="center")
        self.tabel.column("nama", width=150, anchor="w")
        self.tabel.column("alamat", width=200, anchor="w")

        self.tabel.pack(fill="both", expand=True, pady=10)

# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()