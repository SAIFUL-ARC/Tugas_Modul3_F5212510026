# Saiful_F5212510026
# buku_controller.py
from tkinter import messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.id_terpilih = None       # id_buku dari baris tabel yang sedang dipilih
        self.logout_diminta = False   # True jika pengguna menekan tombol Logout

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_edit.configure(command=self.edit_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_reset.configure(command=self.bersihkan_form)
        self.view.btn_logout.configure(command=self.logout)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        # OTORISASI: jika bukan admin, nonaktifkan form input dan tombol simpan/perbarui/hapus
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_edit.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def hanya_admin(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk mengubah data!")
            return False
        return True

    def muat_data_tabel(self):
        # Membersihkan isi tabel sebelum memuat data baru
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data ke dalam Tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku["id_buku"], buku["judul"], buku["penulis"], buku["tahun_terbit"]))

    def validasi_input(self, judul, penulis, tahun):
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return False
        if len(judul) > 100 or len(penulis) > 100:
            messagebox.showwarning("Peringatan", "Judul dan penulis maksimal 100 karakter!")
            return False
        if not tahun.isdigit() or not (1901 <= int(tahun) <= 2155):
            messagebox.showwarning("Peringatan", "Tahun harus berupa angka antara 1901 dan 2155!")
            return False
        return True

    def isi_form(self, judul, penulis, tahun):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.view.entry_judul.insert(0, judul)
        self.view.entry_penulis.insert(0, penulis)
        self.view.entry_tahun.insert(0, tahun)

    def bersihkan_form(self):
        self.isi_form("", "", "")
        self.id_terpilih = None
        self.view.tabel.selection_remove(self.view.tabel.selection())

    def pilih_baris(self, event=None):
        # Dipanggil saat baris tabel diklik: data baris dimasukkan ke form
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        id_buku, judul, penulis, tahun = self.view.tabel.item(terpilih[0], "values")
        self.id_terpilih = id_buku
        self.isi_form(str(judul), str(penulis), str(tahun))

    def simpan_data(self):
        # Proteksi ganda di level Controller
        if not self.hanya_admin():
            return

        # Mengambil nilai input dari View
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi input
        if not self.validasi_input(judul, penulis, tahun):
            return

        # Mengirim data ke Model untuk disimpan
        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def edit_data(self):
        if not self.hanya_admin():
            return
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris buku di tabel yang akan diperbarui!")
            return
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()
        if not self.validasi_input(judul, penulis, tahun):
            return
        if self.model.update_buku(self.id_terpilih, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        if not self.hanya_admin():
            return
        if self.id_terpilih is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris buku di tabel yang akan dihapus!")
            return
        judul = self.view.entry_judul.get()
        if not messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus buku '{judul}'?"):
            return
        if self.model.delete_buku(self.id_terpilih):
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def logout(self):
        # Menutup jendela perpustakaan; AuthController akan menampilkan LoginView lagi
        self.logout_diminta = True
        self.view.destroy()

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()
        return self.logout_diminta   # True = kembali ke login, False = aplikasi ditutup