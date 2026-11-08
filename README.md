<div align="center">

# 🕷️ Manual Web Scraper & Quotes Organizer
### *Automation Systems UTS Project — Universitas Pelita Bangsa*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Architecture](https://img.shields.io/badge/Architecture-CLI%20%2F%20Regex-orange?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![Course](https://img.shields.io/badge/Course-Automation%20Systems-purple?style=for-the-badge)](#)

A high-performance, zero-dependency HTML parser implementation built from scratch using pure **Python Regular Expressions (`re`)** for dynamic web data extraction, multi-page crawling, structural data storage, and automated archiving.

[Identitas Kelompok](#-identitas-kelompok) • [Ringkasan](#-ringkasan-proyek) • [Persyaratan Sistem](#-persyaratan-sistem) • [Panduan Instalasi](#-panduan-instalasi-langkah-demi-langkah) • [Penggunaan CLI](#-panduan-penggunaan-cli) • [Arsitektur Teknik](#-arsitektur-teknik--skema-regex) • [Struktur Berkas](#-struktur-berkas-dan-output)

</div>

---

---

## 👥 Identitas Kelompok

| Parameter | Keterangan |
| :--- | :--- |
| **Mata Kuliah** | Automation Systems |
| **Dosen Pengampu** | Anggi Muhammad Rifa'i, M.Kom |
| **Program Studi** | Teknik Informatika |
| **Fakultas** | Fakultas Teknik — Universitas Pelita Bangsa |

### 👨‍💻 Anggota Kelompok (3 Mahasiswa)

| No. | Nama Mahasiswa | NIM |
| :-: | :--- | :-: |
| 1 | **Muhammad Fiqri Firmansyah** | 312310629 |
| 2 | **Muhammad Adrian Arsy Fadila** | 312310648 |
| 3 | **Endang Sirait** | 312310588 |

## 📌 Ringkasan Proyek

Aplikasi **Manual Web Scraper & Quotes Organizer** ini dikembangkan untuk mengotomatisasi pencarian, penelusuran halaman (*crawling*), pembersihan data, serta pengarsipan informasi dari website publik secara otomatis tanpa ketergantungan pada pustaka parser eksternal seperti BeautifulSoup atau Scrapy.

Seluruh proses ekstraksi data dijalankan melalui **Command Line Interface (CLI)** dengan memanfaatkan alur kerja standar pustaka bawaan Python:
- Ekstraksi elemen HTML menggunakan **Regular Expressions (`re`)**.
- Penanganan hirarki sistem berkas dinamis menggunakan **`pathlib`**.
- Pengarsipan otomatis berbasis kompresi **`zipfile`**.

---

## 📋 Persyaratan Sistem

Sebelum menjalankan aplikasi ini, pastikan sistem komputer memenuhi prasyarat berikut:

- **Sistem Operasi:** Windows 10/11, macOS, atau Linux (Disarankan Windows 11).
- **Python:** Versi `3.8` atau yang lebih baru.
- **Git:** Versi terbaru untuk kloning repositori.
- **Editor Kode:** Visual Studio Code (disarankan).

---

## 🛠️ Panduan Instalasi Langkah demi Langkah

Ikuti instruksi perintah terminal di bawah ini untuk menyiapkan lingkungan proyek di komputer lokal:

### 1. Kloning Repositori
Buka terminal / Command Prompt kamu dan jalankan perintah:
```bash
git clone [https://github.com/MuhammadFiqriFirmansyah/uts-automation-systems-scraper.git](https://github.com/MuhammadFiqriFirmansyah/uts-automation-systems-scraper.git)
cd uts-automation-systems-scraper

```

### 2. Buat Virtual Environment (Sangat Direkomendasikan)

Untuk mengisolasi pustaka proyek agar tidak bentrok dengan Python global:

* **Di Windows (PowerShell / CMD):**
```bash
python -m venv venv
.\venv\Scripts\activate

```


* **Di macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



### 3. Install Dependensi

Pasang pustaka HTTP `requests` yang tercantum di dalam file `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

---

## 🚀 Panduan Penggunaan CLI

Aplikasi dieksekusi melalui terminal menggunakan perintah `python main.py` diikuti dengan argumen opsi yang dinamis.

### Parameter Argumen Terminal

| Argumen | Tipe | Wajib | Deskripsi | Nilai Default |
| --- | --- | --- | --- | --- |
| `--url` | `string` | ❌ | Target URL utama yang akan di-scrape | `https://quotes.toscrape.com/` |
| `--keyword` | `string` | ❌ | Filter pencarian kata kunci pada teks/penulis/tag | `""` (tanpa filter) |
| `--limit` | `integer` | ❌ | Batas kuota minimal jumlah record data yang diambil | `30` |
| `--backup` | `flag` | ❌ | Menyertakan flag ini untuk otomatis membuat arsip ZIP | `False` |

---

### Contoh Perintah Eksekusi

#### 1. Eksekusi Standar (Minimal 30 Data + Backup)

Mengambil 30 record data pertama dari situs target dan langsung membuat arsip backup ZIP:

```bash
python main.py --limit 30 --backup

```

#### 2. Eksekusi Saring Kata Kunci (Filtering Search)

Mencari 30 data yang spesifik mengandung kata kunci **"love"** di seluruh halaman web hingga kuota terpenuhi:

```bash
python main.py --keyword love --limit 30 --backup

```

#### 3. Custom URL & Limit Spesifik

Menjalankan pencarian pada URL target dengan batas 50 record data:

```bash
python main.py --url [https://quotes.toscrape.com/](https://quotes.toscrape.com/) --keyword life --limit 50 --backup

```

---

### 💻 Contoh Tampilan Console (Terminal Output)

```text
==================================================
   AUTOMATION SYSTEMS - QUOTES & DATA COLLECTOR   
==================================================
[*] Mengambil data dari Halaman 1: [https://quotes.toscrape.com/](https://quotes.toscrape.com/)
[*] Mengambil data dari Halaman 2: [https://quotes.toscrape.com/page/2/](https://quotes.toscrape.com/page/2/)
[*] Mengambil data dari Halaman 3: [https://quotes.toscrape.com/page/3/](https://quotes.toscrape.com/page/3/)
[*] Mengambil data dari Halaman 4: [https://quotes.toscrape.com/page/4/](https://quotes.toscrape.com/page/4/)
[*] Berhasil mengekstrak 30 record data secara manual via Regex.
[+] Data berhasil disimpan ke folder 'data/' dan 'output/'
[+] File backup ZIP berhasil disimpan di: D:\project\backup\backup_data.zip

================ RINGKASAN HASIL ================
 Filter Kata Kunci        : 'love'
 Total Record Lolos       : 30
==================================================

```

---

## 🔬 Arsitektur Teknik & Skema Regex

Aplikasi ini tidak menggunakan pustaka parsing HTML eksternal. Seluruh ekstraksi string HTML mentah memanfaatkan kombinasi tiga pola Regular Expression berikut:

1. **Pola Pemotong Container (Block Extractor):**
```regex
<div class="quote"[^>]*>(.*?)</div>\s*<!-- div class="quote" -->

```


*Mengisolasi setiap elemen `<div class="quote">` secara individu.*
2. **Pola Teks Kutipan (Quote Text):**
```regex
class="text"[^>]*>\s*“?(.*?)”?\s*</span>

```


*Menangkap konten teks kutipan di dalam elemen HTML.*
3. **Pola Penulis & Tag (Metadata Extractor):**
```regex
class="author"[^>]*>(.*?)</small>
<a class="tag"[^>]*>(.*?)</a>

```


*Mengekstrak nama penulis serta kategori tag secara spesifik.*

---

## 📂 Struktur Berkas dan Output

Setelah eksekusi program selesai, aplikasi secara otomatis membangun hirarki direktori berikut:

```text
UTS_Project_Kelompok_01/
├── 📁 backup/
│   └── backup_data.zip      # File arsip kompresi (.zip) hasil olahan data
├── 📁 data/
│   └── raw_data.txt         # Log mentah penangkapan teks langsung dari HTTP
├── 📁 dokumentasi/
│   └── laporan_uts.pdf      # Laporan resmi dan dokumentasi akademis
├── 📁 output/
│   ├── hasil_scraping.csv   # Dataset terstruktur berformat CSV
│   └── laporan.txt          # Ringkasan statistik eksekusi program
├── main.py                  # Script logika utama Python (CLI Executable)
├── README.md                # Berkas petunjuk penggunaan & dokumentasi
└── requirements.txt         # Daftar pustaka dependen

```

---

## 📊 Matriks Rubrik Penilaian UTS

| Aspek Penilaian | Bobot | Status Implementasi |
| --- | --- | --- |
| **Web Scraping & Data Extraction** | 20% | ✅ Berhasil mengambil >30 record dari target web. |
| **Regular Expressions (`re`)** | 15% | ✅ Menggunakan 3+ pola Regex manual tanpa BeautifulSoup. |
| **Reading & Writing Files** | 15% | ✅ Pemrosesan file `.txt` dan `.csv` menggunakan mode I/O. |
| **Organisasi File & Backup ZIP** | 15% | ✅ Struktur folder dinamis (`pathlib`) & otomatisasi ZIP. |
| **CLI Arguments & Error Handling** | 15% | ✅ Argumen dinamis (`argparse`) & `try-except` jaringan. |
| **Dokumentasi & Kualitas Kode** | 10% | ✅ Kode bersih, modular, dan README berstandar profesional. |
| **Presentasi & Demo** | 10% | ✅ Siap didemonstrasikan melalui CLI terminal. |

---