import sys
import re
import csv
import zipfile
import argparse
from pathlib import Path
import requests

def fetch_html(url):
    """Mengambil HTML mentah dari URL target dengan penanganan error koneksi."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Gagal mengambil data dari website: {e}")
        return None

def parse_quotes_manual_regex(html_content, base_url):
    """
    Ekstraksi data kutipan secara manual dari string HTML mentah
    menggunakan Regular Expressions (tanpa BeautifulSoup).
    """
    quotes_list = []
    
    # Non-greedy regex pattern untuk mengekstrak per elemen container <div class="quote">...</div>
    quote_block_pattern = re.compile(
        r'<div class="quote"[^>]*>(.*?)</div>\s*<!-- div class="quote" -->', 
        re.DOTALL | re.IGNORECASE
    )
    blocks = quote_block_pattern.findall(html_content)
    
    # Fallback pattern jika struktur komentar HTML penutup div tidak ada
    if not blocks:
        quote_block_pattern = re.compile(
            r'<div class="quote"[^>]*>(.*?)(?=<div class="quote"|<nav>|</div>\s*</div>)', 
            re.DOTALL | re.IGNORECASE
        )
        blocks = quote_block_pattern.findall(html_content)

    # Regex 1: Ekstraksi Teks Kutipan
    text_pattern = re.compile(r'class="text"[^>]*>\s*“?(.*?)”?\s*</span>', re.DOTALL | re.IGNORECASE)
    
    # Regex 2: Ekstraksi Penulis (Author)
    author_pattern = re.compile(r'class="author"[^>]*>(.*?)</small>', re.DOTALL | re.IGNORECASE)
    
    # Regex 3: Ekstraksi Tag/Kategori
    tags_pattern = re.compile(r'<a class="tag"[^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)

    for block in blocks:
        # Ekstraksi Teks Kutipan
        text_match = text_pattern.search(block)
        quote_text = text_match.group(1).strip() if text_match else ""
        quote_text = quote_text.replace('&rdquo;', '').replace('&ldquo;', '').strip()

        # Ekstraksi Penulis
        author_match = author_pattern.search(block)
        author = author_match.group(1).strip() if author_match else "Unknown"
        
        # Ekstraksi Tag
        tags = tags_pattern.findall(block)
        tags_str = ", ".join([t.strip() for t in tags]) if tags else "General"

        if quote_text:
            quotes_list.append({
                'author': author,
                'quote': quote_text,
                'tags': tags_str,
                'url': base_url
            })
        
    return quotes_list

def fetch_multiple_pages(base_url, limit, keyword_filter=""):
    """
    Mengambil data dari halaman web berturut-turut sampai mendapatkan 
    jumlah record yang lolos filter sesuai limit yang diminta.
    """
    all_quotes = []
    page = 1
    max_pages = 100  # Batas aman traversal halaman
    
    kw_re = re.compile(re.escape(keyword_filter), re.IGNORECASE) if keyword_filter else None

    while page <= max_pages:
        url = f"{base_url.rstrip('/')}/page/{page}/" if page > 1 else base_url
        print(f"[*] Mengambil data dari Halaman {page}: {url}")
        
        html_content = fetch_html(url)
        if not html_content:
            break
            
        quotes = parse_quotes_manual_regex(html_content, base_url)
        if not quotes:
            print("[!] Tidak ada data lagi di halaman berikutnya.")
            break
            
        # Jika argumen keyword diisi, saring langsung data yang sesuai
        if kw_re:
            filtered = [
                q for q in quotes 
                if kw_re.search(q['quote']) or kw_re.search(q['author']) or kw_re.search(q['tags'])
            ]
            all_quotes.extend(filtered)
        else:
            all_quotes.extend(quotes)
            
        # Hentikan loop jika kuota data tersaring sudah mencapai limit
        if len(all_quotes) >= limit:
            break
            
        page += 1
        
    return all_quotes[:limit]

def save_data(quotes, keyword_filter):
    """Menyimpan data mentah dan hasil scraping ke CSV & TXT menggunakan pathlib."""
    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "output"
    
    data_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Simpan raw log ke data/raw_data.txt
    raw_txt = data_dir / "raw_data.txt"
    with open(raw_txt, "w", encoding="utf-8") as f:
        for q in quotes:
            f.write(f"AUTHOR: {q['author']} | TAGS: [{q['tags']}] | QUOTE: \"{q['quote']}\"\n")
            
    # 2. Simpan CSV ke output/hasil_scraping.csv
    csv_file = output_dir / "hasil_scraping.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['author', 'quote', 'tags', 'url'])
        writer.writeheader()
        writer.writerows(quotes)
        
    # 3. Simpan Laporan Ringkasan ke output/laporan.txt
    laporan_file = output_dir / "laporan.txt"
    total_count = len(quotes)
    
    with open(laporan_file, "w", encoding="utf-8") as f:
        f.write("=== RINGKASAN PEMROSESAN LAPORAN SCRAPING ===\n")
        f.write(f"Kata Kunci Filter       : '{keyword_filter if keyword_filter else 'Semua'}'\n")
        f.write(f"Total Record Tersaring  : {total_count}\n")
        f.write(f"Sumber Web              : {quotes[0]['url'] if quotes else 'N/A'}\n")

    return total_count

def create_backup():
    """Membuat backup file ZIP dari data dan output."""
    base_dir = Path(__file__).resolve().parent
    backup_dir = base_dir / "backup"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    zip_path = backup_dir / "backup_data.zip"
    
    files_to_zip = [
        base_dir / "data" / "raw_data.txt",
        base_dir / "output" / "hasil_scraping.csv",
        base_dir / "output" / "laporan.txt"
    ]
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_zip:
            if file.exists():
                zipf.write(file, arcname=file.name)
                
    return zip_path

def main():
    parser = argparse.ArgumentParser(
        description="Aplikasi Manual Web Scraping Quotes Collector (UTS Automation Systems)"
    )
    parser.add_argument("--url", type=str, default="https://quotes.toscrape.com/", help="URL Target Website")
    parser.add_argument("--keyword", type=str, default="", help="Kata kunci filter penulis, kata, atau tag")
    parser.add_argument("--limit", type=int, default=30, help="Jumlah minimal record data (default: 30)")
    parser.add_argument("--backup", action="store_true", help="Buat backup file ZIP otomatis")
    
    args = parser.parse_args()
    
    print("==================================================")
    print("   AUTOMATION SYSTEMS - QUOTES & DATA COLLECTOR   ")
    print("==================================================")
    
    quotes = fetch_multiple_pages(args.url, args.limit, args.keyword)
    
    if not quotes:
        print("[!] Data kosong atau scraping gagal.")
        sys.exit(1)
        
    print(f"[*] Berhasil mengekstrak {len(quotes)} record data secara manual via Regex.")
    
    count = save_data(quotes, args.keyword)
    print(f"[+] Data berhasil disimpan ke folder 'data/' dan 'output/'")
    
    if args.backup:
        zip_path = create_backup()
        print(f"[+] File backup ZIP berhasil disimpan di: {zip_path}")
        
    print("\n================ RINGKASAN HASIL ================")
    print(f" Filter Kata Kunci        : '{args.keyword}'")
    print(f" Total Record Lolos       : {count}")
    print("==================================================")

if __name__ == "__main__":
    main()