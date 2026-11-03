# Aplikasi Manajemen Perpustakaan

Dibuat oleh: **Saiful (F5212510026)**

## Deskripsi Aplikasi

Aplikasi desktop berbasis Python untuk mengelola data **buku** dan **anggota** perpustakaan.
Dibangun dengan pola arsitektur **Model-View-Controller (MVC)**, menggunakan **Tkinter / CustomTkinter**
untuk antarmuka dan **MySQL** (melalui Laragon) sebagai basis data.

Fitur utama:

- **Login** dengan password ter-hash SHA-256 dan pembatasan hak akses berbasis peran (Role-Based Access Control)
  - `admin`: dapat menambah, memperbarui, dan menghapus data buku
  - `anggota`: hanya dapat melihat daftar buku (tombol Simpan, Perbarui, dan Hapus dikunci)
- **Manajemen buku** (CRUD): simpan, perbarui, hapus, dan tampilkan daftar buku
- **Manajemen anggota** (CRUD): simpan, edit, hapus, dan tampilkan daftar anggota
- **Logout** untuk kembali ke halaman login
- **Unit test** dengan pytest dan **CI otomatis** dengan GitHub Actions (flake8 dan pytest)

## Struktur Direktori MVC

```
Tugas_Modul3_F5212510026/
├── main.py                      # Titik masuk aplikasi (menjalankan AuthController)
├── main_anggota.py              # Titik masuk untuk modul Anggota
├── pytest.ini                   # Konfigurasi pytest
├── requirements.txt             # Daftar dependensi
├── .gitignore
├── config/
│   └── database.py              # Pengaturan dan koneksi ke MySQL
├── models/                      # MODEL: akses data dan logika bisnis
│   ├── buku_model.py
│   ├── anggota_model.py
│   └── user_model.py
├── views/                       # VIEW: tampilan antarmuka (pasif, tanpa logika)
│   ├── buku_view.py
│   ├── anggota_view.py
│   └── login_view.py
├── controllers/                 # CONTROLLER: penghubung View dan Model
│   ├── buku_controller.py
│   ├── anggota_controller.py
│   └── auth_controller.py
├── tests/                       # Unit test (pytest)
│   ├── test_buku.py
│   └── test_auth.py
└── .github/workflows/
    └── ci_pipeline.yml          # Pipeline CI GitHub Actions
```

Pembagian tanggung jawab:

| Komponen | Tanggung jawab |
|---|---|
| **Model** | Menjalankan kueri SQL (CRUD dan autentikasi) ke MySQL |
| **View** | Menampilkan form, tabel, dan tombol; tidak berisi logika bisnis |
| **Controller** | Menerima aksi pengguna dari View, memanggil Model, lalu memperbarui View |

## Panduan Instalasi dan Konfigurasi Database MySQL

### 1. Prasyarat

- Python 3.11 atau lebih baru (diuji dengan Python 3.13)
- [Laragon](https://laragon.org/) (menyediakan MySQL)
- Git

### 2. Unduh proyek dan siapkan virtual environment

```bash
git clone https://github.com/SAIFUL-ARC/Tugas_Modul3_F5212510026.git
cd Tugas_Modul3_F5212510026
python -m venv env
```

Aktifkan virtual environment:

```powershell
# PowerShell
.\env\Scripts\Activate.ps1
```

```bash
# Git Bash
source env/Scripts/activate
```

Instal seluruh dependensi:

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi database MySQL

1. Buka **Laragon**, lalu klik **Start All** agar layanan MySQL berjalan.
2. Buka **Terminal** pada Laragon dan masuk ke MySQL:

```bash
mysql -u root -p
```

3. Jalankan skrip berikut untuk membuat database, tabel, dan akun uji coba:

```sql
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

CREATE TABLE buku (
    id_buku INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(100) NOT NULL,
    penulis VARCHAR(100) NOT NULL,
    tahun_terbit YEAR NULL
);

CREATE TABLE anggota (
    id_anggota INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat TEXT NULL
);

CREATE TABLE users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'anggota') NOT NULL DEFAULT 'anggota'
);

-- Akun uji coba (password disimpan sebagai hash SHA-256)
INSERT INTO users (username, password, role) VALUES
('petugas', SHA2('admin123', 256), 'admin'),
('mahasiswa', SHA2('user123', 256), 'anggota');
```

4. Pengaturan koneksi berada di `config/database.py`. Nilai bawaannya sudah sesuai dengan Laragon:

| Pengaturan | Nilai |
|---|---|
| host | `localhost` |
| database | `perpustakaan` |
| username | `root` |
| password | *(kosong)* |

Jika MySQL kamu memakai username atau password yang berbeda, ubah nilai tersebut pada file `config/database.py`.

## Cara Menjalankan Aplikasi

Pastikan MySQL di Laragon sudah menyala (**Start All**), lalu dari folder proyek dengan virtual environment aktif:

```bash
python main.py
```

Jendela **Login** akan muncul. Masuk menggunakan akun uji coba:

| Username | Password | Role | Hak akses |
|---|---|---|---|
| `petugas` | `admin123` | admin | Tambah, perbarui, dan hapus data buku |
| `mahasiswa` | `user123` | anggota | Hanya melihat daftar buku |

Gunakan tombol **Logout** di bagian bawah form untuk kembali ke halaman login.

Untuk membuka modul **Anggota**:

```bash
python main_anggota.py
```

## Menjalankan Pengujian

```bash
pytest -v
```

## Membuat Berkas Eksekusi (.exe)

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

Hasilnya berada di `dist/AplikasiPerpustakaan.exe`. MySQL (Laragon) harus tetap menyala saat aplikasi dibuka.

## Continuous Integration

Setiap `push` atau `pull request` ke branch `main` menjalankan pipeline GitHub Actions
(`.github/workflows/ci_pipeline.yml`): instalasi dependensi, pengecekan kode dengan **flake8**, lalu **pytest**.
