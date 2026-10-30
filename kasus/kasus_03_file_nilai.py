"""Kasus 3: membaca daftar nilai dari file teks.

Format file: satu nilai angka per baris. Baris kosong diabaikan.
"""

import tempfile
import unittest
from pathlib import Path


def baca_nilai(path):
	with open(path, encoding="utf-8") as file:
		return [int(baris.strip()) for baris in file if baris.strip()]


class TestBacaNilai(unittest.TestCase):
	def test_membaca_beberapa_nilai(self):
		with tempfile.TemporaryDirectory() as direktori:
			path = Path(direktori) / "nilai.txt"
			path.write_text("80\n90\n70\n", encoding="utf-8")

			self.assertEqual(baca_nilai(path), [80, 90, 70])

	def test_mengabaikan_baris_kosong(self):
		with tempfile.TemporaryDirectory() as direktori:
			path = Path(direktori) / "nilai.txt"
			path.write_text("80\n\n90\n", encoding="utf-8")

			self.assertEqual(baca_nilai(path), [80, 90])

	def test_file_tanpa_nilai_menghasilkan_list_kosong(self):
		with tempfile.TemporaryDirectory() as direktori:
			path = Path(direktori) / "nilai.txt"
			path.write_text("\n  \n", encoding="utf-8")

			self.assertEqual(baca_nilai(path), [])


if __name__ == "__main__":
	unittest.main()
