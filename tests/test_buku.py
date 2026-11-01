from unittest.mock import MagicMock
from models.buku_model import BukuModel


def buat_model_palsu():
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model = BukuModel()
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    return model, mock_cursor


def test_create_buku_berhasil():
    model, mock_cursor = buat_model_palsu()

    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


def test_get_all_buku_mengembalikan_daftar_buku():
    model, mock_cursor = buat_model_palsu()

    # Simulasi data yang dikembalikan database
    data_palsu = [
        {"id_buku": 1, "judul": "Bumi Manusia", "penulis": "Pramoedya Ananta Toer", "tahun_terbit": 1980},
        {"id_buku": 2, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun_terbit": 2005},
    ]
    mock_cursor.fetchall.return_value = data_palsu

    hasil = model.get_all_buku()

    assert hasil == data_palsu
    assert len(hasil) == 2
    assert hasil[0]["judul"] == "Bumi Manusia"
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_get_all_buku_tanpa_koneksi_mengembalikan_list_kosong():
    model = BukuModel()
    model.conn = None

    assert model.get_all_buku() == []


def test_update_buku_berhasil():
    model, mock_cursor = buat_model_palsu()

    hasil = model.update_buku(1, "Judul Baru", "Penulis Baru", 2024)

    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()


def test_delete_buku_berhasil():
    model, mock_cursor = buat_model_palsu()

    hasil = model.delete_buku(1)

    assert hasil is True
    mock_cursor.execute.assert_called_once()
    model.conn.commit.assert_called_once()