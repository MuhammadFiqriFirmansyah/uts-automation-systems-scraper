<div align="center">

# 🕷️ Manual Web Scraper & Quotes Organizer
### *Automation Systems UTS Project — Universitas Pelita Bangsa*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Architecture](https://img.shields.io/badge/Architecture-CLI%20%2F%20Regex-orange?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![Course](https://img.shields.io/badge/Course-Automation%20Systems-purple?style=for-the-badge)](#)

A high-performance, zero-dependency HTML parser implementation built from scratch using pure **Python Regular Expressions (`re`)** for dynamic web data extraction, multi-page crawling, structural data storage, and automated archiving.

[Ringkasan](#-ringkasan-proyek) • [Persyaratan Sistem](#-persyaratan-sistem) • [Panduan Instalasi](#-panduan-instalasi-langkah-demi-langkah) • [Penggunaan CLI](#-panduan-penggunaan-cli) • [Arsitektur Teknik](#-arsitektur-teknik--skema-regex) • [Struktur Berkas](#-struktur-berkas-dan-output)

</div>

---

## 📌 Ringkasan Proyek

Aplikasi **Manual Web Scraper & Quotes Organizer** ini dikembangkan untuk mengotomatisasi pencarian, pengambil sampel (*crawling*), pembersihan data, serta pengarsipan informasi dari website publik secara otomatis tanpa ketergantungan pada pustaka parser eksternal seperti BeautifulSoup atau Scrapy.

Seluruh proses ekstraksi data dijalankan melalui **Command Line Interface (CLI)** dengan memanfaatkan alur kerja bawaan standar pustaka Python:
- Ekstraksi elemen HTML menggunakan **Regular Expressions (`re`)**[cite: 1].
- Penanganan hirarki sistem berkas dinamis menggunakan **`pathlib`**.
- Pengarsipan otomatis berbasis kompresi **`zipfile`**[cite: 1, 2].

---

## 📋 Persyaratan Sistem

Sebelum menjalankan aplikasi ini, pastikan sistem kamu memenuhi prasyarat berikut:

- **Sistem Operasi:** Windows 10/11, macOS, atau Linux (Disarankan Windows 11).
- **Python:** Versi `3.8` atau yang lebih baru.
- **Git:** Versi terbaru untuk kloning repositori.
- **Visual Studio Code:** Opsional (disarankan sebagai Code Editor utama).

---

## 🛠️ Panduan Instalasi Langkah demi Langkah

Ikuti instruksi terminal di bawah ini untuk memasang dan menyiapkan lingkungan proyek di komputer lokal:

### 1. Kloning Repositori
Buka terminal / Command Prompt kamu dan jalankan perintah:
```bash
git clone [https://github.com/USERNAME_KAMU/uts-automation-systems-scraper.git](https://github.com/USERNAME_KAMU/uts-automation-systems-scraper.git)
cd uts-automation-systems-scraper