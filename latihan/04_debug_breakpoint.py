"""Latihan breakpoint: rata-rata, batas kelulusan, dan nilai dari file.

Pembagi tetap 5 hanya benar jika list berisi tepat lima nilai. Pasang
breakpoint di fungsi yang ingin ditelusuri, lalu jalankan test dengan F5.
"""

import tempfile
import unittest
from pathlib import Path


def rata_rata(data):
	if not data:
		raise ValueError("Data nilai tidak boleh kosong")
	total = sum(data)
	return total / len(data)


def status_lulus(nilai):
	if nilai >= 60:
		return "Lulus"
	return "Tidak lulus"


def baca_nilai(path):
	with open(path, encoding="utf-8") as file:
		return [int(baris.strip()) for baris in file if baris.strip()]


class TestRataRata(unittest.TestCase):
	def test_tiga_nilai(self):
		self.assertEqual(rata_rata([80, 90, 70]), 80)

	def test_dua_nilai(self):
		self.assertEqual(rata_rata([100, 80]), 90)

	def test_satu_nilai(self):
		self.assertEqual(rata_rata([75]), 75)

	def test_list_kosong(self):
		with self.assertRaisesRegex(ValueError, "tidak boleh kosong"):
			rata_rata([])


class TestKasus1BatasKelulusan(unittest.TestCase):
	def test_di_bawah_batas(self):
		self.assertEqual(status_lulus(59), "Tidak lulus")

	def test_tepat_di_batas(self):
		self.assertEqual(status_lulus(60), "Lulus")

	def test_di_atas_batas(self):
		self.assertEqual(status_lulus(61), "Lulus")


class TestKasus3NilaiDariFile(unittest.TestCase):
	def test_membaca_nilai_dari_file(self):
		with tempfile.TemporaryDirectory() as direktori:
			path = Path(direktori) / "nilai.txt"
			path.write_text("80\n90\n70\n", encoding="utf-8")

			self.assertEqual(baca_nilai(path), [80, 90, 70])


if __name__ == "__main__":
	print("Rata-rata:", rata_rata([80, 90, 70]))
	unittest.main()
