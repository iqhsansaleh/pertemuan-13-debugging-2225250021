"""Perbaikan bug pembagi tetap pada perhitungan rata-rata.

Pembagi 5 hanya menghasilkan rata-rata yang benar jika data berisi lima
nilai. Gunakan panjang list agar jumlah data apa pun dihitung dengan benar.
"""

import unittest


def rata_rata(data):
	if not data:
		raise ValueError("Data tidak boleh kosong")
	return sum(data) / len(data)


class TestRataRata(unittest.TestCase):
	def test_satu_nilai(self):
		self.assertEqual(rata_rata([80]), 80)

	def test_tiga_nilai(self):
		self.assertEqual(rata_rata([80, 90, 70]), 80)

	def test_lima_nilai(self):
		self.assertEqual(rata_rata([60, 70, 80, 90, 100]), 80)

	def test_list_kosong(self):
		with self.assertRaisesRegex(ValueError, "Data tidak boleh kosong"):
			rata_rata([])


if __name__ == "__main__":
	print(rata_rata([80, 90, 70]))
	unittest.main()
