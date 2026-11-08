<div align="center">

# 🕷️ Manual Web Scraper & Quotes Organizer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)
[![Automation Systems](https://img.shields.io/badge/Course-Automation%20Systems-orange.svg)](#)
[![Universitas Pelita Bangsa](https://img.shields.io/badge/Campus-Universitas%20Pelita%20Bangsa-blueviolet.svg)](https://pelitabangsa.ac.id)

*A robust Command Line Interface (CLI) web scraping application built with pure Regular Expressions without third-party HTML parsers.*

[Fitur Utama](#-fitur-utama) • [Instalasi](#-instalasi) • [Cara Penggunaan](#-cara-penggunaan) • [Struktur Proyek](#-struktur-proyek)

---

</div>

## 📌 Deskripsi Proyek
Aplikasi ini dikembangkan untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah **Automation Systems** di Universitas Pelita Bangsa. Program berfungsi mengambil, mengorganisasi, dan mengarsip data dari situs web publik secara manual memanfaatkan ekspresi reguler (**Regex**) sesuai standar otomatisasi Python.

## ✨ Fitur Utama
- 🔍 **Manual Parsing (Regex):** Ekstraksi data murni menggunakan pustaka `re` tanpa BeautifulSoup/Scrapy.
- 📄 **Organisasi File Otomatis:** Penyimpanan logs raw dan file `.csv` otomatis menggunakan `pathlib`.
- 🗜️ **Backup Otomatis:** Mengompresi hasil pemrosesan dan data mentah ke dalam arsip `.zip`.
- 💻 **CLI Dynamic Arguments:** Mendukung argumen kustom via terminal (`--url`, `--keyword`, `--limit`, `--backup`).
- ⚡ **Auto-Page Traversal:** Penelusuran halaman dinamis hingga memenuhi kuota batas data minimum.

## 📁 Struktur Proyek
```text
UTS_Project_Kelompok_01/
├── data/               # Menyimpan log data mentah (.txt)
├── output/             # Hasil ekstraksi terstruktur (.csv) & laporan (.txt)
├── backup/             # File backup kompresi (.zip)
├── dokumentasi/        # Berkas PDF & laporan akademik
├── main.py             # Script utama program CLI
├── README.md           # Dokumentasi repositori
└── requirements.txt     # Pustaka dependen