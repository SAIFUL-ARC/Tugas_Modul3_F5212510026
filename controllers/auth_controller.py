#Saiful_F5212510026
import tkinter as tk
import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = None
        self.user = None   # diisi data user jika login berhasil

    def buka_login(self):
        # Membuat jendela login baru (dipakai saat aplikasi mulai dan setelah logout)
        self.user = None
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)
        self.view.bind("<Return>", lambda event: self.proses_login())

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']} ({user['role']})")
            self.user = user
            # Menghentikan mainloop jendela login; jendela utama dibuka di run()
            self.view.quit()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def run(self):
        while True:
            self.buka_login()
            self.view.mainloop()

            # Tutup jendela login (abaikan jika sudah ditutup lewat tombol X)
            try:
                self.view.destroy()
            except tk.TclError:
                pass

            # Login tidak berhasil (jendela login ditutup): aplikasi selesai
            if self.user is None:
                break

            # Buka jendela utama Perpustakaan dengan mengirimkan role pengguna
            app_utama = BukuController(user_role=self.user['role'])
            kembali_ke_login = app_utama.run()

            # Jika bukan karena Logout (jendela ditutup biasa), aplikasi selesai
            if not kembali_ke_login:
                break