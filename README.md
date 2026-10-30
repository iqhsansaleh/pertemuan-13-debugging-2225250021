# Pertemuan 13 - Debugging dan Testing

**Nama:** Iqhsan Saleh  
**NIM:** 2225250021  
**Kelas:** 3A

## Kasus

Program pada `praktik/praktik_4_debugging.py` memproses data nilai mahasiswa melalui tiga fungsi: menghitung rata-rata, menentukan status kelulusan dengan batas 60, dan mencari nilai tertinggi. Program awal memiliki tiga bug logika. Pengujian dilakukan dengan test case untuk membuktikan perilaku yang salah sebelum perbaikan.

Output aktual program awal:

```text
Rata-rata: 60.0
Status 60: Tidak lulus
Tertinggi: 0
```

## Test Case

Test awal dijalankan sebelum perbaikan. T6 merupakan test tambahan untuk memeriksa data yang seluruh nilainya negatif.

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| T2 | Rata-rata `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | Status nilai `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | Status nilai `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | Tertinggi `[80, 60, 90, 70]` | `90` | `0` | FAIL |
| T6 | Tertinggi `[-8, -2, -5]` | `-2` | `-8` | FAIL |

## Bug Report

| Bug ID | Gejala | Test Case | Lokasi | Akar Penyebab | Perbaikan |
|---|---|---|---|---|---|
| B01 | Rata-rata tidak sesuai jumlah data. | T1 menghasilkan `60.0`; T2 menghasilkan `36.0`. | `praktik/praktik_4_debugging.py`, `hitung_rata_rata` | Jumlah selalu dibagi 5, meskipun jumlah elemen bukan lima. | Bagi `sum(nilai)` dengan `len(nilai)`. |
| B02 | Nilai tepat 60 dinyatakan tidak lulus. | T3 gagal; T4 tetap benar. | `praktik/praktik_4_debugging.py`, `status` | Kondisi `nilai > 60` salah ketika nilainya sama dengan 60. | Ganti menjadi `nilai >= 60`. |
| B03 | Fungsi tidak menemukan nilai terbesar. | T5 menghasilkan `0`; T6 menghasilkan `-8`. | `praktik/praktik_4_debugging.py`, `nilai_tertinggi` | Nilai awal `0` tidak sesuai untuk semua rentang input dan kondisi `x < tertinggi` mencari nilai yang lebih kecil, bukan lebih besar. | Mulai dari elemen pertama dan perbarui jika `x > tertinggi`. |

Bukti tracing: pada T1, jumlah data adalah `300`, sehingga pembagi tetap menghasilkan `300 / 5 = 60`, bukan `75`. Pada T3, `60 > 60` bernilai `False`. Pada T5, seluruh nilai positif gagal dibandingkan dengan kondisi `x < 0`, sehingga nilai awal 0 tidak berubah. Pada T6, kondisi lama justru memilih `-8` sebagai nilai terkecil.

## Retest

Setelah perbaikan, seluruh enam test dijalankan kembali: **6 PASS, 0 FAIL**. Test T4 yang telah lulus sebelum perbaikan tetap lulus. Output program setelah perbaikan:

```text
Rata-rata: 75.0
Status 60: Lulus
Tertinggi: 90
```

## Cara Menjalankan

Jalankan program dari direktori root proyek:

```bash
python3 praktik/praktik_4_debugging.py
```

Jalankan seluruh test praktik:

```bash
python3 -m unittest discover -s praktik -p 'test_praktik_4_debugging.py' -v
```

## Refleksi

Teknik yang paling membantu adalah membuat test case untuk nilai batas dan variasi input, lalu menelusuri perubahan nilai variabel pada fungsi. Test memperlihatkan input yang gagal secara spesifik, sedangkan tracing menjelaskan akar penyebabnya. Setelah perbaikan, menjalankan ulang seluruh test memastikan bug tertangani tanpa merusak kasus yang sebelumnya sudah benar.
