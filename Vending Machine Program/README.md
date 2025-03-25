README - Panduan Menjalankan Vending Machine DFA

Cara Menjalankan Program
1. Menjalankan dari Source Code (Python)
Persyaratan : Python 3.6 atau versi lebih baru
Langkah-langkah :
-Pastikan Anda memiliki file-file berikut dalam satu folder:
    vending_machine.py (program utama)
    vending_dfa.txt (file konfigurasi DFA)
-Buka terminal/command prompt di folder tersebut
-Jalankan program dengan perintah:
    python vending_machine.py

2. Menjalankan dari Executable (.exe)
Untuk Windows
-Download file vending_machine.exe
-Pastikan file vending_dfa.txt berada di folder yang sama
-Klik double pada vending_machine.exe

Untuk Linux/Mac:
-Download file executable yang sesuai
-Berikan permission eksekusi
    chmod +x vending_machine
-Jalankan
    ./vending_machine


Panduan Penggunaan Program

1. Masukkan Uang:
-Gunakan pecahan: 1000, 2000, 5000, atau 10000
-Uang bisa dimasukkan berkali-kali
-Jumlah maksimal nominal uang yang dapat dimasukkan adalah Rp10.000
-Contoh:
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 5000

2. Pilih Minuman:
-Ketik A (Rp3.000), B (Rp4.000), atau C (Rp6.000) ketika tombol ON menyala
-Contoh:
    ON: Minuman A, Minuman B, Minuman C
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B

3. Keluar dari Program:
-Ketik Exit untuk keluar

Contoh Output yang Diharapkan

-Contoh 1: Pembelian Berhasil
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 2000
    ON: Minuman A
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 1000
    ON: Minuman A, Minuman B
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): A
    Lintasan DFA: S0 → S2000 → S3000
    Minuman A dapat dibeli. Status: ACCEPTED.

-Contoh 2: Pembelian dengan Kembalian
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): 5000
    ON: Minuman A, Minuman B, Minuman C
    Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): B
    Lintasan DFA: S0 → S5000
    Minuman B dapat dibeli. Status: ACCEPTED.
    Kembalian: 1000

Troubleshooting

1. Error "File not found":
-Pastikan vending_dfa.txt ada di folder yang sama dengan program

2. Input tidak bekerja:
-Jika menggunakan executable, jalankan dari command prompt
-Pastikan tidak ada antivirus yang memblokir program

