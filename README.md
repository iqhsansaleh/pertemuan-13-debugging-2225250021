# Praktik 4: Investigasi dan Perbaikan Bug

## Baseline sebelum perbaikan

Program awal dijalankan tanpa perubahan dengan perintah:

```powershell
python praktik/praktik_4_debugging.py
```

Output aktual:

```text
Rata-rata: 60.0
Status 60: Tidak lulus
Tertinggi: 0
```

## Test reproduksi

Test dijalankan dari root proyek:

```powershell
python -m unittest discover -s praktik -p 'test_praktik_4_debugging.py' -v
```

| ID | Input | Expected | Aktual sebelum perbaikan | Hasil awal |
|---|---|---:|---:|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | `75.0` | `60.0` | FAIL |
| T2 | Rata-rata `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | Status `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | Status `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | Tertinggi `[80, 60, 90, 70]` | `90` | `0` | FAIL |
| T6 | Tertinggi `[-8, -2, -5]` | `-2` | `-8` | FAIL |

T1 sampai T5 adalah test minimum praktik. T6 ditambahkan untuk memeriksa bahwa pencarian nilai tertinggi juga benar saat semua nilai negatif.

## Laporan bug

| Bug ID | Gejala dan test bukti | Lokasi | Akar penyebab | Perbaikan |
|---|---|---|---|---|
| B01 | Rata-rata terlalu kecil; T1 mendapat `60.0` dan T2 mendapat `36.0`. | `praktik/praktik_4_debugging.py`, fungsi `hitung_rata_rata`, baris 2 | Jumlah selalu dibagi `5`, tidak peduli jumlah elemen. Pada T1 jumlahnya `300`, tetapi `300 / 5 = 60`; pada T2 `180 / 5 = 36`. | Bagi jumlah dengan `len(nilai)`. |
| B02 | Nilai ambang 60 dinyatakan tidak lulus; T3 gagal, sedangkan T4 lulus. | `praktik/praktik_4_debugging.py`, fungsi `status`, baris 5 | Kondisi `nilai > 60` bernilai salah ketika `nilai` tepat 60. | Gunakan `nilai >= 60` agar nilai batas termasuk lulus. |
| B03 | Nilai tertinggi untuk data positif menjadi `0`; T5 gagal. | `praktik/praktik_4_debugging.py`, fungsi `nilai_tertinggi`, baris 11-14 | Variabel dimulai dari 0 dan kondisi `x < tertinggi` justru mencari nilai yang lebih kecil. Semua input T5 positif, sehingga kondisi tidak pernah benar dan hasil tetap 0. | Mulai dari elemen pertama, lalu perbarui jika `x > tertinggi`. Ini juga menangani daftar yang seluruh nilainya negatif (T6). |

## Bukti tracing

- B01 / T1: `sum([80, 60, 90, 70])` adalah `300`; pembagi yang tertulis `5` menghasilkan `60.0`, bukan `75.0`. T2: `180 / 5` menghasilkan `36.0`, bukan `90.0`.
- B02 / T3: saat `nilai` adalah `60`, evaluasi `60 > 60` menghasilkan `False`, sehingga fungsi mengembalikan `"Tidak lulus"`.
- B03 / T5: `tertinggi` mulai `0`; nilai `80`, `60`, `90`, dan `70` semuanya gagal pada kondisi `x < 0`, sehingga tidak ada pembaruan dan hasil `0`. Pada T6, nilai pertama `-8` menggantikan `0`, tetapi `-2` dan `-5` tidak lebih kecil dari `-8`, sehingga hasilnya `-8` (nilai terkecil), bukan `-2`. Pada perbaikan, nilai awal adalah elemen pertama dan nilai `90` menggantikannya karena `90 > 80`.

## Retest setelah perbaikan

Seluruh test dijalankan kembali dengan perintah yang sama. Hasil: **6 test PASS, 0 FAIL**. T1-T5 lulus sesuai expected; T4 yang sudah PASS sebelum perbaikan tetap PASS, sehingga tidak ada regresi pada test itu. T6 juga lulus untuk data negatif.

Output program setelah perbaikan:

```text
Rata-rata: 75.0
Status 60: Lulus
Tertinggi: 90
```

## Riwayat Git

- `6c61db3` - `Praktik 4: rekam baseline dan test reproduksi` menyimpan program awal bermasalah dan test yang menunjukkan kegagalan.
- Commit perbaikan berikutnya menyimpan perubahan kode dan dokumentasi hasil retest.
