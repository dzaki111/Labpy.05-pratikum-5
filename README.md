


# Program Pengelolaan Data Mahasiswa

Program ini dirancang untuk mengelola data mahasiswa secara efisien. Fitur-fitur yang disediakan meliputi:

- **Melihat Data Mahasiswa**: Menampilkan data seluruh mahasiswa dalam format tabel.
- **Menambahkan Data Baru**: Memasukkan data mahasiswa baru, termasuk Nama, NIM, Nilai Tugas, UTS, dan UAS.
- **Mengubah Data**: Memperbarui informasi siswa berdasarkan nomor urut data.
- **Menghapus Data**: Menghapus data pelajar tertentu dari daftar.
- **Mencari Data**: Mencari mahasiswa berdasarkan Nama atau NIM.
- **Keluar dari Program**: Menyelesaikan program.

## Perhitungan Nilai Akhir
Nilai akhir pelajar dihitung berdasarkan bobot sebagai berikut:
- **Tugas**: 30%
- **UTS**: 35%
- **UAS**: 35%.

## Komponen Program

### 1. Struktur Data
Data siswa disimpan dalam daftar bernama `data_list`, yang berisi elemen kamus. Setiap kamus mewakili satu pelajar dengan format berikut:

```python
{
    'Nama': 'Nama Mahasiswa',
    'NIM': 'NIM Mahasiswa',
    'Tugas': 80.0,  # Nilai Tugas
    'UTS': 75.0,    # Nilai UTS
    'UAS': 85.0,    # Nilai UAS
    'Nilai Akhir': 81.5  # Hasil perhitungan nilai akhir
}
```

### 2. Fungsi-Fungsi Utama

#### `oi_final_grade(tugas, uts, uas)`
Fungsi ini menghitung nilai akhir siswa berdasarkan bobot masing-masing:
- **Tugas**: 30%
- **UTS**: 35%
- **UAS**: 35%.

#### `lihat_data()`
Fungsi ini menampilkan seluruh data siswa dalam format tabel. Jika data kosong, ditampilkan pesan `"Tidak ada data!"`.

#### `tambah_data()`
Fungsi ini meminta pengguna untuk memasukkan data siswa baru, seperti Nama, NIM, dan nilai-nilai (Tugas, UTS, UAS). Nilai akhir dihitung menggunakan `oi_final_grade`, kemudian data dimasukkan ke dalam `data_list`.

#### `ubah_data()`
Fungsi ini memungkinkan pengguna untuk memperbarui data siswa berdasarkan nomor urut. Setelah memilih nomor data, pengguna dapat memasukkan data baru. Nilai akhir diperbarui secara otomatis.

#### `hapus_data()`
Fungsi ini memungkinkan pengguna untuk menghapus data siswa berdasarkan nomor urut. Data akan dihapus dari daftar `data_list`.

#### `cari_data()`
Fungsi ini mencari data siswa berdasarkan Nama atau NIM. Jika ditemukan, data yang sesuai akan ditampilkan dalam tabel. Jika tidak ditemukan, ditampilkan pesan `"Data tidak ditemukan!"`.

### 3. Program Utama (Menu Loop)
Menu program utama memungkinkan pengguna untuk memilih fitur melalui input:

- **L**: Melihat data.
- **T**: Menambahkan data.
- **U**: Mengubah data.
- **H**: Menghapus data.
- **C**: Mencari data.
- **K**: Keluar dari program.

Program terus berjalan hingga pengguna memilih opsi **K**.

## Cara Menggunakan Program

1. Simpan kode dalam file Python, misalnya `program_mahasiswa.py`.
2. Jalankan program di terminal/command prompt dengan perintah:
   ```bash
   python program_mahasiswa.py
   ```
3. Pilih menu yang diinginkan sesuai instruksi.

## Contoh Tabel Data
Berikut adalah contoh tampilan tabel data:

```
Daftar Nilai
======================================================================
| NO | NIM      | NAMA       | TUGAS   | UTS     | UAS     | AKHIR   |
======================================================================
|  1 | 1234     | ZAKI       | 80.00   | 75.00   | 90.00   | .0   |
|  2 | 4567     | TONO       | 90.00   | 75.00   | 80.00   | .0   |
|  3 | 8910     | BUDI       | 90.00   | 75.00   | 80.00   | .0   |
======================================================================
```

Program ini membantu mengelola data siswa dengan mudah dan fleksibel menggunakan antarmuka berbasis teks.
