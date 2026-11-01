# anggota_controller.py
from tkinter import messagebox

from models.anggota_model import AnggotaModel

class AnggotaController:
    def __init__(self, view):
        self.model = AnggotaModel()
        self.view = view
        self.id_terpilih = None   # id_anggota dari baris tabel yang sedang dipilih
        self.data_anggota = {}    # penyimpan data lengkap per id (alamat bisa multi-baris)

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_edit.configure(command=self.edit_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_reset.configure(command=self.bersihkan_form)
        # Klik baris di tabel -> isi form otomatis
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Membersihkan isi tabel sebelum memuat data baru
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        self.id_terpilih = None
        self.data_anggota = {}

        # Mengambil data dari Model (database)
        data = self.model.get_all_anggota()

        # Memasukkan data ke dalam Tabel View
        for anggota in data:
            id_anggota = str(anggota["id_anggota"])
            alamat = anggota["alamat"] or ""     # kolom alamat boleh NULL
            self.data_anggota[id_anggota] = (anggota["nama"], alamat)
            # Di tabel, baris baru pada alamat diganti spasi agar tampil satu baris
            alamat_tabel = alamat.replace("\r", " ").replace("\n", " ")
            self.view.tabel.insert("", "end", iid=id_anggota,
                                   values=(id_anggota, anggota["nama"], alamat_tabel))

    def ambil_input(self):
        # Mengambil nilai input dari View
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get("1.0", "end-1c").strip()
        return nama, alamat

    def validasi_input(self, nama, alamat):
        # Nama wajib diisi (NOT NULL), alamat boleh kosong (NULL)
        if not nama:
            messagebox.showwarning("Peringatan", "Nama anggota harus diisi!")
            return False

        # Sesuai struktur tabel: nama varchar(100)
        if len(nama) > 100:
            messagebox.showwarning("Peringatan", "Nama maksimal 100 karakter!")
            return False

        return True

    def isi_form(self, nama, alamat):
        # Mengosongkan lalu mengisi form dengan data yang diberikan
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete("1.0", 'end')
        self.view.entry_nama.insert(0, nama)
        self.view.entry_alamat.insert("1.0", alamat)

    def bersihkan_form(self):
        # Mengosongkan form dan membatalkan pilihan baris
        self.isi_form("", "")
        self.id_terpilih = None
        self.view.tabel.selection_remove(self.view.tabel.selection())

    def pilih_baris(self, event=None):
        # Dipanggil saat baris tabel diklik: data baris dimasukkan ke form
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        self.id_terpilih = terpilih[0]
        nama, alamat = self.data_anggota[self.id_terpilih]
        self.isi_form(nama, alamat)

    def simpan_data(self):
        nama, alamat = self.ambil_input()

        if not self.validasi_input(nama, alamat):
            return

        # Alamat kosong disimpan sebagai NULL
        berhasil = self.model.create_anggota(nama, alamat or None)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def edit_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris anggota di tabel yang akan diedit!")
            return

        nama, alamat = self.ambil_input()

        if not self.validasi_input(nama, alamat):
            return

        if self.model.update_anggota(self.id_terpilih, nama, alamat or None):
            messagebox.showinfo("Sukses", "Data anggota berhasil diubah!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat mengubah data.")

    def hapus_data(self):
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris anggota di tabel yang akan dihapus!")
            return

        # Konfirmasi sebelum menghapus (penghapusan tidak bisa dibatalkan)
        nama = self.view.entry_nama.get()
        if not messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus anggota '{nama}'?"):
            return

        if self.model.delete_anggota(self.id_terpilih):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()